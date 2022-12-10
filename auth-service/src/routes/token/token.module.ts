import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { User } from 'src/entities/user';
import { UserModule } from '../user/user.module';
import { TokenController } from './token.controller';

@Module({
  imports: [TypeOrmModule.forFeature([User]), UserModule],
  controllers: [TokenController],
})
export class TokenModule {}
