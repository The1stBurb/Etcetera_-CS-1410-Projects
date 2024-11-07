import pygame as py
py.init()
X = 750
Y = 1000
scrn = py.display.set_mode((X, Y))
clk=py.time.Clock()
# set the py window name
py.display.set_caption('image')
# create a surface object, image is drawn on it.
back = py.image.load("flabby bird\\background.png").convert()
brd = py.image.load("flabby bird\\bird.png").convert()
grnd = py.image.load("flabby bird\\ground.png").convert()
pip = py.image.load("flabby bird\\pipe.png").convert()
fpip = py.transform.flip(py.image.load("flabby bird\\pipe.png").convert(),False,True)
class pipe:
    def __init__(self,x,y,g):
        self.x,self.y,self.gp=x,y,g
        # self.p=pip
        # self.fp=fpip
        # self.r=self.p.get_rect()
        # self.fr=self.fp.get_rect()
    def dr(self):
        # self.r.center=(self.x,self.y)
        # self.fr.center=(self.x,self.y)
        # self.x-=1
        scrn.blit(pip,(self.x,self.y))
# Using blit to copy content from one surface to other
scrn.blit(back, (0, -500))
# scrn.blit(brd, (0, 0))
scrn.blit(grnd, (0, 700))
# scrn.blit(pip, (0, 0))
# paint screen one time
def drw():
    py.display.flip()
# py.display.flip()
drw()
pps=[pipe(500,0,10)]
status=True
while (status):
    for i in py.event.get():
        if i.type == py.QUIT:
            status = False
    scrn.fill((255, 255, 255))
    for i in pps:
        i.dr()
    drw()
    clk.tick(60)
# deactivates the py library
py.quit()