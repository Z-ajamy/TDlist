from domain.entities.task import Task, Priority
from infrastructure.database.models.task_model import TaskModel

class TaskMapper:

    @staticmethod
    def from_orm(task_model:TaskModel) -> Task:
        return Task(id=task_model.id,
            title=task_model.title,
            body=task_model.body,
            created_at=task_model.created_at,
            priority=Priority(task_model.priority),
            version=task_model.version
        )

    @staticmethod
    def to_orm(task_entity:Task) -> TaskModel:
        return TaskModel(
                id=task_entity.id,
                title=task_entity.title,
                body=task_entity.body,
                created_at=task_entity.created_at,
                priority=task_entity.priority.value,
                version=task_entity.version
            )
