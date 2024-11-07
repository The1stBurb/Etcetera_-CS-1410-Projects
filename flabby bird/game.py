import pygame as py
class gam:
    def __init__(self,brd,pip,bac):
        self.brd=py.image.load("flabby bird\\bird.png").convert_alpha()
        self.pip=py.image.load("flabby bird\\pipe.png").convert_alpha()
        self.fpip=py.transform.flip(py.image.load("flabby bird\\pipe.png").convert_alpha(),False,True)
        self.bac = py.image.load("flabby bird\\background.png").convert_alpha()
        grnd = py.image.load("flabby bird\\ground.png").convert_alpha()
    def resImg(self):
        self.brd=py.transform.scale(self.brd,(51,34))