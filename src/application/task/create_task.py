from application.interfaces.uow import UnitOfWorkProtocol
from application.task.dtos import CreateTaskRequestDTO
from domain.entities.task import Task


class CreateTaskUseCase:
    def __init__(self, uow: UnitOfWorkProtocol):
        self.uow = uow

    def execute(self, request: CreateTaskRequestDTO) -> str:
        with self.uow as db:
            task = Task(title=request.title, body=request.body, priority=request.priority)

            db.tasks.save(task=task)
            db.commit()

            return task.id

