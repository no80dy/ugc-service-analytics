from uuid import UUID
from typing_extensions import Literal

from pydantic import BaseModel


class UGCPayloads(BaseModel):
    user_id: UUID
    film_id: UUID


class FilmHistoryPayloads(UGCPayloads):
    event_name: Literal['film_history']
    film_sec: int


class FilmLikePayloads(UGCPayloads):
    event_name: Literal['film_likes']
    like: bool


class FilmCommentPayloads(UGCPayloads):
    event_name: Literal['film_comments']
    comment: str


