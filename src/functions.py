import random
import sys
import time
import os
import msvcrt as m
from pokemons import Rowletbot, Poppliobot, Littenbot


class Color:
    """
    Cores ASCII
    """
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    R = '\33[m'


def print_delay(s):
    print()
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
    print()
    time.sleep(1)


def wait():
    m.getch()


def clear():
    os.system('cls')


def mod_func(pokemon, pk_bot):
    return pokemon.mod_tipo(pk_bot)


def attacking(pokemon, pk_bot):
    return pokemon.damage(pk_bot, mod_func(pokemon, pk_bot))


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


def bot_poke():
    pokes = [Littenbot, Rowletbot, Poppliobot]
    poke_bot = random.choice(pokes)
    return poke_bot


def hp_atk_taken(pokemon, pk_bot):
    dmgf = attacking(pokemon, pk_bot)
    damage = dmgf[0]
    effect = dmgf[1]
    pk_bot.hp_loss(damage)
    print_delay(effect)
    if pk_bot.hp <= 0:
        print_delay(f"Foe {pk_bot.name} fainted!")

