import time

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
print (f1)
print (f2)
print (f3)

time.sleep(3)
"""
# My own example (SDVX Login, Select game mode and my room's customize)

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
print ("Welcome to Sound Voltex!\n")
time.sleep(3)
print ("Login...\n")
time.sleep(5)
print (p1)

# Game mode select 
time.sleep(5)
while True:
    time.sleep(1.5)
    print("1.NORMAL")
    time.sleep(0.2)
    print("2.FRIEND")
    time.sleep(0.2)
    print("3.MEGAMIX BATTLE")
    time.sleep(0.2)
    print("4.ARENA BATTLE")
    time.sleep(0.2)
    print("5.SINGLE BATTLE")
    time.sleep(0.2)
    print("6.BLASTER")
    time.sleep(0.2)
    print("7.PREMIUM TIME")
    time.sleep(0.2)
    print("8.SKILL ANALYZER")
    time.sleep(0.2)

    choice = input("\nSelect game mode:")

    if choice == "1":
        time.sleep(1.5)
        print("1.Light    start (4 CREDIT)  Level Resistance ON  -- ARS Rating OFF")
        time.sleep(0.5)
        print("2.Standard start (5 CREDIT)  Level Resistance OFF -- ARS Rating ON")
        time.sleep(0.5)
        choice = input("\nSelect mode to continue:")
        break
    elif choice == "2":
        time.sleep(1.5)
        print("1.Light    start (4 CREDIT)  Level Resistance ON  -- ARS Rating OFF")
        time.sleep(0.5)
        print("2.Standard start (5 CREDIT)  Level Resistance OFF -- ARS Rating ON")
        time.sleep(0.5)
        choice = input("\nSelect mode to continue:")
        break
    elif choice == "3":
        time.sleep(1.5)
        print("1.Light start (4 CREDIT)")
        time.sleep(0.5)
        choice = input("Select mode to continue:")
        if choice == "1":
            time.sleep(1.5)
            print("1.Local Battle")
            time.sleep(0.5)
            print("2.National Battle") 
            time.sleep(0.5)
            choice = input("\nSelect mode to continue:")
        break
    elif choice == "4":
        time.sleep(1.5)
        print("1.Light    start (4 CREDIT)  Level Resistance ON  -- ARS Rating OFF")
        time.sleep(0.5)
        print("2.Standard start (5 CREDIT)  Level Resistance OFF -- ARS Rating ON")
        time.sleep(0.5)
        choice = input("\nSelect mode to continue:")
        if choice == "1":
            time.sleep(1.5)
            print("1.Rank Battle")
            time.sleep(0.5)
            print("2.Local Battle")
            time.sleep(0.5)
            print("3.National Battle") 
            time.sleep(0.5)
            choice = input("\nSelect mode to continue:")
        break
    elif choice == "5":
        time.sleep(1.5)
        print("1.Light    start (4 CREDIT)  Level Resistance ON  -- ARS Rating OFF")
        time.sleep(0.5)
        print("2.Standard start (5 CREDIT)  Level Resistance OFF -- ARS Rating ON")
        time.sleep(0.5)
        choice = input("\nSelect mode to continue:")
        break
    elif choice == "6":
        time.sleep(1.5)
        print("1.Light    start (4 CREDIT)  Level Resistance ON  -- ARS Rating OFF")
        time.sleep(0.5)
        print("2.Standard start (5 CREDIT)  Level Resistance OFF -- ARS Rating ON")
        time.sleep(0.5)
        choice = input("\nSelect mode to continue:")
        break
    elif choice == "7":
        time.sleep(1.5)
        print("1.Light    start (4 CREDIT)  Level Resistance ON  -- ARS Rating OFF")
        time.sleep(0.5)
        print("2.Standard start (5 CREDIT)  Level Resistance OFF -- ARS Rating ON")
        time.sleep(0.5)
        choice = input("Select mode to continue:")
        break
    elif choice == "8":
        time.sleep(1.5)
        print("1.Light    start (4 CREDIT)  Level Resistance ON  -- ARS Rating OFF")
        time.sleep(0.5)
        print("2.Standard start (5 CREDIT)  Level Resistance OFF -- ARS Rating ON")
        time.sleep(0.5)
        choice = input("Select mode to continue:")
        break

#My room (where you can customize your stuff)

while True:
    time.sleep(1.5)
    print("1.Game start")
    time.sleep(0.5)
    print("2.Crew")
    time.sleep(0.5)
    print("3.Appeal Card ")
    time.sleep(0.5)
    print("4.Valkrie Generator")
    time.sleep(0.5)

    choice = input("\nSelect your option:")

    if choice == "1":
        time.sleep(1.5)
        print("Game start!")
        time.sleep(3)
        print("Enjoy the world of Sound voltex~")
        break
    elif choice == "2":
        time.sleep(1.5)
        print("1.Rasis")
        time.sleep(0.5)
        print("2.Grace")
        time.sleep(0.5)
        choice = input("Select your Navigator:")
        if choice == "1":
            print ("Navigatior selected!")
            time.sleep(1)
            print ("Rasis:Thank you for select me as your navigator, I will do my best to support you!")
            continue
        elif choice == "2":
            print ("Navigatior selected!")
            time.sleep(1)
            print ("Grace:You should be thankful that you got my support~")
            continue
    elif choice == "3":
        time.sleep(1.5)
        print("1.Test Card")
        time.sleep(0.5)
        print("2.Test Card")
        time.sleep(0.5)
        print("3.Test Card")
        time.sleep(0.5)
        choice = input("\nSelect your Appeal Card:")
        if choice == "1":
            print ("Card 1 selected!")
            continue
        elif choice == "2":
            print ("Card 2 selected!")
            continue
        elif choice == "3":
            print ("Card 2 selected!")
            continue
    elif choice == "4":
        time.sleep(1.5)
        print ("Generator vol.1 Grace")
        time.sleep(0.5)
        print ("Generator vol.2 Tsuma buki")
        time.sleep(0.5)
        print ("Generator vol.3 Near & Noah")
        time.sleep(0.5)
        choice = input("\nSelect your Valkrie Generator to roll:")
        if choice == "1":
            print ("Rolling...")
            time.sleep(6)
            print ("You got an item!")
            continue
        elif choice == "2":
            print ("Rolling...")
            time.sleep(6)
            print ("You got an item!")
            continue
        elif choice == "3":
            print ("Rolling...")
            time.sleep(6)
            print ("You got an item!")       
            continue

    else:
        print("Sorry, wrong input\nPlease enter 1 2 3 and 4 to continue")