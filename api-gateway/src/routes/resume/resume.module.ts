import { Module } from '@nestjs/common';
import { ResumeService } from './resume.service';
import { ResumeController } from './resume.controller';

@Module({
  providers: [ResumeService],
  controllers: [ResumeController]
})
export class ResumeModule {}
