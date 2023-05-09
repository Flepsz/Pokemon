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
