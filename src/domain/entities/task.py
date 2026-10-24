from enum import Enum
from dataclasses import dataclass, field, replace
from domain.shared.utils import create_uuid4, crete_utctime
from datetime import datetime

class Priority(str, Enum):
    Normal = "Normal"
    Average = "Average"
    Urgent = "Urgent"

@dataclass(frozen=True, slots=True, kw_only=True)
class Task:
    id:str = field(default_factory=create_uuid4)
    title: str
    body: str = "body"
    created_at: datetime = field(default_factory=crete_utctime)
    priority: Priority = Priority.Normal
    version: int = 0

    def ch_priority(self, priority:Priority):
        return replace(self, priority=priority, version=self.version + 1)
    def ch_body(self, body:str):
        return replace(self, body=body, version=self.version + 1)
    def ch_title(self, title:str):
        return replace(self, title=title, version=self.version + 1)


