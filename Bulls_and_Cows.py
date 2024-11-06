"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie - hra Bulls and Cows
author: Přemysl Pleva
email: premyslpleva75@gmail.com
discord: premeq#5714
"""

import random as r
from datetime import datetime


def bull_number():
    """
    This function is generating a random 4-digit number
    """

    num_list = []
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    for i in range(4):
        a = r.choice(digits)
        num_list += a
        digits.remove(a)
    while num_list[0] == "0":  # checking the first digit - it cannot be a zero
        r.shuffle(num_list)

    num = ''.join(num_list)
    return num


def total_time(a, z):
    """
    This function calculates the total time from a to z
    :param a: start
    :param z: end
    :return: total time from a to z
    """
    tot_sec = (z - a).total_seconds()
    if 119 < tot_sec < 180:
        m = int(tot_sec // 60)
        s = int(tot_sec % 60)
        result = f"It took you {m} minutes and {s} seconds :)"
    elif tot_sec >= 180:
        result = f"You are a lame and your game won't make it to the records..."
    else:
        result = f"It took you {int(tot_sec)} seconds only!"
    return result


def count_bulls_cows(tip):
    number_of_bulls = 0
    number_of_cows = 0
    for i in range(4):
        if tip[i] == generated_num[i]:
            number_of_bulls += 1
        elif tip[i] in generated_num:
            number_of_cows += 1
    return number_of_bulls, number_of_cows


def game_conditions_ok(user_input: str) -> bool:
    """
    This function checks the game rules for player's input
    :param user_input: Player's input, a number
    :return: True or False
    """
    if not user_input.isnumeric():
        print("Your input contains non-digit symbols...")
        return False
    elif len(user_input) != 4:
        print("Your input should be a 4-digit number...")
        return False
    elif len(set(user_input)) != 4:
        print("Digits do not repeat...")
        return False
    return True


def wrong_guess():
    """
    This function prints the count of Bulls and Cows
    :return: A string of counted Bulls and Cows
    :example: 1 Bull, 0 Cows
    """

    the_count = count_bulls_cows(x)
    b = "Bull" if the_count[0] == 1 else "Bulls"
    c = "Cow" if the_count[1] == 1 else "Cows"
    result = f"{the_count[0]} {b}, {the_count[1]} {c}"
    return result


def end_game_check():
    '''
    This function asks the player if they want to play another game with a newly generated number
    :return: "y" for yes or "n" for no
    '''
    while True:  # Loop for asking if the player wants to play again
        new_game = input("Would you like to play again, cowboy? (y/n):")
        if new_game == "y":
            print("*" * 50)
            print("That's my boi! Let's GO!")
            print("*" * 50)
            break
        elif new_game == "n":
            print("*" * 50)
            print("Thanks for playing, see you again soon.")
            break
        else:
            continue

    return new_game


# THE GAME
#
#
print(
    "Hi there!",
    "-" * 50,
    "I've generated a random 4 digit number for you.",
    "It has unique digits.",
    "Let's play Bulls and Cows game.",
    "-" * 50,
    "The number has been generated!",
    "-" * 50,
    sep="\n"
)


while True:  # Loop for the entire game

    generated_num = bull_number()  # The random number that is to be guessed
    # print(generated_num)

    guesses = 0  # trial & error counter
    # again = str()  # An empty string - used later to check in the player wants a new game

    start = datetime.now()  # timer - start

    while True:  # Loop where the player is guessing the number

        x = input("Your guess: ")  # player's guess
        guesses += 1

        if game_conditions_ok(x) is False:  # Verifying validity of player's input
            continue

        bulls, cows = count_bulls_cows(x)

        if bulls < 4:  # and game_conditions_ok(x) is True:  # Wrong guess, less than 4 Bulls
            print(wrong_guess())
        else:  # Correct guess, 4 Bulls
            end = datetime.now()  # timer - end
            print("*" * 50)
            if guesses == 1:
                print("Wow! You must be a fortuneteller.")
            else:
                print("Correct!! Amazing game, congratulations :)", f"You got it in {guesses} turns!", sep="\n")
            total_time(start, end)
            print("*" * 50)
            break

    again = end_game_check()
    if again == "n":
        break



