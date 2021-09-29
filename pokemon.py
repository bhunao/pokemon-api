import pandas as pd
from dataclasses import dataclass, field


@dataclass(frozen=True)
class Pokemon:
    """class that stores the pokemon data and has methods to compare and evaluate then"""
    id: int
    name: str
    type: tuple
    hp: int = field(repr=False)
    attack: int = field(repr=False)
    defense: int = field(repr=False)
    sp_attack: int = field(repr=False)
    sp_defense: int = field(repr=False)
    speed: int = field(repr=False)
    total: int = field(repr=False)
    sprite: str = field(repr=False, default=None)
    _is_mega: bool = field(repr=False, default=None)
    _evolution: object = field(repr=False, default=None)
    _devolution: object = field(repr=False, default=None)
