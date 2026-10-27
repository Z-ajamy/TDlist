import re
from pydantic import BaseModel, Field, ConfigDict, field_validator
from domain.entities.task import Priority
from application.task.dtos import CreateTaskRequestDTO

class CreateTaskSchema(BaseModel):
    model_config = ConfigDict(
        extra="forbid",     
        str_strip_whitespace=True
        )

    title: str = Field(
        ..., 
        min_length=3, 
        max_length=100,
    )
    
    body: str = Field(
        default="", 
        max_length=1000,
    )
    
    priority: Priority = Field(
        default=Priority.Normal,
    )

    @field_validator("title")
    @classmethod
    def sanitize_title(cls, v: str) -> str:
        cleaned_title = re.sub(r'\s+', ' ', v)
        if not cleaned_title:
            raise ValueError("Title cannot be empty after sanitization.")
        return cleaned_title

    def to_dto(self) -> CreateTaskRequestDTO:
        return CreateTaskRequestDTO(
            title=self.title,
            body=self.body,
            priority=self.priority
        )
