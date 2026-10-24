from domain.entities.task import Priority
from dataclasses import dataclass

@dataclass(frozen=True, slots=True, kw_only=True)
class CreateTaskRequestDTO:
    title: str
    body: str
    priority: Priority
