import { Injectable } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { Repository } from 'typeorm';
import { User } from 'src/entities/user';

@Injectable()
export class UserService {
  constructor(
    @InjectRepository(User) private readonly repository: Repository<User>,
  ) {}

  async getUsers(): Promise<User[]> {
    return this.repository.find();
  }
}
