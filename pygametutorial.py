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

    #font = pygame.font.Font(None, 36)                   # schriftart, größe
    #text = font.render('Hello World', 1, (10, 10, 10))  # text, ?, farbe
    #textpos = text.get_rect()                           # 
    #textpos.centerx = bg.get_rect().centerx             # center x koordinate 
    #bg.blit(text, textpos)                              # text an der stelle 

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
    fullname = os.path.join('data', name)                 # bilder sind in directory data
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



class Ball(pygame.sprite.Sprite):                           # ball erbt alles von sprite, macht bewegen einfacher?
    def __init__(self, vector):                             # setup des balls
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png('ball.png')
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.vector = vector

    def update(self):                                       # updatet die position
        newpos = self.calcnewpos(self.rect, self.vector)
        self.rect = newpos
    
    def calcnewpos(self, rect, vector):                     # berechnet neue position des balls
        (angle, z) = vector                                 # winkel und geschwindigkeit
        (dx, dy) = (z * math.cos(angle), z * math.sin(angle))
        return rect.move(dx, dy)



class Bat(pygame.sprite.Sprite):
    def __init__(self, side):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png('bat.png')
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.side = side
        self.speed = 10
        self.state = 'still'
        self.reinit()

    def reinit(self):                                       # zurück zur ausgangsposition
        self.state = 'still'
        self.movepos = [0, 0]
        if self.side == 'left':
            self.rect.midleft = self.area.midleft
        elif self.side == 'right':
            self.rect.midright = self.area.midright

    def update(self):
        newpos = self.rect.move(self.movepos)
        if self.area.contains(newpos):
            self.rect = newpos
        pygame.event.pump()

    def moveup(self):                                       # für jeden frame bewegt sich der bat 10 pixel hoch
        self.movepos[1] = self.movepos[1] - (self.speed)
        self.state = 'moveup'

    def movedown(self):
        self.movepos[1] = self.movepos[1] + (self.speed)
        self.state = 'movedown'

for event in pygame.event.get():
    if event.type == QUIT:                                  # schießt die schleife wenn fenster geschlosen wird
        return
    elif event.type == KEYDOWN:                             # wenn eine taste gedrückt wird
        if event.key == K_UP:
            player.moveup()                                 # player ist ein objekt von Bat
        if event.key == K_DOWN:
            player.movedown()
    elif event.type == KEYUP:                               # wenn taste losgelassen wird
        if event.key == K_UP or event.key == K_DOWN:
            player.movepos[0, 0]
            player.state = 'still'



# anstoßen
if not self.area.contains(newpos):
    tl = not self.area.collidepoint(newpos.topleft)         # collidiert der nicht oben links
    tr = not self.area.collidepoint(newpos.topright)
    bl = not self.area.collidepoint(newpos.bottomleft)
    br = not self.area.collidepoint(newpos.bottomright)
    if tr and tl or (br and bl):                            # wenn der ball oben oder unten anschlägt prallt er ab
        angle = - angle
    if tl and bl:                                           # wenn er an der seite anschlägt geht er aus
        self.offcourt(player = 2)
    if tr and br:
        self.offcourt(player = 1)
else:
    player1.rect.inflate(-3, -3)                            # damit der ball nicht hinten vom schläger geschlagen wird?
    player2.rect.inflate(-3, -3)

    if self.rect.colliderect(player1.rect) == 1 and not self.hit: # teil ist dafür das der ball nicht im schläger hin und herspringen kann
        angle = math.pi - angle
        self.hit = not self.hit                             
    elif self.rect.colliderect(player2.rect) == 1 and not self.hit: # colliderect gibt true zurück wenn zwei rechtecke überlappen
        angle = math.pi - angle
        self.hit = not self.hit
    elif self.hit:
        self.hit = not self.hit

self.vector = (angle, z)                                    # vector updaten

pygame.quit()