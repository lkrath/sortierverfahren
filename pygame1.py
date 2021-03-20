import pygame as pg, sys

#from pygame.locals import *
#(
#    K_UP,
#    K_DOWN,
#    K,LEFT,
#    K_RIGHT,
#    K_ESCAPE,
#    QUIT,
#)

pg.init()

w = ord('w')
a = ord('a')
s = ord('s')
d = ord('d')

# um beides benutzen zu können
# if event.key == pg.K_LEFT or event.key == ord('a'):  

S_WIDTH = 1200
S_HEIGHT = 800

screen = pg.display.set_mode((S_WIDTH, S_HEIGHT))
screen.fill((255, 255, 255))

pg.draw.circle(screen, (0, 255, 255), (600, 400), 75)

start = True

while start:

    i = 0

    for event in pg.event.get():
        if event.type == pg.QUIT:
            start = False

        if event.type == pg.K_LEFT:
            #if event.key == pg.K_LEFT:
            i += 10
            screen.fill((255, 255, 255))
            pg.draw.circle(screen, (0, 255, 255), (600-i, 400), 75)
            pg.display.flip

    #pg.draw.circle(screen, (0, 255, 255), (600, 400), 75) # screen, farbe, position, radius?

    pg.display.flip() # braucht am immer weil sonst nichts angezeigt

pg.quit()