import time

#Teacher's example
class Fruit:
    def __init__ (fruit,name,weight):
        fruit.name = name
        fruit.weight = weight
    
    def __str__ (fruit):
        return f"Name:{fruit.name}\nWeight(g):{fruit.weight}\n"
    
    
f1 = Fruit ("Apple",300)
print (f1)

time.sleep(3)

#My own example

class SDVX:
    def __init__ (sdvx,player_name,player_id,volfroce,dan,played_times):
        sdvx.name = player_name
        sdvx.id = player_id
        sdvx.vol = volfroce
        sdvx.dan = dan
        sdvx.times = played_times
    def __str__ (sdvx):
        return f"Name:{sdvx.name}\nID:{sdvx.id}\nVolforce:{sdvx.vol}\nDan Class:{sdvx.dan}\nPlayed_Times:{sdvx.times}"
    
p1 = SDVX ("NekoTaro","SV-3810-7398",18.198,11,733)
print ("Welcome to Sound Voltex!\n")
time.sleep(3)
print ("Login...\n")
time.sleep(5)
print (p1)