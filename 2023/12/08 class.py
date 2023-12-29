# Teacher's example Fruit
"""
class Fruit:
    def __init__ (fruit,name,weight,cost):
        fruit.name = name
        fruit.weight = weight
        fruit.cost = cost
    
    def __str__ (fruit):
        return f"Name:{fruit.name}\nWeight(g):{fruit.weight}\nCost:{fruit.cost}\n"
    
f1 = Fruit ("Apple",300,20)
f2 = Fruit ("Banana",500,25)
f3 = Fruit ("Watermelon",300,35)
typewriter_effect (f1)
typewriter_effect (f2)
typewriter_effect (f3)

time.sleep(3)
"""
# My own example (SDVX Login, Select game mode and my room's customize)

import time
import sys

def typewriter_effect(text, speed=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)


class SDVX:
    def __init__ (sdvx,player_name,player_id,volfroce,dan,played_times):
        sdvx.name = player_name
        sdvx.id = player_id
        sdvx.vol = volfroce
        sdvx.dan = dan
        sdvx.times = played_times
    def __str__ (sdvx):
        return f"Name:{sdvx.name}\nID:{sdvx.id}\nVolforce:{sdvx.vol}\nDan Class:{sdvx.dan}\nPlayed_Times:{sdvx.times}\n"
    
p1 = SDVX ("NekoTaro","SV-3810-7398",18.198,11,733)
typewriter_effect ("Welcome to Sound Voltex!\n")
time.sleep(3)
typewriter_effect ("Login...\n")
time.sleep(5)
print (p1)

# Game mode select 
time.sleep(5)
while True:
    time.sleep(1.5)
    typewriter_effect("1.NORMAL\n")
    time.sleep(0.2)
    typewriter_effect("2.FRIEND\n")
    time.sleep(0.2)
    typewriter_effect("3.MEGAMIX BATTLE\n")
    time.sleep(0.2)
    typewriter_effect("4.ARENA BATTLE\n")
    time.sleep(0.2)
    typewriter_effect("5.SINGLE BATTLE\n")
    time.sleep(0.2)
    typewriter_effect("6.BLASTER\n")
    time.sleep(0.2)
    typewriter_effect("7.PREMIUM TIME\n")
    time.sleep(0.2)
    typewriter_effect("8.SKILL ANALYZER\n")
    time.sleep(0.2)

    choice = input("\nSelect game mode:")

    if choice == "1":
        time.sleep(1.5)
        typewriter_effect("1.Light    start (4 CREDIT)  Level Resistance ON  -- ARS Rating OFF\n")
        time.sleep(0.5)
        typewriter_effect("2.Standard start (5 CREDIT)  Level Resistance OFF -- ARS Rating ON\n")
        time.sleep(0.5)
        choice = input("Select mode to continue:")
        break
    elif choice == "2":
        time.sleep(1.5)
        typewriter_effect("1.Light    start (4 CREDIT)  Level Resistance ON  -- ARS Rating OFF\n")
        time.sleep(0.5)
        typewriter_effect("2.Standard start (5 CREDIT)  Level Resistance OFF -- ARS Rating ON\n")
        time.sleep(0.5)
        choice = input("Select mode to continue:")
        break
    elif choice == "3":
        time.sleep(1.5)
        typewriter_effect("1.Light start (4 CREDIT)\n")
        time.sleep(0.5)
        choice = input("Select mode to continue:")
        if choice == "1":
            time.sleep(1.5)
            typewriter_effect("1.Local Battle\n")
            time.sleep(0.5)
            typewriter_effect("2.National Battle\n") 
            time.sleep(0.5)
            choice = input("Select mode to continue:")
        break
    elif choice == "4":
        time.sleep(1.5)
        typewriter_effect("1.Light    start (4 CREDIT)  Level Resistance ON  -- ARS Rating OFF\n")
        time.sleep(0.5)
        typewriter_effect("2.Standard start (5 CREDIT)  Level Resistance OFF -- ARS Rating ON\n")
        time.sleep(0.5)
        choice = input("Select mode to continue:")
        if choice == "1":
            time.sleep(1.5)
            typewriter_effect("1.Rank Battle\n")
            time.sleep(0.5)
            typewriter_effect("2.Online Battle\n")
            time.sleep(0.5)
            typewriter_effect("3.Local Battle\n") 
            time.sleep(0.5)
            choice = input("Select mode to continue:")
        break
    elif choice == "5":
        time.sleep(1.5)
        typewriter_effect("1.Light    start (4 CREDIT)  Level Resistance ON  -- ARS Rating OFF\n")
        time.sleep(0.5)
        typewriter_effect("2.Standard start (5 CREDIT)  Level Resistance OFF -- ARS Rating ON\n")
        time.sleep(0.5)
        choice = input("Select mode to continue:")
        break
    elif choice == "6":
        time.sleep(1.5)
        typewriter_effect("2.Standard start (6 CREDIT)  Level Resistance OFF -- ARS Rating ON\n")
        time.sleep(0.5)
        choice = input("Select mode to continue:")
        break
    elif choice == "7":
        time.sleep(1.5)
        typewriter_effect("2.Standard start (6 CREDIT)  Level Resistance OFF -- ARS Rating ON\n")
        time.sleep(0.5)
        choice = input("Select mode to continue:")
        break
    elif choice == "8":
        time.sleep(1.5)
        typewriter_effect("1.Light    start (4 CREDIT)  Level Resistance ON  -- ARS Rating OFF\n")
        time.sleep(0.5)
        typewriter_effect("2.Standard start (5 CREDIT)  Level Resistance OFF -- ARS Rating ON\n")
        time.sleep(0.5)
        choice = input("Select mode to continue:")
        break
    else:
        typewriter_effect("Sorry, there was a misinput\nPlease enter the numbers on the menu to continue\n")

