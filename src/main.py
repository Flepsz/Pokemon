import time
import random
import inquirer
from functions import clear, start_battle, print_delay, attacking, hp_atk_taken
from pokemons import PokemonWater, PokemonGrass, PokemonFire, Pokemon, Rowlet, Popplio, Litten


def start_game():
    print("{:^30}".format("POKEMON"))
    print_delay("Welcome to the POKEMON world!")
    clear()
    print_delay("Let's start!")
    time.sleep(1)
    clear()
    print_delay("What is your name?")
    myname = input("Name: ")
    print_delay("Let's choose your pokemon!")
    clear()

    questions = [
        inquirer.List('pokemon',
                      message=f"Which pokemon do you want?",
                      choices=[Litten.name, Rowlet.name, Popplio.name],
                      ),
    ]
    pokemonsl = inquirer.prompt(questions)
    print_delay(f"The pokemon that you choose was {pokemonsl['pokemon']}!")
    clear()
    print_delay("Nice choice!")
    if pokemonsl['pokemon'] == Litten.name:
        poke = Litten
    elif pokemonsl['pokemon'] == Rowlet.name:
        poke = Rowlet
    else:
        poke = Popplio
    clear()
    print_delay("Now you need to say the name of your rival")
    clear()
    print_delay("What's the name of your rival?")
    rival = input("Name: ")
    print_delay(f"\n Your rival is {rival}")
    clear()
    print_delay("Now let's start the game!!")
    clear()
    print_delay(f"{rival}: Yo! {myname}!")
    clear()
    print_delay("You're still struggling along back here?")
    clear()
    print_delay("I'm doing great! I caught a bunch of strong and smart POKEMON!")
    clear()
    print_delay(f"Here, let me see what you caught, {myname}")
    clear()
    print_delay("...")
    clear()
    print_delay("*Battle starts...*")
    clear()
    return rival, poke


def choose_poke():
    pass


def fight(pokemon, pk_bot, btname, name):
    # print_delay(f"{btname[0]} wants to fight!")
    # time.sleep(1)
    # clear()
    # print_delay(f"{btname[0]} sent out {pk_bot.name}")
    # clear()
    # print_delay(f"Go! {pokemon.name}!")
    # clear()


