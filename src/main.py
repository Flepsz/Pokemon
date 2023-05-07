import sys
import time
import random


# Calcs = {
#     'EV': 5,
#     'IV': 15,
#     'Damage': (((2 * self.lv + 10) / 100) * (attack / bot.defense) * (self.power + 2) x mod_tipo,
#     'Attack': self.atk_base + ((((2 * self.atk_base + ev / 4 + iv / 4) * self.lvl) / 100 + 5) * mod_tipo)
# }

Pokemons = {
    'Litten': {
        'lvl': 5,
        'hp': 45,
        'type': 'Fire',
        'move': {'Ember', 40},
        'atk_base': 65,
        'Defense': 40,
        'Agility': 70,
    },

    'Rowlet': {
        'lvl': 5,
        'hp': 68,
        'type': 'Grass',
        'move': {'Leafage', 40},
        'atk_base': 55,
        'Defense': 55,
        'Agility': 42,
    },

    'Popplio': {
        'lvl': 5,
        'hp': 50,
        'type': 'Water',
        'move': {'Water Gun', 40},
        'atk_base': 54,
        'Defense': 54,
        'Agility': 40,
    }
}


def print_delay(chr):
    for wrt in chr:
        sys.stdout.write(chr)
        sys.stdout.flush()
        time.sleep(0.05)


class Pokemon:
    def __init__(self, name, lvl, hp, type, move, atk_base, stats):
        self.name = name
        self.lvl = lvl
        self.hp = hp
        self.type = type
        self.move = move
        self.power = move['Power']
        self.atk_base = atk_base
        self.attack = stats['Attack']
        self.defense = stats['Defense']
        self.agility = stats['Agility']

    def fight(self, pk_bot):
        print(f"""
        ================== BATTLE ==================
          {self.name}                     {pk_bot.name}
          LVL. {self.lvl}             VS         LVL. {pk_bot.lvl}
          TYPE: {self.type}                    TYPE: {pk_bot.type}
        """)

        time.sleep(2)

        types = ['Fire', 'Grass', 'Water']
        for x, y in enumerate(types):
            if self.type == y:
                if pk_bot.type == y:
                    pk_bot_atk = 'Its not very effective...'
                    self_atk = 'Its not very effective...'

                elif pk_bot.type == types[(x + 1) % 3]:
                    pk_bot.attack *= 2
                    pk_bot.defense *= 2
                    self.attack /= 2
                    self.defense /= 2
                    pk_bot_atk = 'Its super effective!'
                    self_atk = 'Its not very effective...'

                elif pk_bot.type == types[(x + 2) % 3]:
                    pk_bot.attack /= 2
                    pk_bot.defense /= 2
                    self.attack *= 2
                    self.defense *= 2
                    self_atk = 'Its super effective!'
                    pk_bot_atk = 'Its not very effective...'

        while self.hp > 0 and pk_bot > 0:

