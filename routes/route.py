from fastapi import APIRouter
from models.user import User
from config.database import collection_name
from schema.schemas import list_serial
from bson import ObjectId

router = APIRouter()

@router.get("/")
async def get_users():
    users = list_serial(collection_name.find())
    
    return users