#     print(f"""
# <-{"BATTLE":^50}->
# {pokemon.name}\t\t\t\t\t{pk_bot.name}
# LVL. {pokemon.lvl}{'VS':^33}LVL. {pk_bot.lvl}
# TYPE: {pokemon.type}\t\t\t\tTYPE: {pk_bot.type}
# <-{"|-----|":^50}->
# """)

    # time.sleep(2)

    while pokemon.hp > 0 and pk_bot.hp > 0:
        start_battle = 'f'
        if start_battle == 'f':
            print(f'\n\t{pokemon.name}\tLVL. {pokemon.lvl}\n\tHP {pokemon.bar_hp()}\n')
            print(f'\t{pk_bot.name}\tLVL. {pokemon.lvl}\n\tHP {pk_bot.bar_hp()}\n')
            questions = [
                inquirer.List('pokedo',
                              message=f"What will {pokemon.name} do?",
                              choices=['Fight', 'Run'],
                              ),
            ]
            actiondo = inquirer.prompt(questions)
            clear()
            print(f'\n\t{pokemon.name}\tLVL. {pokemon.lvl}\n\tHP {pokemon.bar_hp()}\n')
            print(f'\t{pk_bot.name}\tLVL. {pokemon.lvl}\n\tHP {pk_bot.bar_hp()}')
            if actiondo['pokedo'] == 'Fight':
                print()
                questions = [
                    inquirer.List('atkdo',
                                  message=f"Choose the move?",
                                  choices=[f'{pokemon.movname}', 'Back'],
                                  ),
                ]
                movedo = inquirer.prompt(questions)
                clear()

                if movedo['atkdo'] == f'{pokemon.movname}':
                    print_delay(f"{pokemon.name} used {pokemon.movname}")
                    clear()
                    hp_atk_taken(pokemon, pk_bot)
                    clear()

                    if pokemon.kill(pk_bot):
                        clear()
                        print_delay(f"{pokemon.name} gained {pokemon.calc_xp(pk_bot):.2f} EXP. Points!")
                        clear()
                        print_delay(f"{name} defeated {btname}")
                        clear()
                        print_delay(f"{btname}: Humph!")
                        clear()
                        print_delay("At least you're raising your POKEMON!")
                        clear()
                        print_delay("Congratulations, you win!")
                        break
                else:
                    continue
                clear()
                print_delay(f'{pk_bot.name} turns.')
                time.sleep(1)
                clear()
                print_delay(f"Enemy {pk_bot.name} used {pokemon.movname}")
                clear()
                hp_atk_taken(pk_bot, pokemon)
                clear()

            else:
                if pokemon.run() == 0:
                    print_delay("Couldn't escape!\n")
                    continue
                else:
                    print_delay("Got away safely!")
                    break

        else:
            print(f'\n\t{pokemon.name}\tLVL. {pokemon.lvl}\n\tHP {pokemon.bar_hp()}\n')
            print(f'\t{pk_bot.name}\tLVL. {pokemon.lvl}\n\tHP {pk_bot.bar_hp()}\n')
            time.sleep(1)
            print_delay(f'{pk_bot.name} turns.')
            time.sleep(1)
            clear()
            print_delay(f"Enemy {pk_bot.name} used {pokemon.movname}")
            clear()
            hp_atk_taken(pk_bot, pokemon)
            clear()

            print(f'\n\t{pokemon.name}\tLVL. {pokemon.lvl}\n\tHP {pokemon.bar_hp()}\n')
            print(f'\t{pk_bot.name}\tLVL. {pokemon.lvl}\n\tHP {pk_bot.bar_hp()}\n')
            questions = [
                inquirer.List('pokedo',
                              message=f"What will {pokemon.name} do?",
                              choices=['Fight', 'Run'],
                              ),
            ]
            actiondo = inquirer.prompt(questions)
            clear()
            print(f'\n\t{pokemon.name}\tLVL. {pokemon.lvl}\n\tHP {pokemon.bar_hp()}\n')
            print(f'\t{pk_bot.name}\tLVL. {pokemon.lvl}\n\tHP {pk_bot.bar_hp()}')
            if actiondo['pokedo'] == 'Fight':
                print()
                questions = [
                    inquirer.List('atkdo',
                                  message=f"Choose the move?",
                                  choices=[f'{pokemon.movname}', 'Back'],
                                  ),
                ]
                movedo = inquirer.prompt(questions)
                clear()

                if movedo['atkdo'] == f'{pokemon.movname}':
                    print_delay(f"{pokemon.name} used {pokemon.movname}")
                    clear()
                    hp_atk_taken(pokemon, pk_bot)
                    clear()

                    if pokemon.kill(pk_bot):
                        clear()
                        print_delay(f"{pokemon.name} gained {pokemon.calc_xp(pk_bot):.2f} EXP. Points!")
                        clear()
                        print_delay(f"{name} defeated {btname}")
                        clear()
                        print_delay(f"{btname}: Humph!")
                        clear()
                        print_delay("At least you're raising your POKEMON!")
                        clear()
                        print_delay("Congratulations, you win!")
                        break
                else:
                    continue
            else:
                if pokemon.run() == 0:
                    print_delay("Couldn't escape!\n")
                    continue
                else:
                    print_delay("Got away safely!")
                    break

# damage = Litten.damage(Rowlet, Litten.mod_tipo(Rowlet))
# Rowlet.hp_loss(damage[0])
# print_delay(damage[1])
# print_delay(f"Rowlet perdeu {damage[0]:.2f} de vida")
# print(Rowlet.show_health())


# rival = start_game()

rival = "Pedro"
name = "Felipe"
fight(Litten, Rowlet, rival, name)
