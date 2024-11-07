import pygame as py
from random import randint
py.init()
X = 1000
Y = 1000
scrn = py.display.set_mode((X, Y))
clk=py.time.Clock()
font = py.font.SysFont(None, 50)
# set the py window name
py.display.set_caption('image')
# create a surface object, image is drawn on it.
back = py.image.load("flabby bird\\background.png").convert()
brd = py.image.load("flabby bird\\bird.png").convert()
grnd = py.image.load("flabby bird\\ground.png").convert()
pip = py.image.load("flabby bird\\pipe.png").convert()
fpip = py.transform.flip(py.image.load("flabby bird\\pipe.png").convert(),False,True)
class pipe:
    def __init__(self,x,y,g,sp):
        self.x,self.y,self.gp=x,y,randint(200,250)
        self.sp=1+sp/10
        self.ck=False
        # self.p=pip
        # self.fp=fpip
        # self.r=self.p.get_rect()
        # self.fr=self.fp.get_rect()
    def dr(self):
        # self.r.center=(self.x,self.y)
        # self.fr.center=(self.x,self.y)
        self.x-=self.sp
        scrn.blit(pip,(self.x,self.y))
        scrn.blit(fpip,(self.x,self.y-827-self.gp))
# Using blit to copy content from one surface to other
# scrn.blit(pip, (0, 0))
# paint screen one time
def gn(s,xp=0):
    return pipe(1000+xp,randint(100,620),0,s)
# for i in range(1):
# pps.append()
class brrd:
    def __init__(self):
        self.x=200
        self.y=100
        self.ys=0
        self.bp=0
        self.sc=0
        self.t=[self.y for i in range(100)]
    def dr(self,kd):
        # if self.ys<3:
        self.ys+=0.1
        if kd and self.bp<0:
            self.bp=10
            self.ys=-4
        self.y+=self.ys
        self.bp-=1
        self.t=self.t[1:]+[self.y]
def drw(c=True):
    global hs
    scrn.blit(back, (753, -500))
    scrn.blit(back, (0, -500))
    for i in range(len(br.t)-1):
        scrn.blit(brd, (br.x-(len(br.t)-2-i)*2, br.t[i]))
    scrn.blit(brd, (br.x, br.y))
    d=False
    for a,i in enumerate(pps):
        # if i.x+160<0:
        #     pps.append(gn(randint(450,550)))
        i.dr()
        # scrn.blit(font.render(f"{br.y}\n{i.y-i.gp}\n{i.y}", True, (0,0,0)),(i.x,i.y))
        if br.x+100>i.x and br.x<i.x+160 and c:
            if (br.y<i.y-i.gp or br.y+70>i.y):
                scrn.blit(font.render(f"YOU DIED", True, (255,0,0)),(450,500))
                d=True
            else:
                # br.sc+=1
                i.ck=True
        if br.x>i.x+159 and i.ck:
            i.ck=False
            br.sc+=1
    # scrn.blit(brd)
    if br.sc>hs:
        hs=br.sc
    scrn.blit(font.render(f"Highscore: {hs}", True, (0,0,0)),(0,0))
    scrn.blit(font.render(f"Score: {br.sc}", True, (0,0,0)),(0,50))
    scrn.blit(grnd, (0, 700))
    scrn.blit(grnd, (750, 700))
    py.display.flip()
    return "ded" if d else ""
# py.display.flip()
run=True
hs=0
br=brrd()
while run:
    pps=[gn(br.sc,-200)]
    br=brrd()
    drw()
    t=7*60
    status=True
    while (status):
        kd=False
        if t>randint(7,8)*60:
            t=0
            pps.append(gn(br.sc,randint(450,550)))
        for i in py.event.get():
            if i.type == py.QUIT:
                status = False
            elif i.type==py.KEYDOWN:
                if i.key==py.K_SPACE:
                    kd=True
        br.dr(kd)
        scrn.fill((255, 255, 255))
        if drw()=="ded":
            break
        clk.tick(60)
        t+=1
    # deactivates the py library
    while True:
        for i in py.event.get():
            if i.type == py.QUIT:
                py.quit()