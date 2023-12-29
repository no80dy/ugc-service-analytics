from http import HTTPStatus
from typing import Union

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse

from services.event import EventService, get_event_service
from schemas.entity import FilmHistoryPayloads, FilmLikePayloads, FilmCommentPayloads


router = APIRouter()


@router.post(
    '/post_event',
    summary='Сбор статистики',
    description='Принимает события, связанные с фильмами, от конкретного пользователя: \
                История просмотра фильма, лайки, комментарии',

)
async def post_event(
    event_payloads: Union[FilmHistoryPayloads, FilmLikePayloads, FilmCommentPayloads],
    event_service: EventService = Depends(get_event_service)
):
    posted = await event_service.post_event(event_payloads)

    if posted:
        return JSONResponse(
            status_code=HTTPStatus.OK,
            content={
                'detail': 'event is posted',
            }
        )
    return HTTPException(
        status_code=HTTPStatus.SERVICE_UNAVAILABLE,
        detail={
            'detail': 'event is not posted',
        }
    )
