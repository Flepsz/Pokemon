import random


class Pokemon:
    """
    Essa classe cria um objeto de pokémon para o jogo. Ela inclui métodos para calcular o ataque, defesa, velocidade,
    vida e xp de um pokémon, além de métodos para calcular o dano causado, calcular a perda de hp, calcular a barra
    de saúde do pokémon e determinar se o pokémon foi morto ou não.
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
        """
        Calcula o stats de defesa do pokemon de acordo com sua defesa base e nível.
        :return: Status de defesa.
        """
        self.defense = self.defense + (((2 * self.defense + 15 + (self.lvl / 4)) * self.lvl) / 100) + 5
        return self.defense

    def calc_speed(self):
        """
        Calcula o stats de velocidade do pokemon de acordo com sua velocidade base e nível.
        :return: Status de velocidade.
        """
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

    def calc_xp(self, pk_bot):
        """
        Calcula o xp que o pokemon vai ganhar.
        :param pk_bot: Pokemon inimigo para pegar seu nível.
        :return: XP
        """
        xp = (1000 * pk_bot.lvl) / (7 * self.lvl)
        return xp

    def damage(self, pk_bot, mod_tipo):
        """
        Calcula se o usuário acertou, crítico ou errou.
        Calcula o dano que o pokemon do usuário dará de acordo com seu nível, ataque, defesa do oponente,
        poder da habilidade e modificador de tipo.

        1 = Acertou! | 2 = Crítico! | 3 = Errou!
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
        """
        Computa a perda de vida do pokemon.
        :param dmg: Dano recebido.
        :return: Vida com o dano recebido.
        """
        self.hp -= dmg
        return self.hp

    def bar_hp(self):
        """
        Mostra a vida em barras dinamicamente.
        """
        bar_full = int((self.hp / self.hpmax) * 20)
        bar_hp = (chr(0x2588) * bar_full)
        bar_msng = chr(0x2591) * (20 - bar_full)
        bar = bar_hp + bar_msng
        return bar


    @staticmethod
    def kill(pk_bot):
        """
        Verifica se o pokemon foi morto ou não.
        """
        if pk_bot.hp <= 0:
            return True
        else:
            return False

    @staticmethod
    def run():
        """
        Função que marca a probabilidade do jogador fugir da batalha.
        0 = Ficou | 1 = Fugiu
        :return:
        """
        chances = [0, 1]
        probs = [0.5, 0.5]

        run = random.choices(chances, weights=probs, k=1)[0]
        return run


class PokemonFire(Pokemon):
    """
    Classe dos pokemons de fogo.
    """
    def __init__(self, name, move, stats):
        super().__init__(name, move, stats)
        self.type = "Fire"
        self.effect = str

    def mod_stats(self, pk_bot):
        if pk_bot.type == "Grass":
            pk_bot.attack /= 1.5
            pk_bot.defense /= 1.5

        elif pk_bot.type == "Water":
            self.attack /= 1.5
            self.defense /= 1.5
        else:
            pass

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
            self.effect = 'Its super effective!'
            pk_bot.effect = 'Its not very effective...'
            return self.effect, pk_bot.effect

        else:
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

    def mod_stats(self, pk_bot):
        if pk_bot.type == "Water":
            pk_bot.attack /= 1.5
            pk_bot.defense /= 1.5

        elif pk_bot.type == "Fire":
            self.attack /= 1.5
            self.defense /= 1.5
        else:
            pass

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
            self.effect = 'Its super effective!'
            pk_bot.effect = 'Its not very effective...'
            return self.effect, pk_bot.effect

        else:
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

    def mod_stats(self, pk_bot):
        if pk_bot.type == "Fire":
            pk_bot.attack /= 1.5
            pk_bot.defense /= 1.5

        elif pk_bot.type == "Grass":
            self.attack /= 1.5
            self.defense /= 1.5
        else:
            pass

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
            self.effect = 'Its super effective!'
            pk_bot.effect = 'Its not very effective...'
            return self.effect, pk_bot.effect

        else:
            self.effect = 'Its not very effective...'
            pk_bot.effect = 'Its super effective!'
            return self.effect, pk_bot.effect


Litten = PokemonFire('Litten', {'Name': 'Ember', 'Power': 40}, {'LVL': 5, 'HPMAX': 45, 'HP': 45, 'AttackBase': 65, 'Attack': 65, 'Defense': 40, 'Speed': 70})
Rowlet = PokemonGrass('Rowlet', {'Name': 'Leafage', 'Power': 40}, {'LVL': 5, 'HPMAX': 68, 'HP': 68, 'AttackBase': 55, 'Attack': 55, 'Defense': 55, 'Speed': 42})
Popplio = PokemonWater('Popplio', {'Name': 'Water Gun', 'Power': 40}, {'LVL': 5, 'HPMAX': 50, 'HP': 50, 'AttackBase': 54, 'Attack': 54, 'Defense': 54, 'Speed': 40})

Littenbot = PokemonFire('Litten', {'Name': 'Ember', 'Power': 40}, {'LVL': 5, 'HPMAX': 45, 'HP': 45, 'AttackBase': 65, 'Attack': 65, 'Defense': 40, 'Speed': 70})
Rowletbot = PokemonGrass('Rowlet', {'Name': 'Leafage', 'Power': 40}, {'LVL': 5, 'HPMAX': 68, 'HP': 68, 'AttackBase': 55, 'Attack': 55, 'Defense': 55, 'Speed': 42})
Poppliobot = PokemonWater('Popplio', {'Name': 'Water Gun', 'Power': 40}, {'LVL': 5, 'HPMAX': 50, 'HP': 50, 'AttackBase': 54, 'Attack': 54, 'Defense': 54, 'Speed': 40})
