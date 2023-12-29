from uuid import UUID
from pydantic import (BaseModel)


class UserActivityModel(BaseModel):
	id: UUID
	user_id: UUID
	film_id: UUID
	event_name: str
	event_data: dict
