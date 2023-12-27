import uvicorn

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from api.v1 import statistic
from core.config import settings


REQUEST_LIMIT_PER_MINUTE = 20


app = FastAPI(
    description='Сервис сбора статистики',
    version='1.0.0',
    # Конфигурируем название проекта. Оно будет отображаться в документации
    title=settings.project_name,
    # Адрес документации в красивом интерфейсе
    docs_url='/ugc/api/openapi',
    # Адрес документации в формате OpenAPI
    openapi_url='/ugc/api/openapi.json',
    default_response_class=JSONResponse,
)


app.include_router(statistic.router, prefix='/ugc/api/v1/statistic', tags=['statistic'])


if __name__ == '__main__':
    # Приложение может запускаться командой
    # `uvicorn main:app --host 0.0.0.0 --port 8000 --reload`
    uvicorn.run(
        'main:app',
        host='0.0.0.0',
        port=8000,
        reload=True
    )
