from fastapi import APIRouter
from core.logger.api_logger import ApiLogger
from fastapi import Path

# Get logger for module
LOGGER = ApiLogger().logger

router = APIRouter(
    prefix="/index",
    tags=['index']
)


@router.get("/")
async def index():
    msg = {'msg': "Welcome index page !"}
    LOGGER.info(msg=msg)
    return msg


inventory = {
    1: {
        "name": "Milk",
        "price": 3.99,
        "brand": "Regular"
    }
}


@router.get("/{item_id}")
async def index_item(
        item_id: int = Path(default_factory=None, description="The ID of the item you'd like to view.", gt=0, lt=2)):
    item = inventory[item_id]
    msg = {'msg': f"Welcome index/{item_id} page {item}!"}
    LOGGER.info(msg=msg)
    return msg
