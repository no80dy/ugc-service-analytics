from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field


class UGCPayloads(BaseModel):
    user_id: UUID


class FilmHistoryPayloads(UGCPayloads):
    film_id: UUID
    film_sec: int


class FilmLikePayloads(UGCPayloads):
    film_id: UUID
    like: bool


class FilmCommentPayloads(UGCPayloads):
    film_id: UUID
    comment: str


