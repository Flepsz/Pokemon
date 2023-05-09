class Pokemon:
    def __init__(self, name, move, stats):
        self.name = name
        self.lvl = stats['LVL']
        self.hp = stats['HP']
        self.movname = move['Name']
        self.power = move['Power']
        self.atk_base = stats['AttackBase']
        self.attack = stats['Attack']
        self.defense = stats['Defense']
        self.speed = stats['Speed']

    def show_stats(self):
        return self.name, self.lvl, self.hp, self.movname, self.power, self.atk_base, self.attack, self.defense, self.speed

    def calc_atk(self):
        self.attack = self.atk_base + (((2 * self.atk_base + self.lvl / 4 + 15 / 4) * self.lvl) / 100 + 5)
        return self.attack

    def calc_dmg(self, pk_bot, mod_tipo):
        damage = (((2 * self.lvl + 10) / 100) * (self.attack / pk_bot.defense) * (self.power + 2) * mod_tipo)
        return damage


class PokemonFire(Pokemon):
    def __init__(self, name, move, stats):
        super().__init__(name, move, stats)
        self.type = "Fire"

    def mod_tipo(self, pk_bot):
        if self.type == pk_bot.type:
            self_atk = 'Its not very effective...'
            pk_bot_atk = 'Its not very effective...'

        elif pk_bot == "Grass":
            self.attack *= 2
            self.defense *= 2
            pk_bot.attack /= 2
            pk_bot.defense /= 2
            self_atk = 'Its super effective!'
            pk_bot_atk = 'Its not very effective...'

        elif pk_bot == "Water":
            self.attack /= 2
            self.defense /= 2
            pk_bot.attack *= 2
            pk_bot.defense *= 2
            self_atk = 'Its not very effective...'
            pk_bot_atk = 'Its super effective!'


class PokemonGrass(Pokemon):
    def __init__(self, name, move, stats):
        super().__init__(name, move, stats)
        self.type = "Grass"

    def mod_tipo(self, pk_bot):
        if self.type == pk_bot.type:
            self_atk = 'Its not very effective...'
            pk_bot_atk = 'Its not very effective...'

        elif pk_bot == "Water":
            self.attack *= 2
            self.defense *= 2
            pk_bot.attack /= 2
            pk_bot.defense /= 2
            self_atk = 'Its super effective!'
            pk_bot_atk = 'Its not very effective...'

        elif pk_bot == "Fire":
            self.attack /= 2
            self.defense /= 2
            pk_bot.attack *= 2
            pk_bot.defense *= 2
            self_atk = 'Its not very effective...'
            pk_bot_atk = 'Its super effective!'


class PokemonWater(Pokemon):
    def __init__(self, name, move, stats):
        super().__init__(name, move, stats)
        self.type = "Water"

    def mod_tipo(self, pk_bot):
        if self.type == pk_bot.type:
            self_atk = 'Its not very effective...'
            pk_bot_atk = 'Its not very effective...'

        elif pk_bot == "Fire":
            self.attack *= 2
            self.defense *= 2
            pk_bot.attack /= 2
            pk_bot.defense /= 2
            self_atk = 'Its super effective!'
            pk_bot_atk = 'Its not very effective...'

        elif pk_bot == "Grass":
            self.attack /= 2
            self.defense /= 2
            pk_bot.attack *= 2
            pk_bot.defense *= 2
            self_atk = 'Its not very effective...'
            pk_bot_atk = 'Its super effective!'


Litten = PokemonFire('Litten', {'Name': 'Ember', 'Power': 40}, {'LVL': 5, 'HP': 45, 'AttackBase': 65, 'Attack': 65, 'Defense': 40, 'Speed': 70})
Rowlet = PokemonGrass('Rowlet', {'Name': 'Leafage', 'Power': 40}, {'LVL': 5, 'HP': 68, 'AttackBase': 55, 'Attack': 55, 'Defense': 55, 'Speed': 42})
Popplio = PokemonWater('Popplio', {'Name': 'Water Gun', 'Power': 40}, {'LVL': 5, 'HP': 50, 'AttackBase': 54, 'Attack': 54, 'Defense': 54, 'Speed': 40})
Litten.calc_atk()
Rowlet.calc_atk()
Popplio.calc_atk()
