from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse

from services.message import MessageService, get_message_service
from schemas.entity import FilmHistoryPayloads, FilmLikePayloads, FilmCommentPayloads


router = APIRouter()


@router.post(
    '/film_history',
    summary='История просмотра фильма',
    description='Принимает сообщения о текущем состоянии просмотра фильма, который смотрит пользователь',
)
async def film_history(
    message: FilmHistoryPayloads,
    message_service: MessageService = Depends(get_message_service)
):
    topic = 'film_history'
    posted = await message_service.post_msg(topic, message)
    if posted:
        return JSONResponse(
            status_code=HTTPStatus.OK,
            content={
                'detail': 'message was posted'
            }
        )
    return HTTPException(
        status_code=HTTPStatus.SERVICE_UNAVAILABLE,
        detail="Message wasn't posted"
    )


@router.post(
    '/film_likes',
    summary='История лайков фильма',
    description='Принимает сообщения об установке пользователем лайка для фильма',
)
async def film_likes(
    message: FilmLikePayloads,
    message_service: MessageService = Depends(get_message_service)
):
    topic = 'film_likes'
    posted = await message_service.post_msg(topic, message)
    if posted:
        return JSONResponse(
            status_code=HTTPStatus.OK,
            content={
                'detail': 'message was posted'
            }
        )
    return HTTPException(
        status_code=HTTPStatus.SERVICE_UNAVAILABLE,
        detail="Message wasn't posted"
    )


@router.post(
    '/film_comments',
    summary='История комментариев фильма',
    description='Принимает сообщения о комментарии для фильма',
)
async def film_likes(
    message: FilmCommentPayloads,
    message_service: MessageService = Depends(get_message_service)
):
    topic = 'film_comments'
    posted = await message_service.post_msg(topic, message)
    if posted:
        return JSONResponse(
            status_code=HTTPStatus.OK,
            content={
                'detail': 'message was posted'
            }
        )
    return HTTPException(
        status_code=HTTPStatus.SERVICE_UNAVAILABLE,
        detail="Message wasn't posted"
    )
