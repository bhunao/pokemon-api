import pandas as pd
from dataclasses import dataclass


@dataclass(frozen=True)
class poke_type:
    value: str

    def __eq__(self, other):
        if other.value.lower() == "any":
            return True
        else:
            return self.value == other.value


@dataclass(frozen=True)
class Pokemon:
    """class that stores the pokemon data and has methods to compare and evaluate then"""
    id: int
    name: str
    type: tuple
    hp: int
    attack: int
    defense: int
    sp_attack: int
    sp_defense: int
    speed: int
    total: int
    sprite: str = None
    _is_mega: bool = None
    _evolution: object = None
    _devolution: object = None

    def __repr__(self):
        id = self.id
        name = self.name
        type = self.type

        return f"<{id=} {name=} {type=}>"

    def to_dict(self):
        return dict()

