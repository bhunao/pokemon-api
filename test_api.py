from endpoints import api

import pandas as pd
import random
from fastapi.testclient import TestClient


client = TestClient(api)

bulba = [
          {
            "id": 1,
            "name": "bulbasaur",
            "type": [
              "grass",
              "poison"
            ],
            "hp": 45,
            "attack": 49,
            "defense": 49,
            "sp_attack": 65,
            "sp_defense": 65,
            "speed": 45,
            "total": 318,
            "sprite": "https://img.pokemondb.net/sprites/sword-shield/icon/bulbasaur.png",
            "_is_mega": None,
            "_evolution": None,
            "_devolution": None
          }
        ]

def test_get_pokemon_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"msg": "pokemon-api"}

def test_get_by_id():
    response = client.get("/pokemon/?id=1")

    assert response.status_code == 200
    assert response.json() == bulba

def test_get_by_name():
    response = client.get("/pokemon/?name=bulbasaur")

    assert response.status_code == 200
    assert response.json() == bulba
