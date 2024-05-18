import pygame
from pygame.locals import *

class square(pygame.sprite.Sprite):
    def __init__(self):
        super(square,self).__init__()
        self.surf = pygame.surface((25,25))
        self.surf.fill((0,200,225))
        self.rect = self.surf.get_rect()

pygame.init()
screen =pygame.display.set_mode((800,600))
square1=square()
square2=square()
square3=square()
square4=square()

gameon = True

while gameon:
    for x in pygame.x.get():
        if x.type == KEYDOWN:
            if x.key == K_BACKSPACE:
                gameon = False
        elif x.type == QUIT:
            gameon = False
    screen.blit(square1.surf(40,40))
    screen.blit(square2.surf(80,80))
    screen.blit(square3.surf(160,160))
    screen.blit(square4.surf(240,240))

    pygame.display.flip()