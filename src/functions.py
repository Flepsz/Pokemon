import random
from pokemons import PokemonWater, PokemonGrass, PokemonFire, Pokemon, Rowlet, Popplio, Litten


def start_battle(pokemon, pk_bot):
    """
    Define quem vai começar a batalha de acordo com a "Speed" dos pokemons.
    :param pokemon: Pokemon do usuário
    :param pk_bot: Pokemon do bot
    """
    pokes = [pokemon.name, pk_bot.name]
    if pokemon.speed == pk_bot.speed:
        return random.choice(pokes)
    elif pokemon.speed > pk_bot.speed:
        return pokemon.name
    else:
        return pk_bot.name


print(Litten.show_stats())
print(Litten.attack)
print(Litten.mod_tipo(Rowlet))

print(Litten.damage(Rowlet, Litten.mod_tipo(Rowlet)))

