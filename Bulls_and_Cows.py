"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Přemysl Pleva
email: premyslpleva75@gmail.com
discord: premeq#5714
"""

import random as r
from datetime import datetime
import math

print(
    "Hi there!",
    "-" * 50,
    "I've generated a random 4 digit number for you.",
    "Let's play a bulls and cows game.",
    "-" * 50,
    "Enter a number:",
    "-" * 50,
    sep="\n"
)


# Následuje uživatelská funkce <bull_number> na generování náhodného 4-místného čísla bez opakování číslic
#
def bull_number():
    """
    Funkce generuje náhodné 4-ciferné číslo, v němž se neopakuje žádná číslice
    """
    # číslo pvní generuju jako string, a až na závěr jej převedu do integer
    #
    num_str = ""
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    #
    # Ve smyčve vždy vyberu jeden prvek z <digits> a připojím jej na konec <num_str>
    # Následně vybraný prvek odstraním z množiny <digits> (aby nedošlo k opakování číslic)
    #
    for i in range(5):
        #
        #
        a = r.choice(digits)
        #
        # Ověřím, zda není první číslice "nula" - proto se jedná o 5-ti kolečkový cyklus
        #
        if a == "0" and len(num_str) == 0:
            continue
        #
        # Připojím vybranou číslici ke stringu
        #
        num_str += a
        #
        # Odstraním vybranou číslici z <digits>
        #
        digits.remove(a)
        #
        # Ověřím délku doteď vytvořeného čísla
        #
        if len(num_str) == 4:
            break
    #
    # Převedu vytvořené číslo na integer
    #
    num = int(num_str)
    return num


# Následuje uživatelská funkce <total_time>, která počítá, jak dlouho hadač hádal
#
def total_time(a, z):
    tot_sec = (z - a).total_seconds()
    if 119 < tot_sec < 180:
        m = math.floor(tot_sec / 60)
        s = math.floor((tot_sec % 60) * 60)
        a = f"It took you {m} minutes and {s} seconds :)"
    elif tot_sec >= 180:
        a = f"You are a lame and your game won't make it to the records..."
    else:
        a = f" It took you {math.floor(tot_sec)} seconds only!"
    return print(a)


def count_bulls_cows(tip):
    bulls = 0
    cows = 0
    for i in range(4):
        if tip[i] == generated_num[i]:
            bulls += 1
        elif tip[i] in generated_num:
            cows += 1
    return bulls, cows

# THE GAME
#
#
new_game = True
#
while new_game:
    #
    # generátor čísla, kt se má uhádnout
    generated_num = str(bull_number())
    # print(generated_num)
    #
    # počitadlo pokusů
    i = 0
    mistakes = True
    #
    # stopky - start
    start = datetime.now()
    #
    while mistakes:
        #
        # uživatelův tip
        #
        x = input()
        #
        # Kontrola podmínek hry
        #
        if not x.isnumeric():
            print("Zadal jsi nepovolené znaky! Znovu...")
            continue
        elif len(x) > 4:
            print("Zadal jsi příliš dlouhé číslo! Znovu...")
            continue
        elif len(x) < 4:
            print("Zadal jsi příliš krátké číslo! Znovu...")
            continue
        elif len(set(x)) != 4:
            print("Čislice se nesmí opakovat! Znovu...")
            continue
        else:
            #
            # případ, kdy uživatel úhádne správné číslo
            #
            if count_bulls_cows(x)[0] == 4:
                i += 1
                #
                # stopky - konec
                end = datetime.now()
                print("*" * 50)
                print("Correct!! Amazing game, congratulations :)", f"You got it in {i} turns!", sep="\n")
                total_time(start, end)
                print("*" * 50)
                #
                # následuje větvení, zda-li chce uživatel hrát znovu
                while True:
                    again = input("Would you like to play again, cowboy? (y/n):")
                    if again not in ("y", "n"):
                        continue
                    elif again == "n":
                        mistakes = False
                        new_game = False
                        print("*" * 50)
                        print("Thanks for playing, see you again soon.")
                        break
                    elif again == "y":
                        mistakes = False
                        print("*" * 50)
                        print("That's my boi! Let's GO!")
                        print("*" * 50)
                        break
            #
            #
            # špatný tip, pouze 1x bull a 1x cow
            elif count_bulls_cows(x)[0] == 1 and count_bulls_cows(x)[1] == 1:
                i += 1
                print(f"{count_bulls_cows(x)[0]} Bull, {count_bulls_cows(x)[1]} Cow")
                print("-" * 50)
                continue
            #
            # špatný tip, pouze 1x bull
            elif count_bulls_cows(x)[0] == 1 and count_bulls_cows(x)[0] != 1:
                i += 1
                print(f"{count_bulls_cows(x)[0]} Bull, {count_bulls_cows(x)[1]} Cows")
                print("-" * 50)
                continue
            #
            # špatný tip, pouze 1x cow
            elif count_bulls_cows(x)[0] != 1 and count_bulls_cows(x)[1] == 1:
                i += 1
                print(f"{count_bulls_cows(x)[0]} Bulls, {count_bulls_cows(x)[1]} Cow")
                print("-" * 50)
                continue
            #
            # špatný tip, více bulls a cows
            else:
                i += 1
                print(f"{count_bulls_cows(x)[0]} Bulls, {count_bulls_cows(x)[1]} Cows")
                print("-" * 50)
                continue

