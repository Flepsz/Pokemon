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
    """
    Função que faz o print aparecer pausadamente.
    """
    print()
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)
    print()
    time.sleep(1)


def print_delay_clr(s):
    """
    Função que faz o print aparecer pausadamente, mas limpando o terminal ao final do print.
    """
    print()
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)
    print()
    time.sleep(1)
    clear()


def wait():
    m.getch()


def clear():
    """
    Limpa o terminal.
    """
    os.system('cls')


def mod_func(pokemon, pk_bot):
    """
    Retorna os textos de efeitos dos pokemons de acordo com o tipo deles.
    """
    return pokemon.mod_tipo(pk_bot)


def attacking(pokemon, pk_bot):
    """
    Retorna o dano do pokemon com os textos de efeito.
    """
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
    if pokemon.speed > pk_bot.speed:
        return pokemon.name
    else:
        return pk_bot.name


def bot_poke():
    """
    Função que escolhe aleatóriamente o pokemon do bot.
    """
    pokes = [Littenbot, Rowletbot, Poppliobot]
    poke_bot = random.choice(pokes)
    return poke_bot


def hp_atk_taken(pokemon, pk_bot):
    """
    Essa função diminui o HP do Pokémon inimigo. Ela recebe como parâmetros o Pokémon que está sendo atacado e o
    Pokémon que está atacando. A função, então, calcula o dano recebido usando a função de ataque e subtrai do HP do
    Pokémon atacado. Em seguida, imprime o efeito do ataque e, se o HP do Pokémon atacado atingir zero ou menos,
    imprime a mensagem "Foe {nome_do_pokemon} fainted!"
    :param pokemon: Pokemon que atacou.
    :param pk_bot: Pokemon que recebeu o dano.
    """
    dmgf = attacking(pokemon, pk_bot)
    damage = dmgf[0]
    effect = dmgf[1]
    pk_bot.hp_loss(damage)
    print_delay(effect)
    if pk_bot.hp <= 0:
        print_delay(f"Foe {pk_bot.name} fainted!")


def show_health(pokemon, pk_bot):
    """
    Função que apenas printa a vida atual dos pokemons.
    """
    print(
        f'\n\t{Color.PURPLE}{pokemon.name}{Color.R}\tLVL. {pokemon.lvl}\n\tHP {Color.GREEN}{pokemon.bar_hp()}{Color.R}\n')
    print(f'\t{pk_bot.name}\tLVL. {pk_bot.lvl}\n\tHP {Color.GREEN}{pk_bot.bar_hp()}{Color.R}')
