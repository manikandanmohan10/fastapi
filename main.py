import os
import time

from fastapi import FastAPI, Request
from fastapi_sqlalchemy import DBSessionMiddleware
from models import *

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.getenv('DATABASE_URL'))

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

@app.get("/")
async def read_root():
    return {"Hello": "World"}

