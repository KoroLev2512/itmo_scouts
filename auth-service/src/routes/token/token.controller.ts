import { Controller, Inject } from '@nestjs/common';
import { decodeJWT, signJWT } from 'src/providers/jwt.provider';
import { MessagePattern, Payload } from '@nestjs/microservices';
import { JwtPayload } from 'jsonwebtoken';
import { UserService } from '../user/user.service';

@Controller('token')
export class TokenController {
  constructor(@Inject(UserService) private readonly userService: UserService) {}
  @MessagePattern({ cmd: 'verify.token' })
  async verifyToken(@Payload('token') token: string): Promise<boolean> {
    return Boolean(decodeJWT(token));
  }

  @MessagePattern({ cmd: 'decode.token' })
  async decodeToken(@Payload() token: string): Promise<JwtPayload | string> {
    const payload = decodeJWT(token);

    if (!payload?.id) {
      return;
    }

    const user = await this.userService.getUser(payload.id);

    return user && decodeJWT(token);
  }

  @MessagePattern({ cmd: 'get.token' })
  async getToken(@Payload() payload: JwtPayload): Promise<string> {
    const user = await this.userService.getUser(payload?.id);
    return user && signJWT(payload);
  }
}
