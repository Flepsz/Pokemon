import time
import random
import inquirer
from functions import start_battle, print_delay, attacking
from pokemons import PokemonWater, PokemonGrass, PokemonFire, Pokemon, Rowlet, Popplio, Litten


def start_game():
    print("{:^30}".format("POKEMON BATTLE"))


def choose_poke():
    pass


def fight(pokemon, pk_bot):
    print(f"""
    ================== BATTLE ==================
      {pokemon.name}                     {pk_bot.name}
      LVL. {pokemon.lvl}             VS         LVL. {pk_bot.lvl}
      TYPE: {pokemon.type}                    TYPE: {pk_bot.type}
    """)

    time.sleep(2)

    while pokemon.hp > 0 and pk_bot.hp > 0:
        start_battle(pokemon, pk_bot)
        if start_battle == pokemon.name:
            print(f'{pokemon.name}\t\tHP {pokemon.show_health()}')
            print(f'{pk_bot.name}\t\tHP {pk_bot.name}')

            import inquirer
            questions = [
                inquirer.List('pokedo',
                              message=f"\nWhat will {pokemon.name} do?",
                              choices=['Fight', 'Run'],
                              ),
            ]
            actiondo = inquirer.prompt(questions)
            if actiondo == 'Fight':
                questions = [
                    inquirer.List('atkdo',
                                  message=f"\nChoose the move?",
                                  choices=[f'{pokemon.movname}', 'Back'],
                                  ),
                ]
                movedo = inquirer.prompt(questions)
                if movedo == f'{pokemon.movname}':
                    damage = attacking(pokemon, pk_bot)[0]
                    effect = attacking(pokemon, pk_bot)[1]

                    pk_bot.hp_loss(damage[0])
                    print_delay(damage[1])
                    print_delay(f"{pk_bot.name} perdeu {damage:.2f} de vida")
                else:
                    break

                print_delay(f'{pk_bot.name} turns.')
                damage1 = attacking(pk_bot, pokemon)[0]
                effect1 = attacking(pk_bot, pokemon)[1]
                
                pokemon.hp_loss(damage1)
                print_delay(damage[1])
                print_delay(f"{pokemon.name} perdeu {damage:.2f} de vida")
                

            else:
                break

        else:
            print(f'{pokemon.name}\t\tHP {pokemon.show_health()}')
            print(f'{pk_bot.name}\t\tHP {pk_bot.name}')

# damage = Litten.damage(Rowlet, Litten.mod_tipo(Rowlet))
# Rowlet.hp_loss(damage[0])
# print_delay(damage[1])
# print_delay(f"Rowlet perdeu {damage[0]:.2f} de vida")
# print(Rowlet.show_health())
start_game()
