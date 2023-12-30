import uuid

from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, Field


class UserActivityModel(BaseModel):
	id: UUID = Field(default_factory=uuid.uuid4)
	user_id: UUID
	film_id: UUID
	event_name: str
	comment: str | None = Field(default=None)
	film_sec: int | None = Field(default=None)
	like: bool = Field(default=False)
	event_time: datetime = Field(default_factory=datetime.now)
