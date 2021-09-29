from sqlalchemy.orm import Session

from . import models, schemas


def get_pokemon(db: Session, pokemon_id: int):
    return db.query(models.Pokemon).filter(models.Pokemon.id == pokemon_id).first()

def get_pokemon_by_name(db: Session, pokemon_name):
    return db.query(models.Pokemon).filter(models.Pokemon.name == pokemon_name).first()

def get_pokemons(db: Session, skip: int = 0, limit: int = 150):
    return db.query(models.Pokemon).offset(skip).limit(limit).all()

def create_pokemon(db: Session, pokemon: schemas.PokemonCreate):
    if isinstance(pokemon, dict):
        db_pokemon = models.Pokemon(**pokemon)
    else:
        db_pokemon = models.Pokemon(**pokemon.dict())
    db.add(db_pokemon)
    db.commit()
    db.refresh(db_pokemon)
    return db_pokemon

def delete_pokemon(db: Session, pokemon: schemas.Pokemon):
    db.delete(pokemon)
    db.commit()
    return {"message": "pokemon deleted"}
