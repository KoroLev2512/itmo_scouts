import { Module } from '@nestjs/common';
import { StudentsService } from './students.service';

@Module({
  providers: [StudentsService],
})
export class StudentsModule {}
