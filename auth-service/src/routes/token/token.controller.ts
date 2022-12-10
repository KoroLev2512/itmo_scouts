import { Controller, Query } from '@nestjs/common';
import { decodeJWT } from 'src/providers/jwt.provider';
import { MessagePattern, Payload } from '@nestjs/microservices';
import { JwtPayload } from 'jsonwebtoken';

@Controller('token')
export class TokenController {
  @MessagePattern({ cmd: 'verify.token' })
  async verifyToken(@Payload('token') token: string): Promise<boolean> {
    return Boolean(decodeJWT(token));
  }

  @MessagePattern({ cmd: 'decode.token' })
  async decodeToken(@Payload() token: string): Promise<JwtPayload | string> {
    return decodeJWT(token);
  }
}
