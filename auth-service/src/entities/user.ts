import { BaseEntity, Entity, Column, PrimaryColumn } from 'typeorm';

@Entity('user')
export class User extends BaseEntity {
  @PrimaryColumn()
  id: number;

  @Column()
  login: string;

  @Column()
  password: string;
}
