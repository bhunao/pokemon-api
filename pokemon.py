from fastapi import FastAPI
from data import get_pokemon_by_id

api = FastAPI()

@api.get("/")
async def home():
    return {"msg": "pokemon-api"}


@api.get("/pokemon/{id}")
async def get_pokemon(id: int):
    return get_pokemon_by_id(id)
