from uuid import UUID
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query, Path

from .auth import security


router = APIRouter()

DETAIL = 'films not found'


@router.post(
    '/{film_id}',
    # response_model=Film,
    summary='Добавление лайка к фильму',
    description='Данный эндпоинт осуществляет добавление лайка к фильмую',
    response_description='Добавление лайка к фильму',
)
async def film_details(
    user: Annotated[dict, Depends(security)],
    film_id: Annotated[UUID, Path(description='Идентификатор кинопроизведения')],
) -> []:
    # здесь будет обработан запрос на добавление лайков к фильму по его айди
    return []
