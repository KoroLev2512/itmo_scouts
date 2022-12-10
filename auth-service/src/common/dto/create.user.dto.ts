import { Exclude, Expose } from '@nestjs/class-transformer';

@Exclude()
export class CreateUserDto {
  @Expose()
  id: number;
  login: string;
  password: string;
}
