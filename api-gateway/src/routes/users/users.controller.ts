import {
  BadRequestException,
  Body,
  Controller,
  Get,
  Inject,
  Query,
} from '@nestjs/common';
import { ClientProxy } from '@nestjs/microservices';
import { JwtPayload } from 'jsonwebtoken';
import { MICROSERVICES } from 'src/common/const/microservices';
import { User } from 'src/types/user';

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
  async getToken(@Body() payload: User) {
    try {
      return await this.authClient.send({ cmd: 'get.token' }, payload);
    } catch (error) {
      throw new BadRequestException();
    }
  }
}
