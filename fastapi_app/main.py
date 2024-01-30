import uvicorn
from fastapi import FastAPI
from core.logger.api_logger import ApiLogger
from core.logger.middleware_logger import log_middleware
from starlette.middleware.base import BaseHTTPMiddleware

# get logger for module
LOGGER = ApiLogger().logger


def init_app():
    apps = FastAPI(
        title="BOZEN FASTAPI Practice",
        description="Fast API",
        version="1.0.0"
    )
    apps.add_middleware(middleware_class=BaseHTTPMiddleware, dispatch=log_middleware)

    @apps.on_event("startup")
    async def startup():
        msg = {'msg': "--- Start up App ---"}
        LOGGER.info(msg=msg)
        pass

    @apps.on_event("shutdown")
    async def shutdown():
        msg = {'msg': "--- Shut down App ---"}
        LOGGER.info(msg=msg)
        pass

    @apps.get('/')
    def home():
        msg = {'msg': "Welcome home on main.py !"}
        return msg

    from fastapi_app.controllers import home, index

    apps.include_router(home.router)
    apps.include_router(index.router)

    return apps


app = init_app()

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8888, reload=True)
