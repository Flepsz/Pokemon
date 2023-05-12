import time
import inquirer
from functions import clear, print_delay, hp_atk_taken, bot_poke, start_battle, wait, Color, show_health
from pokemons import Rowlet, Popplio, Litten


def start_game():
    clear()
    print_delay("{:^30}".format("POKEMON"))
    print_delay("Welcome to the POKEMON world!")
    print_delay(input("Press ENTER to continue!\n"))
    wait()
    clear()
    print_delay("Let's start!")
    time.sleep(1)
    clear()
    print_delay("What is your name?")
    myname = input("Name: ").title()
    print_delay(f"Your name is {myname}.")
    clear()
    print_delay("Let's choose your pokemon!\n")

    pokemonsl = inquirer.prompt(
        [inquirer.List('pokemon', message=f"Which pokemon do you want?", choices=[Litten.name, Rowlet.name, Popplio.name])])

    print_delay(f"The pokemon that you choose was {pokemonsl['pokemon']}!")
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
    rival = input("Name: ").title()
    print_delay(f"\nYour rival is {rival}")
    clear()
    print_delay("Now let's start the game!!")
    clear()
    print_delay(f"{rival}: Yo! {myname}!")
    clear()
    print_delay("You're still struggling along back here?")
    clear()
    print_delay("I'm doing great! I caught a bunch of strong and smart POKEMON!")
    clear()
    print_delay(f"Here, let me see what you caught, {myname}!")
    clear()
    print_delay("...")
    clear()

    lvlchange = inquirer.prompt(
        [inquirer.List('lvl', message=f"Before start the battle, do you want to choose the level of pokemons?",
                       choices=['Yes', 'No'])])
    if lvlchange['lvl'] == 'Yes':
        lvl = int(input(f"Type the level of your {poke.name}: "))
        poke.change_lvl(lvl)
        lvlbt = int(input(f"Now, type the level of enemy pokemon: "))
    else:
        lvlbt = 5

    clear()
    return poke, rival, myname, lvlbt


def fight(pokemon, pk_bot, btname, name, lvlbot):
    # print_delay(f"{btname} wants to fight!")
    # time.sleep(1)
    # clear()
    # print_delay(f"{btname} sent out {pk_bot.name}")
    # clear()
    # print_delay(f"Go! {pokemon.name}!")
    # clear()

    time.sleep(2)
    pk_bot.change_lvl(lvlbot)
    pokemon.mod_stats(pk_bot)

    while pokemon.hp > 0 and pk_bot.hp > 0:
        if start_battle(pokemon, pk_bot) == pokemon.name:
            show_health(pokemon, pk_bot)
            print()

            actiondo = inquirer.prompt(
                [inquirer.List('pokedo', message=f"What will {pokemon.name} do?", choices=['Fight', 'Run'])])

            clear()

            show_health(pokemon, pk_bot)

            if actiondo['pokedo'] == 'Fight':
                print()
                movedo = inquirer.prompt(
                    [inquirer.List('atkdo', message=f"Choose the move?", choices=[f'{pokemon.movname}', 'Back'])])
                clear()

                if movedo['atkdo'] == f'{pokemon.movname}':
                    print_delay(f"{pokemon.name} used {pokemon.movname}!")
                    clear()
                    hp_atk_taken(pokemon, pk_bot)
                    clear()

                    if pokemon.kill(pk_bot):
                        clear()
                        print_delay(f"{pokemon.name} gained {pokemon.calc_xp(pk_bot):.2f} EXP. Points!")
                        clear()
                        print_delay(f"{name} defeated {btname}!")
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
                show_health(pokemon, pk_bot)

                print_delay(f'{pk_bot.name} turns.')
                time.sleep(1)
                clear()
                print_delay(f"Enemy {pk_bot.name} used {pk_bot.movname}!")
                clear()
                hp_atk_taken(pk_bot, pokemon)
                clear()

                if pk_bot.kill(pokemon):
                    clear()
                    print_delay(f"{rivals}: LOSER!")
                    clear()
                    print_delay("...")
                    clear()
                    print_delay("You has been defeated!")
                    clear()
                    print_delay("Try again later...")
                    break
            else:
                if pokemon.run() == 0:
                    print_delay("Couldn't escape!\n")
                    clear()
                    continue
                else:
                    print_delay("Got away safely!")
                    clear()
                    break

        else:
            player = 2
            if player == 1:
                break
            else:
                show_health(pokemon, pk_bot)
                print()

                time.sleep(1)
                print_delay(f'{pk_bot.name} turns.')
                time.sleep(1)
                clear()
                print_delay(f"Enemy {pk_bot.name} used {pk_bot.movname}!")
                clear()
                hp_atk_taken(pk_bot, pokemon)
                clear()

                if pk_bot.kill(pokemon):
                    clear()
                    print_delay(f"{rivals}: LOSER!")
                    clear()
                    print_delay("...")
                    clear()
                    print_delay("You has been defeated!")
                    clear()
                    print_delay("Try again later...")
                    break
                else:
                    player = 2

            while player == 2:
                show_health(pokemon, pk_bot)
                print()

                actiondo = inquirer.prompt(
                    [inquirer.List('pokedo', message=f"What will {pokemon.name} do?", choices=['Fight', 'Run'])])

                clear()

                show_health(pokemon, pk_bot)

                if actiondo['pokedo'] == 'Fight':
                    print()
                    movedo = inquirer.prompt(
                        [inquirer.List('atkdo', message=f"Choose the move?", choices=[f'{pokemon.movname}', 'Back'])])
                    clear()

                    if movedo['atkdo'] == f'{pokemon.movname}':
                        print_delay(f"{pokemon.name} used {pokemon.movname}!")
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
                            player = 3
                    else:
                        continue

                else:
                    if pokemon.run() == 0:
                        print_delay("Couldn't escape!\n")
                        clear()
                        continue
                    else:
                        print_delay("Got away safely!")
                        clear()
                        player = 1
                        return player


pokem, rivals, mynames, lvlbot = start_game()
# pokem = Litten
# rivals = 'Beck'
# mynames = 'Raphinha'
# lvlbot = 20

fight(pokem, bot_poke(), rivals, mynames, lvlbot)
