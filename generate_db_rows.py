from sql_app import crud, models

from sql_app.database import SessionLocal

from sqlalchemy.orm import Session

import pandas as pd


db = SessionLocal()

def load_pokemon_from_csv(csv, db: Session = db):
    df = pd.read_csv(csv).fillna(0)
    pokemons_list = df.to_dict(orient="records")

    for pokemon in pokemons_list:
        pokemon["national_id"] = pokemon["id"]
        del pokemon["id"]

        crud.create_pokemon(db=db, pokemon=pokemon)

def main():
    print("adding pokemons to the database...")
    load_pokemon_from_csv("data.csv", db=db)
    print("done")


if __name__ == "__main__":
    main()
