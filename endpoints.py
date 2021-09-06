from fastapi import FastAPI
from pydantic import BaseModel

from typing import Optional

from pokedex import Pokedex


api = FastAPI()
pokedex = Pokedex("data.csv")



@api.get("/")
async def home():
    return {"msg": "pokemon-api"}


@api.get("/pokemon/")
async def get_pokemon(id: Optional[int] = None,
                        name: Optional[str] = None,
                        type: Optional[tuple] = None,
                        hp: Optional[int] = None,
                        attack: Optional[int] = None,
                        defense: Optional[int] = None,
                        sp_attack: Optional[int] = None,
                        sp_defense: Optional[int] = None,
                        speed: Optional[int] = None,
                        total: Optional[int] = None):
    
    return pokedex.search_by(id=id,
                            name=name,
                            type=type,
                            hp=hp,
                            attack=attack,
                            defense=defense,
                            sp_attack=sp_attack,
                            sp_defense=sp_defense,
                            speed=speed,
                            total=total)
