import pygame as pg, sys
from pygame.locals import *

pg.init()

S_WIDTH = 1200
S_HEIGHT = 800

screen = pg.display.set_mode((S_WIDTH, S_HEIGHT))
screen.fill((255, 255, 255))

while True:
    pg.display.update()
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
