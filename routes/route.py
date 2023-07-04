from fastapi import APIRouter, Request
from models.user import User
from config.database import collection_name
from schema.schemas import list_serial, individual_serial
from bson import ObjectId

router = APIRouter()

@router.get("/users-list/{id}")
def get_users(id: str):
    if not id:
        return "Params not found"
    if id == 'all':
        users = list_serial(collection_name.find())
        return {"data": users}
    
    users = individual_serial(collection_name.find_one({"_id":ObjectId(id)}))
    if not users:
        return 404
    return {'data': users}

@router.post("/register")
def register(data: User):
    collection_name.insert_one(dict(data))
    
    return 200