import sys
import time
import random
from pokemons import PokemonWater, PokemonGrass, PokemonFire, Pokemon, Rowlet, Popplio, Litten


# Calcs = {
#     'EV': 5,
#     'IV': 15,
#     'Damage': (((2 * self.lv + 10) / 100) * (attack / bot.defense) * (self.power + 2) x mod_tipo,
#     'Attack': self.atk_base + ((((2 * self.atk_base + ev / 4 + iv / 4) * self.lvl) / 100 + 5) * mod_tipo)
# }

def print_delay(chr):
    for wrt in chr:
        sys.stdout.write(chr)
        sys.stdout.flush()
        time.sleep(0.05)


def startbttl(pokemon, pk_bot):
    pokes = [pokemon.name, pk_bot.name]
    if pokemon.speed == pk_bot.speed:
        return random.choice(pokes)
    elif pokemon.speed > pk_bot.speed:
        return pokemon.name
    else:
        return pk_bot.name


def acerto():
    # 1 = Acertou! | 2 = Crítico! | 3 = Errou!
    chances = [1, 2, 3]
    probs = [0.8, 0.1, 0.1]

    return random.choices(chances, weights=probs, k=1)[0]


def fight(pokemon, pk_bot):
    print(f"""
    ================== BATTLE ==================
      {pokemon.name}                     {pk_bot.name}
      LVL. {pokemon.lvl}             VS         LVL. {pk_bot.lvl}
      TYPE: {pokemon.type}                    TYPE: {pk_bot.type}
    """)

    time.sleep(2)

    while pokemon.hp > 0 and pk_bot > 0:
        pass


