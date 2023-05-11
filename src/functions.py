import random
import sys
import time
from pokemons import PokemonWater, PokemonGrass, PokemonFire, Pokemon, Rowlet, Popplio, Litten


def print_delay(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
    print()


def attacking(pokemon, pk_bot):
    pokemon.mod_tipo(pk_bot)
    return pokemon.damage(pk_bot, pokemon.mod_tipo(pk_bot))


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


# print(Litten.show_stats())
# print(Litten.mod_tipo(Rowlet))
# print("lol")
# damage = Litten.damage(Rowlet, Litten.mod_tipo(Rowlet))
# Rowlet.hp_loss(damage[0])
# print(damage[1])
# print(f"Rowlet perdeu {damage[0]:.2f} de vida")
# print(Rowlet.show_health())
#
# damage = Litten.damage(Rowlet, Litten.mod_tipo(Rowlet))
# Rowlet.hp_loss(damage[0])
# print(damage[1])
# print(f"Rowlet perdeu {damage[0]:.2f} de vida")
# print(Rowlet.show_health())


def test(pokemon, pk_bot, damage, effect):
    pk_bot.hp_loss(damage)
    print(effect)
    print(f"{pk_bot.name} perdeu {damage:.2f} de vida")
    print(pk_bot.show_health())


# damage = attacking(Litten, Rowlet)[0]
# effect = attacking(Litten, Rowlet)[1]
# print(Rowlet.show_health())
# test(Litten, Rowlet, damage, effect)
# test(Litten, Rowlet, damage, effect)

