import os
from fastapi import FastAPI, Request
from routes.route import router

app = FastAPI()
app.include_router(router)

@app.get('/')
def hello():
    return 'Success'