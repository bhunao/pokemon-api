from typing import List, Optional

from pydantic import BaseModel


class PokemonBase(BaseModel):
    name: str
    type: str
    hp: int
    attack: int
    defense: int
    sp_attack: int
    sp_defense: int
    speed: int
    total: int
    sprite: str


class PokemonCreate(PokemonBase):
    pass


class Pokemon(PokemonBase):
    id: int

    class Config:
        orm_mode = True


