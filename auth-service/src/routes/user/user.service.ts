import { Injectable } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { Repository } from 'typeorm';
import { User } from 'src/entities/user';
import { plainToClass } from '@nestjs/class-transformer';
import { UserDto } from 'src/common/dto/user.dto';

@Injectable()
export class UserService {
  constructor(
    @InjectRepository(User) private readonly repository: Repository<User>,
  ) {}

  async getUsers(): Promise<UserDto[]> {
    return this.repository.find();
  }

  async getUser(id: number): Promise<User> {
    return this.repository.findOne({ where: { id } });
  }

  async createUser(user: UserDto): Promise<UserDto> {
    const existingUser = await this.repository.findOne({
      where: { login: user.login },
    });

    return existingUser || (await this.repository.save(user));
  }
}
