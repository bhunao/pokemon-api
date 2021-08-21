import pandas as pd


def get_pokemon_by_id(id: int):
    """returns a dictionary with the data of the pokemon with the `id` parameter"""
    pokemon_df = pd.read_csv("data.csv").fillna(0)
    if 0 < id < len(pokemon_df):
        pokemon_data = pokemon_df.iloc[list(pokemon_df["#"] == id)]
        pokemon_dict = pokemon_data.to_dict(orient="records:")
        print("{pokemon_dict=}")
        return pokemon_dict

