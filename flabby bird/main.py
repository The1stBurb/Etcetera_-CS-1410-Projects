import pygame as py
class pipe:
    def __init__(self,x,y,g):
        self.x,self.y,self.gp=x,y,g
py.init()
X = 600
Y = 600
scrn = py.display.set_mode((X, Y))
# set the py window name
py.display.set_caption('image')
# create a surface object, image is drawn on it.
back = py.image.load("flabby bird\\background.png").convert()
brd = py.image.load("flabby bird\\bird.png").convert()
grnd = py.image.load("flabby bird\\ground.png").convert()
pip = py.image.load("flabby bird\\pipe.png").convert()
# Using blit to copy content from one surface to other
scrn.blit(back, (0, 0))
scrn.blit(brd, (0, 0))
scrn.blit(grnd, (0, 0))
scrn.blit(pip, (0, 0))
# paint screen one time
py.display.flip()
status=True
while (status):
    for i in py.event.get():
        if i.type == py.QUIT:
            status = False 
# deactivates the py library
py.quit()