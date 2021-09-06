import pandas as pd
from dataclasses import dataclass, field

from pokemon import Pokemon


class Pokedex:
    """class that hold the pokemon objects"""

    def __init__(self, csv):
        self.pokedex = self.load_pokedex_from_csv(csv)

    @staticmethod
    def load_pokedex_from_csv(csv):
        poke_df = pd.read_csv(csv).fillna(0)
        poke_list = poke_df.to_dict(orient="records")

        pokedex = []
        for poke_attrs in poke_list:
            poke_attrs["type"] = poke_attrs.get("type").split()
            pokemon = Pokemon(**poke_attrs)
            pokedex.append(pokemon)

        return pokedex

    def search_by(self, **attributes):
        result = []
        poke_attrs = {k: v for k, v in attributes.items() if v}


        for pokemon in self.pokedex:
            if pokemon.__dict__.items() >= poke_attrs.items():
                print(poke_attrs, pokemon)
                result.append(pokemon)

        return result


def main():
    path = "data.csv"
    pokedex = Pokedex(path)
    pokemon = pokedex.search_by(id=1)


if __name__ == "__main__":
    main()
