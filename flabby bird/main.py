import pygame as py
import sys
from random import randint,choice
py.init()
X = 1000
Y = 1000
scrn = py.display.set_mode((X, Y))
clk=py.time.Clock()
font = py.font.SysFont(None, 50)
# set the py window name
py.display.set_caption('image')
# create a surface object, image is drawn on it.
def grayscale(surface):
    width, height = surface.get_size()
    grayscale_surface = py.Surface((width, height))#,py.SRCALPHA)
    
    for x in range(width):
        for y in range(height):
            color = surface.get_at((x, y))
            gray = py.Color(color.r, color.g, color.b,color.a).grayscale()
            grayscale_surface.set_at((x, y), gray)
    
    return grayscale_surface
def colorize(image, new_color):
    tinted = py.Surface(image.get_size(), py.SRCALPHA)
    tinted.fill(new_color)
    tinted.blit(image, (0, 0), special_flags=py.BLEND_RGBA_MULT)
    return tinted
    """
    Create a "colorized" version of the image.
    """
    image = image.copy()
    image.fill(new_color[0:3] + (0,), special_flags=py.BLEND_RGBA_MULT)
    return image
back = py.image.load("flabby bird\\background.png").convert_alpha()
gbrd =py.transform.grayscale(py.image.load("flabby bird\\bird.png").convert_alpha()) #colorize(grayscale(py.image.load("flabby bird\\bird.png").convert_alpha()),(255,0,0))
brd=colorize(gbrd,(255,0,0))
grnd = py.image.load("flabby bird\\ground.png").convert_alpha()
pip = py.image.load("flabby bird\\pipe.png").convert_alpha()
err=py.image.load("flabby bird\\erer.png").convert_alpha()
fpip = py.transform.flip(py.image.load("flabby bird\\pipe.png").convert_alpha(),False,True)
class pipe:
    def __init__(self,x,y,g,sp):
        self.x,self.y,self.gp=x,y,randint(200,250)
        self.sp=3+sp/10
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
    return pipe(1000+xp,choice([280,425,562])+randint(-50,50),0,s)#randint(100,620)
# for i in range(1):
# pps.append()
class brrd:
    def __init__(self):
        self.x=200
        self.y=100
        self.ys=0
        self.bp=0
        self.sc=0
        self.t=[self.y for i in range(50)]
    def dr(self,kd):
        # if self.ys<3:
        self.ys+=0.1
        if kd and self.bp<0:
            self.bp=10
            self.ys=-4
        self.y+=self.ys
        self.bp-=1
        self.t=self.t[1:]+[self.y]
def drw(rx,ry,spI):
    global hs
    scrn.blit(back, (750, -500))
    scrn.blit(back, (0, -500))
    # for i in range(len(br.t)-1):
    #     brd2=brd
    #     brd2.set_alpha(i*50)
    #     scrn.blit(brd2, (br.x-(len(br.t)-2-i)*10, br.t[i]))
    scrn.blit(py.transform.rotate(brd, br.ys*-5),(br.x, br.y))
    d=False
    for a,i in enumerate(pps):
        # if i.x+160<0:
        #     pps.append(gn(randint(450,550)))
        i.sp=2+(br.sc)/5
        i.dr()
        # scrn.blit(font.render(f"{br.y}\n{i.y-i.gp}\n{i.y}", True, (0,0,0)),(i.x,i.y))
        if br.x+75>i.x and br.x<i.x+130 and True:
            # scrn.blit(font.render(f"in", True, (0,0,0)),(i.x,i.y))
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
    cat=False
    if br.x+75>rx and br.x-130<rx+100 and br.y>ry and br.y<ry+200:
        cat=True
    if br.sc>hs:
        hs=br.sc
    scrn.blit(font.render(f"Highscore: {hs}", True, (0,0,0)),(0,0))
    scrn.blit(font.render(f"Score: {br.sc}", True, (0,0,0)),(0,50))
    scrn.blit(err,(rx,ry))
    scrn.blit(grnd, (0, 700))
    scrn.blit(grnd, (750, 700))
    py.display.flip()
    return "ded" if d else ("cat" if cat else"")
# py.display.flip()
def map(value, start1, stop1, start2, stop2):
    return start2 + (stop2 - start2) * ((value - start1) / (stop1 - start1))
run=True
hs=0
br=brrd()
ux=0
uy=0
curdler=True
r=0
g=0
b=0
while curdler:
    for i in py.event.get():
        if i.type == py.QUIT:
            py.quit()
        if i.type == py.MOUSEBUTTONDOWN:
            curdler=False
    mx,my=py.mouse.get_pos()
    g=min(255,max(0,map(my,0,1000,0,255)))
    r=min(255,max(0,map(mx,0,500,0,255)))
    b=min(255,max(0,map(mx,500,1000,0,255)))
    scrn.fill((255,255,255))
    scrn.blit(font.render(f"Press space to fly up. Press left shift to dive more.", True, (0,0,0)),(0,50))
    scrn.blit(font.render(f"press space to continue", True, (0,0,0)),(0,100))
    scrn.blit(font.render(f"Move your mouse to change the color,{(int(r),int(g),int(b))}", True, (0,0,0)),(0,150))
    scrn.blit(brd,(200,200))
    #bottom is green
    #left is red
    #right is blue
    # print((int(r),int(g),int(b)))
    brd=colorize(gbrd,(int(r),int(g),int(b)))#py.transform.grayscale(brd)
    py.display.flip()
while run:
    ux=randint(1500,2000)
    uy=randint(0,500)
    spI=0
    pps=[gn(br.sc+spI,-200)]
    br=brrd()
    drw(ux,uy,spI)
    t=0
    pc=0
    status=True
    while (status):
        kd=False
        if pc!=br.sc and t>60*2:# or t>randint(10,11)*60:
            t=0
            pps.append(gn(br.sc+spI,randint(100,150)))
        for i in py.event.get():
            if i.type == py.QUIT:
                status = False
            elif i.type==py.KEYDOWN:
                if i.key==py.K_SPACE:
                    kd=True
            # if i.key==py.K_LSHIFT:# and br.ys<3:
            #     br.ys+=1
        # keys = 
        if py.key.get_pressed()[py.K_LSHIFT] and br.ys<3:
            br.ys+=0.5
        br.dr(kd)
        ux-=2+(br.sc+spI)/5
        scrn.fill((255, 255, 255))
        pc=br.sc
        drwd=drw(ux,uy,t)
        if drwd=="ded":
            break
        elif drwd=="cat":
            ux=randint(2000,3000)
            uy=randint(0,500)
            # spI+=1
            br.sc+=randint(2,4)
        clk.tick(60)
        t+=1
    # deactivates the py library
    curdler=True
    while curdler:
        for i in py.event.get():
            if i.type == py.QUIT:
                py.quit()
            if i.type == py.MOUSEBUTTONDOWN:
                curdler=False