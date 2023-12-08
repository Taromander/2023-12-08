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
# My own example

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

# While menu example
time.sleep(5)
while True:
    print("1.Game start")
    print("2.Crew")
    print("3.Appeal Card ")
    print("4.Valkrie Generator")

    choice = input("Select your option:")

    if choice == "1":
        print("Game start")
        break
    elif choice == "2":
        print("1.Rasis")
        print("2.Grace")
        choice = input("Select your Navigator:")
        if choice == "1":
            print ("Navigatior selected!")
            continue
        elif choice == "2":
            print ("Navigatior selected!")
            continue
    elif choice == "3":
        print("1.Test Card")
        print("2.Test Card")
        print("3.Test Card")
        choice = input("Select your Appeal Card:")
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
        print ("Generator vol.1 Grace")
        print ("Generator vol.2 Tsuma buki")
        print ("Generator vol.3 Near & Noah")
        choice = input("Select your Valkrie Generator to roll:")
        if choice == "1":
            print ("Rolling...")
            time.sleep(6)
            print ("You got an item!")
            continue
        elif choice == "2":
            print ("Rolling...")
            print ("You got an item!")
            time.sleep(6)
            continue
        elif choice == "3":
            print ("Rolling...")
            print ("You got an item!")
            time.sleep(6)
            continue

    else:
        print("Sorry, wrong input\nPlease enter 1 2 3 and 4 to continue")