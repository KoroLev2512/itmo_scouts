import {
  BadRequestException,
  Controller,
  Get,
  Inject,
  Query,
} from '@nestjs/common';
import { ClientProxy } from '@nestjs/microservices';
import { JwtPayload } from 'jsonwebtoken';
import { MICROSERVICES } from 'src/common/const/microservices';

@Controller('users')
export class UsersController {
  constructor(
    @Inject(MICROSERVICES.AUTH_MICROSERVICE) private authClient: ClientProxy,
  ) {}

  @Get('token/verify')
  async verifyUser(@Query('token') token: JwtPayload) {
    return this.authClient.send({ cmd: 'verify.token' }, { token });
  }

  @Get('token')
  async getToken(@Query() payload: JwtPayload) {
    try {
      return await this.authClient
        .send({ cmd: 'decode.token' }, payload)
        .subscribe();
    } catch (error) {
      throw new BadRequestException('sss');
    }
  }
}
