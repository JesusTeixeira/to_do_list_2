from typing import Optional
from sqlmodel import Field, SQLModel


class Todo(SQLModel, table=True):
    task_id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    done: bool
