import { Injectable } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { Repository } from 'typeorm';
import { User } from 'src/entities/user';
import { plainToClass } from '@nestjs/class-transformer';
import { CreateUserDto } from 'src/common/dto/create.user.dto';

@Injectable()
export class UserService {
  constructor(
    @InjectRepository(User) private readonly repository: Repository<User>,
  ) {}

  async getUsers(): Promise<User[]> {
    return this.repository.find();
  }

  async getUser(id: number): Promise<User> {
    return this.repository.findOne({ where: { id } });
  }

  async createUser(user: CreateUserDto): Promise<CreateUserDto> {
    const existingUser = await this.repository.findOne({
      where: { login: user.login },
    });

    const result = existingUser || (await this.repository.save(user));

    return plainToClass(CreateUserDto, result);
  }
}
