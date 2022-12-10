import { Module } from '@nestjs/common';
import { ConfigModule } from '@nestjs/config';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { AuthModule } from './routes/auth/auth.module';
import { TokenModule } from './routes/token/token.module';

@Module({
  imports: [ConfigModule.forRoot({ isGlobal: true }), TokenModule, AuthModule],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
