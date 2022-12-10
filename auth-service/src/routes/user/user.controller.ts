import { plainToClass } from '@nestjs/class-transformer';
import { Controller, Get, Inject } from '@nestjs/common';
import { MessagePattern, Payload } from '@nestjs/microservices';
import { UserDto } from 'src/common/dto/user.dto';
import { User } from 'src/entities/user';
import { UserService } from './user.service';

@Controller('users')
export class UserController {
  constructor(@Inject(UserService) private userService: UserService) {}

  @MessagePattern({ cmd: 'get.users' })
  async getUsers(): Promise<UserDto[]> {
    return (await this.userService.getUsers()).map((u) =>
      plainToClass(UserDto, u),
    );
  }

  @MessagePattern({ cmd: 'get.user' })
  async getUser(@Payload('id') id: number): Promise<UserDto> {
    return plainToClass(UserDto, this.userService.getUser(id));
  }

  @MessagePattern({ cmd: 'create.user' })
  async createUser(@Payload() dto: User) {
    return plainToClass(UserDto, this.userService.createUser(dto));
  }
}
