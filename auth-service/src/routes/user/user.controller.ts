import { Controller, Get } from '@nestjs/common';
import { MessagePattern } from '@nestjs/microservices';
import { User } from 'src/entities/user';
import { UserService } from './user.service';

@Controller('users')
export class UserController {
  constructor(private userService: UserService) {}

  @MessagePattern({ cmd: 'get.users' })
  async getUsers(): Promise<User[]> {
    return this.userService.getUsers();
  }
}
