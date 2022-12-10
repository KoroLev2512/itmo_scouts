import { Controller, Get, Inject } from '@nestjs/common';
import { MessagePattern, Payload } from '@nestjs/microservices';
import { User } from 'src/entities/user';
import { UserService } from './user.service';

@Controller('users')
export class UserController {
  constructor(@Inject(UserService) private userService: UserService) {}

  @MessagePattern({ cmd: 'get.users' })
  async getUsers(): Promise<User[]> {
    return this.userService.getUsers();
  }

  @MessagePattern({ cmd: 'get.user' })
  async getUser(@Payload('id') id: number): Promise<User> {
    return this.userService.getUser(id);
  }

  @MessagePattern({ cmd: 'create.user' })
  async createUser(@Payload() dto: User) {
    return this.userService.createUser(dto);
  }
}
