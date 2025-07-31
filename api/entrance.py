from core.fastapi import fastApp

@fastApp.get("/")
async def read_root():
    return {"Hello": "World"}