from fastapi import FastAPI

api = FastAPI()

@api.get("/")
async def home():
    return {"msg": "pokemon-api"}


@api.get("/pokemon/{id}")
async def get_pokemon(id: int):
    pass
