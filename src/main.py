import time
import inquirer
from functions import clear, print_delay, hp_atk_taken, bot_poke, start_battle, wait, Color, show_health, print_delay_clr
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
    player_name = input("Name: ").title()
    print_delay_clr(f"Your name is {player_name}.")
    print_delay("Let's choose your pokemon!\n")
    pokemons_list = [Litten.name, Rowlet.name, Popplio.name]
    pokemons_choice = inquirer.prompt([inquirer.List('pokemon', message=f"Which pokemon do you want?", choices=pokemons_list)])
    pokemon = get_pokemon(pokemons_choice['pokemon'])
    print_delay(f"The pokemon that you choose was {pokemon.name}!")
    print_delay_clr("Nice choice!")
    print_delay_clr("Now you need to say the name of your rival")
    print_delay("What's the name of your rival?")
    rival_name = input("Name: ").title()
    print_delay_clr(f"\nYour rival is {rival_name}")
    print_delay_clr("Now let's start the game!!")
    print_delay_clr(f"{rival_name}: Yo! {player_name}!")
    print_delay_clr("You're still struggling along back here?")
    print_delay_clr("I'm doing great! I caught a bunch of strong and smart POKEMON!")
    print_delay_clr(f"Here, let me see what you caught, {player_name}!")
    print_delay_clr("...")
    lvl_change = inquirer.prompt([inquirer.List('lvl', message=f"Before start the battle, do you want to choose the level of pokemons?", choices=['Yes', 'No'])])

    if lvl_change['lvl'] == 'Yes':
        pokemon_level = int(input(f"Type the level of your {pokemon.name}: "))
        pokemon.change_lvl(pokemon_level)
        enemy_level = int(input(f"Now, type the level of enemy pokemon: "))
    else:
        enemy_level = 5
    clear()

    return pokemon, rival_name, player_name, enemy_level


def get_pokemon(pokemon_name):
    if pokemon_name == Litten.name:
        return Litten
    elif pokemon_name == Rowlet.name:
        return Rowlet
    else:
        return Popplio


def fight(pokemon, pk_bot, btname, name, lvlbot):
    print_delay(f"{btname} wants to fight!")
    time.sleep(1)
    clear()
    print_delay(f"{btname} sent out {pk_bot.name}")
    clear()
    print_delay(f"Go! {pokemon.name}!")
    clear()

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
# lvlbot = 60

fight(pokem, bot_poke(), rivals, mynames, lvlbot)
