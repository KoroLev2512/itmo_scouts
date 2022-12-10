import { Controller, Query } from '@nestjs/common';
import { decodeJWT } from 'src/providers/jwt.provider';
import { MessagePattern } from '@nestjs/microservices';
import { JwtPayload } from 'jsonwebtoken';

@Controller('token')
export class TokenController {
  @MessagePattern({ cmd: 'verify.token' })
  async verifyToken(@Query('token') token: string): Promise<boolean> {
    console.log(token);

    return Boolean(decodeJWT(token));
  }

  @MessagePattern({ cmd: 'decode.token' })
  async decodeToken(
    @Query('token') token: string,
  ): Promise<JwtPayload | string> {
    return decodeJWT(token);
  }
}
