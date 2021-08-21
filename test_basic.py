import pandas as pd
import random
from fastapi.testclient import TestClient

from pokemon import api


# data for the tests
pokemon_df = pd.read_csv("data.csv").fillna(0)
pokemon_id = random.randint(1, len(pokemon_df))
pokemon_data = pokemon_df.iloc[list(pokemon_df["#"] == pokemon_id)]
pokemon_dict = pokemon_data.to_dict(orient="records:")

client = TestClient(api)

def test_get_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "pokemon-api"}


def test_get_pokemon():
    response = client.get(f"pokemon/{pokemon_id}")
    json_response = response.json()

    assert response.status_code == 200
    assert json_response[0].get("#") == pokemon_id
    assert json_response[0].get("Name") == pokemon_dict[0]["Name"]
    assert json_response[0].get("Type1") == pokemon_dict[0]["Type1"]
    assert json_response[0].get("Type2") == pokemon_dict[0]["Type2"]
    assert json_response[0].get("HP") == pokemon_dict[0]["HP"]
