import { ClientsModule, Transport } from '@nestjs/microservices';
import { MICROSERVICES } from 'src/common/const/microservices';

export const StudentMicroservice = ClientsModule.register([
  {
    name: MICROSERVICES.STUDENT_MICROSERVICE,
    transport: Transport.TCP,
    options: {
      port: +process.env.STUDENT_SERVICE_PORT,
    },
  },
]);

export const CompanyMicroservice = ClientsModule.register([
  {
    name: MICROSERVICES.COMPANY_MICROSERVICE,
    transport: Transport.TCP,
    options: {
      port: +process.env.COMPANY_SERVICE_PORT,
    },
  },
]);

export const AuthMicroservice = ClientsModule.register([
  {
    name: MICROSERVICES.AUTH_MICROSERVICE,
    transport: Transport.TCP,
    options: {
      port: +process.env.AUTH_SERVICE_PORT,
    },
  },
]);
