import os
import time

import models 
import schema

from typing import Dict

from fastapi import FastAPI, Request
from fastapi_sqlalchemy import DBSessionMiddleware, db

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.getenv('DATABASE_URL'))

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

@app.post("/register")
async def read_root(register_data: Dict):
    try:
        is_valid = schema.User(**register_data)
        if is_valid:
            user_data = models.User(email=register_data.get('email'), hashed_password=register_data.get('password'))
            db.session.add(user_data)
            db.session.commit()
        return {'user': user_data}
    except Exception as e:
        return str(e)



