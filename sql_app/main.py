from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/pokemon/", response_model=schemas.Pokemon)
def create_pokemon(pokemon: schemas.PokemonCreate, db: Session = Depends(get_db)):
    return crud.create_pokemon(db=db, pokemon=pokemon)

@app.get("/pokemons/", response_model=List[schemas.Pokemon])
def read_pokemons(skip: int = 0, limit: int = 150, db: Session = Depends(get_db)):
    pokemons = crud.get_pokemons(db=db, skip=skip, limit=limit)
    return pokemons

@app.get("/pokemon/", response_model=schemas.Pokemon)
def read_pokemon(pokemon_id: int, db: Session = Depends(get_db)):
    db_pokemon = crud.get_pokemon(db=db, pokemon_id=pokemon_id)
    if db_pokemon is None:
        raise HTTPException(status_code=400, detail="pokemon not found")
    return db_pokemon

@app.delete("/pokemon/{pokemon_id}")
def delete_pokemon(pokemon_id: int, db: Session = Depends(get_db)):
    db_pokemon = crud.get_pokemon(db=db, pokemon_id=pokemon_id)
    if db_pokemon is None:
        raise HTTPException(status_code=400,
                            detail=f"theres no pokemon with id \"{pokemon_id}\"")
    return crud.delete_pokemon(db=db, pokemon=db_pokemon)
