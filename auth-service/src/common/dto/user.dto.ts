import { Exclude, Expose } from '@nestjs/class-transformer';

@Exclude()
export class UserDto {
  @Expose()
  id: number;
  @Expose()
  moderated: boolean;

  login: string;
  password: string;
}
