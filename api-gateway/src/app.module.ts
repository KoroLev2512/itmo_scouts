import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { EnvConfig } from './config';
import {
  CompanyMicroservice,
  StudentMicroservice,
} from './config/microservices';
import { CompaniesModule } from './routes/companies/companies.module';
import { JobsModule } from './routes/jobs/jobs.module';
import { ProjectsModule } from './routes/projects/projects.module';
import { ResumeModule } from './routes/resume/resume.module';
import { StudentsModule } from './routes/students/students.module';
import { UsersModule } from './routes/users/users.module';

@Module({
  imports: [
    EnvConfig,
    CompanyMicroservice,
    StudentMicroservice,
    UsersModule,
    CompaniesModule,
    StudentsModule,
    ResumeModule,
    ProjectsModule,
    JobsModule,
  ],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
