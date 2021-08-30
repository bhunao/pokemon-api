from endpoints import api

import pandas as pd
import random
from fastapi.testclient import TestClient


client = TestClient(api)

def test_endpoint_get_pokemon_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "pokemon-api"}

