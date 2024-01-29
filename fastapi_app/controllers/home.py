from fastapi import APIRouter
from core.logger.api_logger import ApiLogger

# Get logger for module
LOGGER = ApiLogger().logger

router = APIRouter(
    prefix="/home",
    tags=['home']
)


@router.get("")
async def home():
    msg = {'msg': "Welcome home page !"}
    LOGGER.info(msg=msg)
    return msg


@router.get("/test")
async def home_test():
    msg = {'msg': "Welcome home/test page !"}
    LOGGER.info(msg=msg)
    return msg
