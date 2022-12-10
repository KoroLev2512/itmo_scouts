import { ClientsModule, Transport } from '@nestjs/microservices';
import { MICROSERVICES } from 'src/common/const/microservices';

export const StudentMicroservice = ClientsModule.register([
  {
    name: MICROSERVICES.STUDENT_MICROSERVICE,
    transport: Transport.TCP,
    options: {
      host: process.env.STUDENT_SERVICE_HOST,
      port: +process.env.STUDENT_SERVICE_PORT,
    },
  },
]);

export const CompanyMicroservice = ClientsModule.register([
  {
    name: MICROSERVICES.COMPANY_MICROSERVICE,
    transport: Transport.TCP,
    options: {
      host: process.env.COMPANY_SERVICE_HOST,
      port: +process.env.COMPANY_SERVICE_PORT,
    },
  },
]);
