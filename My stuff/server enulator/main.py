from random import random, randint
from time import sleep
import sys
# from sys.stdout import write
def wrint(txt):
    print(txt,end="")
def move(x, y):
    print(f"\033[{y};{x}H", end="")
def prat(txt,x,y):
    move(x,y)
    print(txt)
def add(tm):
    b2=random()/5
    tm[2]+=b2
    sleep(b2*2)
    if tm[2]>=60:
        tm[2]=0
        tm[1]+=1
    if tm[1]>=60:
        tm[1]=0
        tm[0]+=1
    if tm[0]>=24:
        tm[0]=0
    return tm.copy()
t=add([randint(0,23),randint(0,60),randint(0,60)])
def init():
    global t
    print(f"[{t[0]}:{t[1]}:{int(t[2])}] [INFO] This is v82.5")
    t=add(t)
    print(f"[{t[0]}:{t[1]}:{int(t[2])}] [INFO] Running boot")
    n=len(f"[{t[0]}:{t[1]}:{int(t[2])}] [INFO] ")
    for i in range(3):
        t=add(t)
        sleep(randint(1,2)/5)
        prat(".",n+13+i,2)
    n=len(f"[{t[0]}:{t[1]}:{int(t[2])}] [INFO] ")-1
    print(f"[{t[0]}:{t[1]}:{int(t[2])}] [INFO] Boot complete\n[{t[0]}:{t[1]}:{int(t[2])}] [INFO] Running setup")
    for i in range(3):
        t=add(t)
        sleep(randint(1,2)/5)
        prat(".",n+15+i,4)
    print(f"[{t[0]}:{t[1]}:{int(t[2])}] [INFO] Setup complete")
    t=add(t)
    n=len(f"[{t[0]}:{t[1]}:{int(t[2])}] [INFO] ")
    print(f"[{t[0]}:{t[1]}:{int(t[2])}] [INFO] Starting Server")
    for i in range(3):
        t=add(t)
        sleep(randint(1,2)/5)
        prat(".",n+16+i,6)
    t=add(t)
    print(f"[{t[0]}:{t[1]}:{int(t[2])}] [INFO] Server Started")
    t=add(t)
    # print(f"[{t[0]}:{t[1]}:{int(t[2])}] [INFO] ")
    # t=add(t)
    print(f"[{t[0]}:{t[1]}:{int(t[2])}] [INFO] Ending Init script")
    sleep(0.1)
    t=add(t)
    print(f"[{t[0]}:{t[1]}:{int(t[2])}] [INFO] Init script ended")
    t=add(t)
def dedifY():
    global t
    print(f"[{t[0]}:{t[1]}:{int(t[2])}] [INFO] Initializing server termination!")
    t=add(t)
    print(f"[{t[0]}:{t[1]}:{int(t[2])}] [INFO] Terminating")
    t=add(t)
    print(f"[{t[0]}:{t[1]}:{int(t[2])}] [INFO] Terminating.")
    t=add(t)
    print(f"[{t[0]}:{t[1]}:{int(t[2])}] [INFO] Terminating..")
    t=add(t)
    print(f"[{t[0]}:{t[1]}:{int(t[2])}] [INFO] Terminating...")
    t=add(t)
    print(f"[{t[0]}:{t[1]}:{int(t[2])}] [INFO] Server is terminated")
    t=add(t)
    print(f"[{t[0]}:{t[1]}:{int(t[2])}] [INFO] Please come buy again!")
    t=add(t)
    quit()
def dor():
    global t
    ban=input(" >> ").lower()
    if ban=="help":
        print(f"\"settings\" lets you edit the settings.\n\"stop\" ends the server.\n\"status\" lets you check up on the servers stats.")
        t=add(t)
    elif "settings"in ban:
        print(f"[{t[0]}:{t[1]}:{int(t[2])}] [INFO] There are no settings to change lol")
        t=add(t)
    elif ban=="stop":
        dedifY()
    elif ban=="status":
        print(f"[{t[0]}:{t[1]}:{int(t[2])}] [INFO] Quarbling: {randint(98,100)}%")
        t=add(t)
        print(f"[{t[0]}:{t[1]}:{int(t[2])}] [INFO] The rocks are all fed!")
        t=add(t)
        print(f"[{t[0]}:{t[1]}:{int(t[2])}] [INFO] Performing character checks...")
        t=add(t)
        if randint(0,5)==0:
            print(f"[{t[0]}:{t[1]}:{int(t[2])}] [INFO] All characters are sus")
            t=add(t)
            print(f"[{t[0]}:{t[1]}:{int(t[2])}] [INFO] Preparing to eliminate all susses")
            t=add(t)
            print(f"[{t[0]}:{t[1]}:{int(t[2])}] [INFO] *server go boom*")
            t=add(t)
            dedifY()
        print(f"[{t[0]}:{t[1]}:{int(t[2])}] [INFO] No sus characters found")
        t=add(t)
        print(f"[{t[0]}:{t[1]}:{int(t[2])}] [INFO] All systems good")
        t=add(t)
    elif ban=="hack":
        # pass
        print(f"[{t[0]}:{t[1]}:{int(t[2])}] [INFO] Erm no")
        t=add(t)
    else:
        print(f"Error: \"{ban}\" is not a valid input! You can do \"settings\", \"stop\", \"status\" and \"help\"!")
print("\033c",end="")
init()
while True:
    dor()