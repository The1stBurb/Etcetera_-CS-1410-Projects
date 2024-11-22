from random import randint
stt={
    "bank":{"hp":3,"dex":1,"int":3},
    "sold":{"hp":7,"dex":3,"int":1},
    "warr":{"hp":10,"dex":5,"int":3},
    "wiza":{"hp":6,"dex":5,"int":5},
    "civn":{"hp":2,"dex":1,"int":0},
    "roge":{"hp":-2,"dex":7,"int":4},
    "dude":{"hp":-5,"dex":-5,"int":-5},
}
ft={"banker":"bank","soldier":"sold","warrior":"warr","wizard":"wiza","civilian":"civn","rogue":"rogue","tbo":"dude",}
cls=input("What class would you like to be? Banker, Soldier, Warrior, Wizard, Civilian, Rogue, or Tbo (The bad one)\n >> ").lower()
input("Roll for HP\n >> ")
hp=randint(5,10)
print("You got a",hp,"plus a class boost of",stt[ft[cls]]["hp"])
hp+=stt[ft[cls]]["hp"]
input("Roll for DEX\n >> ")
dex=randint(3,17)
print("You got a",dex,"plus a class boost of",stt[ft[cls]]["dex"])
dex+=stt[ft[cls]]["dex"]
input("Roll for INT\n >> ")
it=randint(3,17)
print("You got a",it,"plus a class boost of",stt[ft[cls]]["int"])
it+=stt[ft[cls]]["int"]
print("\n")
print(f"Your character:\n  Class: {cls}\n  HP: {hp}\n  DEX: {dex}\n  INT: {it}")