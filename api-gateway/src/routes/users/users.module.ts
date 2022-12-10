import { Module } from '@nestjs/common';
import { AuthMicroservice } from 'src/config/microservices';
import { UsersController } from './users.controller';
import { UsersService } from './users.service';

@Module({
  imports: [AuthMicroservice],
  controllers: [UsersController],
  providers: [UsersService],
})
export class UsersModule {}
