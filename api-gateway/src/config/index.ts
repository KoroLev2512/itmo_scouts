import { ConfigModule } from '@nestjs/config';

export const EnvConfig = ConfigModule.forRoot({
  envFilePath: '../../.env',
});
