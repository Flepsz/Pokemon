import random


class Pokemon:
    """
    Classe principal da construção do pokemon.
    """
    def __init__(self, name, move, stats):
        self.name = name
        self.lvl = stats['LVL']
        self.hpmax = stats['HPMAX']
        self.hp = stats['HP']
        self.movname = move['Name']
        self.power = move['Power']
        self.atk_base = stats['AttackBase']
        self.attack = stats['Attack']
        self.defense = stats['Defense']
        self.speed = stats['Speed']

        self.calc_atk()
        self.calc_def()
        self.calc_speed()
        self.calc_hp()

    def show_stats(self):
        """
        Função para retornar todos os status do pokemon.
        :return: Status do pokemon.
        """
        return self.name, self.lvl, self.hp, self.movname, self.power, self.atk_base, self.attack, self.defense, self.speed

    def calc_atk(self):
        """
        Calcula o stats de ataque do pokemon de acordo com seu ataque base e nível.
        :return: Status ataque.
        """
        self.attack = self.atk_base + (((2 * self.atk_base + self.lvl / 4 + 15 / 4) * self.lvl) / 100 + 5)
        return self.attack

    def calc_def(self):
        self.defense = self.defense + (((2 * self.defense + 15 + (self.lvl / 4)) * self.lvl) / 100) + 5
        return self.defense

    def calc_speed(self):
        self.speed = self.speed + (((2 * self.speed + 15 + (self.lvl / 4)) * self.lvl) / 100) + 5
        return self.speed

    def calc_hp(self):
        """
        Calcula o stats de vida do pokemon de acordo com sua vida base e nível.
        :return: Status defesa.
        """
        self.hp = self.hp + (((2 * self.hp + 15 + (self.lvl / 4)) * self.lvl) / 100) + self.lvl + 10
        self.hpmax = self.hp
        return self.hp, self.hpmax

    def damage(self, pk_bot, mod_tipo):
        """
        Calcula se o usuário acertou, crítico ou errou.
        Calcula o dano que o pokemon do usuário dará de acordo com seu nível, ataque, defesa do oponente,
        poder da habilidade e modificador de tipo.
        1 = Acertou! | 2 = Crítico! | 3 = Errou!;
        :param pk_bot: Pokemon do bot.
        :param mod_tipo: Modificador de tipo.
        :return: Dano do pokemon e mensagem.
        """
        damage = ((2 * self.lvl + 10) / 100) * (self.attack / pk_bot.defense) * (self.power + 2)
        chances = [1, 2, 3]
        probs = [0.8, 0.1, 0.1]

        acertou = random.choices(chances, weights=probs, k=1)[0]
        if acertou == 1:
            msg = mod_tipo[0]
            return damage, msg
        elif acertou == 2:
            msg = 'A critical hit!'
            damage *= 2
            return damage, msg
        else:
            msg = 'The attack missed!'
            damage = 0
            return damage, msg

    def hp_loss(self, dmg):
        self.hp -= dmg
        return self.hp

    def show_health(self):
        dash_convert = int(self.hpmax / 20)
        current_dashes = int(self.hp / dash_convert)
        remaining_health = 20 - current_dashes

        health_display = '=' * current_dashes
        remaining_display = ' ' * remaining_health

        print("|" + health_display + remaining_display + '|')


class PokemonFire(Pokemon):
    """
    Classe dos pokemons de fogo.
    """
    def __init__(self, name, move, stats):
        super().__init__(name, move, stats)
        self.type = "Fire"
        self.effect = str

    def mod_tipo(self, pk_bot):
        """
        Função que determina o modificador de tipo, ou seja, a vantagem daquele pokemon contra algum elemento.
        :param pk_bot: Pokemon do bot
        :return: Modificador de tipo
        """
        if self.type == pk_bot.type:
            self.effect = 'Its not very effective...'
            pk_bot.effect = 'Its not very effective...'
            return self.effect, pk_bot.effect

        elif pk_bot.type == "Grass":
            pk_bot.attack /= 1.5
            pk_bot.defense /= 1.5
            self.effect = 'Its super effective!'
            pk_bot.effect = 'Its not very effective...'
            return self.effect, pk_bot.effect

        else:
            self.attack /= 1.5
            self.defense /= 1.5
            self.effect = 'Its not very effective...'
            pk_bot.effect = 'Its super effective!'
            return self.effect, pk_bot.effect


class PokemonGrass(Pokemon):
    """
    Classe dos pokemons de grama.
    """
    def __init__(self, name, move, stats):
        super().__init__(name, move, stats)
        self.type = "Grass"
        self.effect = str

    def mod_tipo(self, pk_bot):
        """
        Função que determina o modificador de tipo, ou seja, a vantagem daquele pokemon contra algum elemento.
        :param pk_bot: Pokemon do bot
        :return: Modificador de tipo
        """
        if self.type == pk_bot.type:
            self.effect = 'Its not very effective...'
            pk_bot.effect = 'Its not very effective...'
            return self.effect, pk_bot.effect

        elif pk_bot.type == "Water":
            pk_bot.attack /= 1.5
            pk_bot.defense /= 1.5
            self.effect = 'Its super effective!'
            pk_bot.effect = 'Its not very effective...'
            return self.effect, pk_bot.effect

        else:
            self.attack /= 1.5
            self.defense /= 1.5
            self.effect = 'Its not very effective...'
            pk_bot.effect = 'Its super effective!'
            return self.effect, pk_bot.effect


class PokemonWater(Pokemon):
    """
    Classe dos pokemons de água.
    """
    def __init__(self, name, move, stats):
        super().__init__(name, move, stats)
        self.type = "Water"
        self.effect = str

    def mod_tipo(self, pk_bot):
        """
        Função que determina o modificador de tipo, ou seja, a vantagem daquele pokemon contra algum elemento.
        :param pk_bot: Pokemon do bot
        :return: Modificador de tipo
        """
        if self.type == pk_bot.type:
            self.effect = 'Its not very effective...'
            pk_bot.effect = 'Its not very effective...'
            return self.effect, pk_bot.effect

        elif pk_bot.type == "Fire":
            pk_bot.attack /= 1.5
            pk_bot.defense /= 1.5
            self.effect = 'Its super effective!'
            pk_bot.effect = 'Its not very effective...'
            return self.effect, pk_bot.effect

        else:
            self.attack /= 1.5
            self.defense /= 1.5
            self.effect = 'Its not very effective...'
            pk_bot.effect = 'Its super effective!'
            return self.effect, pk_bot.effect


Litten = PokemonFire('Litten', {'Name': 'Ember', 'Power': 40}, {'LVL': 5, 'HPMAX': 45, 'HP': 45, 'AttackBase': 65, 'Attack': 65, 'Defense': 40, 'Speed': 70})
Rowlet = PokemonGrass('Rowlet', {'Name': 'Leafage', 'Power': 40}, {'LVL': 5, 'HPMAX': 68, 'HP': 68, 'AttackBase': 55, 'Attack': 55, 'Defense': 55, 'Speed': 42})
Popplio = PokemonWater('Popplio', {'Name': 'Water Gun', 'Power': 40}, {'LVL': 5, 'HPMAX': 50, 'HP': 50, 'AttackBase': 54, 'Attack': 54, 'Defense': 54, 'Speed': 40})

