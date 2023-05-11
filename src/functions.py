import random
import sys
import time
import os
from pokemons import PokemonWater, PokemonGrass, PokemonFire, Pokemon, Rowlet, Popplio, Litten


def print_delay(s):
    print()
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
    print()
    time.sleep(1)


def clear():
    os.system('cls')


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


def hp_atk_taken(pokemon, pk_bot):
    damage = attacking(pokemon, pk_bot)[0]
    effect = attacking(pokemon, pk_bot)[1]
    print("DANO: ", damage)
    pk_bot.hp_loss(damage)
    print_delay(effect)
    if pk_bot.hp <= 0:
        print_delay(f"Foe {pk_bot.name} fainted!")



# damage = attacking(Litten, Rowlet)[0]
# effect = attacking(Litten, Rowlet)[1]
# print(Rowlet.barra())
# test(Litten, Rowlet, damage, effect)
# test(Litten, Rowlet, damage, effect)

