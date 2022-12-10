const bcrypt = require('bcrypt');
import {
  BadRequestException,
  Body,
  Controller,
  Get,
  Inject,
  Param,
  Post,
  Query,
} from '@nestjs/common';
import { ClientProxy } from '@nestjs/microservices';
import { JwtPayload } from 'jsonwebtoken';
import { SALT_ROUNDS } from 'src/common/const/bcrypt';
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
      return this.authClient.send({ cmd: 'get.token' }, payload);
    } catch (error) {
      throw new BadRequestException();
    }
  }

  @Get()
  async getUsers() {
    return this.authClient.send({ cmd: 'get.users' }, {});
  }

  @Get(':id')
  async getUser(@Param('id') id: string) {
    return this.authClient.send({ cmd: 'get.user' }, { id });
  }

  @Post()
  async createUser(@Body() dto: User) {
    const password = await bcrypt.hash(dto.password, SALT_ROUNDS);
    return this.authClient.send({ cmd: 'create.user' }, { ...dto, password });
  }
}
