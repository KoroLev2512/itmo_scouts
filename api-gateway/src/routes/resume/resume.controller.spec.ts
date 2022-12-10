import { Test, TestingModule } from '@nestjs/testing';
import { ResumeController } from './resume.controller';

describe('ResumeController', () => {
  let controller: ResumeController;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      controllers: [ResumeController],
    }).compile();

    controller = module.get<ResumeController>(ResumeController);
  });

  it('should be defined', () => {
    expect(controller).toBeDefined();
  });
});
