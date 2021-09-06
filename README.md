# pokemon-api

## endpoints  

### __`/pokemon`__
search pokemons by attributes using qury parameters. the pokemon attributes are id,name,type,total,hp,attack,defense,sp_attack,sp_defense.

__example:__  
`http://localhost:8000/pokemon/?name=bulbasaur`

## __pokedex__`(csv)`
stores all the pokemons objects.

### __search_by__`(**attributes)
returns all pokemons that match the attributes passed as parameters.

```python
pokedex.search_by(name="bulbasaur")
>> <id=1 name="bulbasaur" type=["grass", "poison"]>
```
