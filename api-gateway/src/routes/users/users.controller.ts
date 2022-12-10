import { Controller, Get, Inject, Query } from '@nestjs/common';
import { ClientProxy } from '@nestjs/microservices';
import { JwtPayload } from 'jsonwebtoken';
import { MICROSERVICES } from 'src/common/const/microservices';

@Controller('users')
export class UsersController {
  constructor(
    @Inject(MICROSERVICES.AUTH_MICROSERVICE) private authClient: ClientProxy,
  ) {}

  @Get('verify')
  async verifyUser(@Query('token') payload: JwtPayload) {
    return this.authClient.send({ cmd: 'verify.token' }, payload);
  }
}
