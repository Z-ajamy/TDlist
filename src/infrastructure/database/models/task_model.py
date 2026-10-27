from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from infrastructure.database.models.base import Base
from datetime import datetime
class TaskModel(Base):
    __tablename__ = "tasks"

    id: Mapped[str] = mapped_column(String(32), primary_key=True)

    title: Mapped[str] = mapped_column(String(100), nullable=False)
    body: Mapped[str] = mapped_column(String(1000), default="")
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    priority: Mapped[str] = mapped_column(String(20), nullable=False)
    version: Mapped[int] = mapped_column(default=0, nullable=False)
