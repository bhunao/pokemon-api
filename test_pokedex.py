import pandas as pd
import random
from fastapi.testclient import TestClient

from endpoints import api
from pokemon import Pokemon
from pokedex import Pokedex


client = TestClient(api)

def test_pokemon_object():
    id = 1
    pokedex = Pokedex("data.csv")
    pokemon = pokedex.search_by(id=id)[0]

    assert pokemon is not None

def test_pokedex_search_by():
    id = 1
    pokedex = Pokedex("data.csv")
    pokemon = pokedex.search_by(id=id)[0]

    assert pokemon.name.lower() == "bulbasaur"
    assert "grass" in pokemon.type
    assert pokemon.total == 318
    assert pokemon.hp == 45
    assert pokemon.attack == 49
    assert pokemon.defense == 49
    assert pokemon.sp_attack == 65
    assert pokemon.sp_defense == 65
    assert pokemon.speed == 45

def test_search_by_type():
    type_ = ["fire"]
    pokedex = Pokedex("data.csv")
    pokemon = pokedex.search_by(type=type_)

    assert pokemon is not None

def test_search_by_name():
    name = "litten"
    pokedex = Pokedex("data.csv")
    pokemon = pokedex.search_by(name=name)

    assert pokemon is not None