#My room (where you can customize your stuff)

while True:
    time.sleep(1.5)
    typewriter_effect("Welcome to My-room, you can customize your personal slyle here!\n\n")
    time.sleep(1)
    typewriter_effect("1.Game start\n")
    time.sleep(0.5)
    typewriter_effect("2.Crew\n")
    time.sleep(0.5)
    typewriter_effect("3.Appeal Card\n")
    time.sleep(0.5)
    typewriter_effect("4.Valkrie Generator\n")
    time.sleep(0.5)

    choice = input("\nSelect your option:")

    if choice == "1":
        time.sleep(1.5)
        typewriter_effect("Game start!\n")
        time.sleep(3)
        typewriter_effect("Enjoy the world of Sound voltex~")
        break
    elif choice == "2":
        time.sleep(1.5)
        typewriter_effect("1.Rasis\n")
        time.sleep(0.5)
        typewriter_effect("2.Grace\n")
        time.sleep(0.5)
        choice = input("Select your Navigator:")
        if choice == "1":
            typewriter_effect ("Navigatior selected!\n")
            time.sleep(1)
            typewriter_effect ("Rasis:Thank you for select me as your navigator, I will do my best to support you!\n")
            continue
        elif choice == "2":
            typewriter_effect ("Navigatior selected!\n")
            time.sleep(1)
            typewriter_effect ("Grace:You should be thankful that you got my support~, you better do your best this time!\n")
            continue
    elif choice == "3":
        time.sleep(1.5)
        typewriter_effect("1.Test Card\n")
        time.sleep(0.5)
        typewriter_effect("2.Test Card\n")
        time.sleep(0.5)
        typewriter_effect("3.Test Card\n")
        time.sleep(0.5)
        choice = input("Select your Appeal Card:")
        if choice == "1":
            typewriter_effect ("Card 1 selected!\n")
            continue
        elif choice == "2":
            typewriter_effect ("Card 2 selected!\n")
            continue
        elif choice == "3":
            typewriter_effect ("Card 3 selected!\n")
            continue
    elif choice == "4":
        time.sleep(1.5)
        typewriter_effect ("Generator vol.1 Grace\n")
        time.sleep(0.5)
        typewriter_effect ("Generator vol.2 Tsuma buki\n")
        time.sleep(0.5)
        typewriter_effect ("Generator vol.3 Near & Noah\n")
        time.sleep(0.5)
        choice = input("Select your Valkrie Generator to roll:")
        if choice == "1":
            typewriter_effect ("Rolling...\n")
            time.sleep(6)
            typewriter_effect ("You got an item!\n")
            continue
        elif choice == "2":
            typewriter_effect ("Rolling...\n")
            time.sleep(6)
            typewriter_effect ("You got an item!\n")
            continue
        elif choice == "3":
            typewriter_effect ("Rolling...\n")
            time.sleep(6)
            typewriter_effect ("You got an item!\n")       
            continue

    else:
        typewriter_effect("Sorry, there was a misinput\nPlease enter the numbers on the menu to continue\n")