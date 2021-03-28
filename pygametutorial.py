try:
    import sys
    import random
    import math
    import os
    import getopt
    import pygame
    from pygame.locals import *
    from socket import *
except(ImportError, err):                                # falls was nicht importiert werden kann
    print('couldnt load module. %s' % err)
    sys.exit(2)

def main():

    pygame.init()
    screen = pygame.display.set_mode((150, 50))         # größe display 
    pygame.display.set_caption('Basic Pygame Program')  # fenster caption 

    bg = pygame.Surface(screen.get_size())              # surface object
    bg = bg.convert()                                   # convert to single pixel formats (schnelleres rendering)
    bg.fill((250, 250, 250))                            # farbe vom screen 

    font = pygame.font.Font(None, 36)                   # schriftart, größe
    text = font.render('Hello World', 1, (10, 10, 10))  # text, ?, farbe
    textpos = text.get_rect()                           # 
    textpos.centerx = bg.get_rect().centerx             # center x koordinate 
    bg.blit(text, textpos)                              # text an der stelle 

    screen.blit(bg, (0, 0))                             # im grunde rendern
    pygame.display.flip()           	                # anzeigen?

    while True:

        for event in pygame.event.get():
            if event.type == QUIT:                      
                return                                  # beenden wenn schließen
        
        screen.blit(bg, (0, 0))
        pygame.display.flip()

if __name__ == '__main__': main()

def load_png(name):                                     # ein png laden, gibt image object zurück
    fullname = os.path.join('data', name)               # bilder sind in directory data
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except(pygame.error, message):
        print('cannot load image: ' + fullname)
        raise(SystemExit, message)
    return image, image.get_rect()

def load_sound(name):                                     # ein png laden, gibt image object zurück
    fullname = os.path.join('data', name)               # bilder sind in directory data
    try:
        sound = pygame.sound.load(fullname)
        if sound.get_alpha() is None:
            sound = sound.convert()
        else:
            sound = sound.convert_alpha()
    except(pygame.error, message):
        print('cannot load sound: ' + fullname)
        raise(SystemExit, message)
    return sound, sound.get_rect()

pygame.quit()