import sys
import keyboard
from random import randint
def prat(x,y,txt):
    print(f"\033[{y};{x}H", end="")
    print(txt)
#to do:
#  make the bricks be bricky
brck=[
    " _____",
    "|     |",
    "|     |",
    "|_____|",
    ]
class board:
    def __init__(self):
        self.brd=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        # self.brd[0][0]=2
        # self.brd[2][0]=2
        # prat(0,17,self.brd)
    def gn(self):
        while True:
            x=randint(0,3)
            y=randint(0,3)
            if self.brd[y][x]==0:
                c=int(randint(2,6)/2)+1
                if c==3:
                    c=2
                self.brd[y][x]=c
                return
    def move(self,d):
        mvd=True
        while mvd:
            mvd=False
            if d==0:#up
                for i in range(3,-1,-1):
                    for j in range(4):
                        if i>0 and self.brd[i][j]!=0:
                            if self.brd[i-1][j]==0:
                                self.brd[i][j],self.brd[i-1][j]=0,self.brd[i][j]
                                mvd=True
                            elif self.brd[i-1][j]==self.brd[i][j]:
                                self.brd[i][j],self.brd[i-1][j]=0,self.brd[i][j]+self.brd[i-1][j]
                                mvd=True
                            else:
                                pass
            elif d==1:#right
                for j in range(4):
                    for i in range(4):
                        if j<3 and self.brd[i][j]!=0:
                            if self.brd[i][j+1]==0:
                                self.brd[i][j],self.brd[i][j+1]=0,self.brd[i][j]
                                mvd=True
                            elif self.brd[i][j+1]==self.brd[i][j]:
                                self.brd[i][j],self.brd[i][j+1]=0,self.brd[i][j]+self.brd[i][j+1]
                                mvd=True
                            else:
                                pass
            elif d==2:#down
                for i in range(4):
                    for j in range(4):
                        if i<3 and self.brd[i][j]!=0:
                            if self.brd[i+1][j]==0:
                                self.brd[i][j],self.brd[i+1][j]=0,self.brd[i][j]
                                mvd=True
                            elif self.brd[i+1][j]==self.brd[i][j]:
                                self.brd[i][j],self.brd[i+1][j]=0,self.brd[i][j]+self.brd[i+1][j]
                                mvd=True
                            else:
                                pass
            elif d==3:#left
                for j in range(3,-1,-1):
                    for i in range(4):
                        if j>0 and self.brd[i][j]!=0:
                            if self.brd[i][j-1]==0:
                                self.brd[i][j],self.brd[i][j-1]=0,self.brd[i][j]
                                mvd=True
                            elif self.brd[i][j-1]==self.brd[i][j]:
                                self.brd[i][j],self.brd[i][j-1]=0,self.brd[i][j]+self.brd[i][j-1]
                                mvd=True
                            else:
                                pass
            if mvd==False:
                self.gn()
                return
    def prnt(self):
        for y,i in enumerate(self.brd):
            for x,j in enumerate(i):
                prat(2+x*6,3+y*3,"    ")
                if j!=0:
                    prat(2+x*6,3+y*3,j)
        prat(0,14,"is")
b=board()
print("\033c")
prat(0,0,""" _____ _____ _____ _____
|     |     |     |     |
|     |     |     |     |
|_____|_____|_____|_____|
|     |     |     |     |
|     |     |     |     |
|_____|_____|_____|_____|
|     |     |     |     |
|     |     |     |     |
|_____|_____|_____|_____|
|     |     |     |     |
|     |     |     |     |
|_____|_____|_____|_____|
""")
mvr=4
def ip(ky):
    return keyboard.is_pressed(ky)
while True:
    b.move(mvr)
    b.prnt()
    kd=True
    while kd:
        if not ip("left") and not ip("right") and not ip("up") and not ip("down"):
            kd=False
    ky=keyboard.read_key()
    # prat(0,20,keyboard.KEY_DOWN)
    if ky=="up":
        mvr=0
    elif ky=="right":
        mvr=1
    elif ky=="down":
        mvr=2
    elif ky=="left":
        mvr=3
    else:
        mvr=4
    ky=""