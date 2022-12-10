import { ConfigModule } from '@nestjs/config';

export const EnvConfig = ConfigModule.forRoot({
  isGlobal: true,
});
