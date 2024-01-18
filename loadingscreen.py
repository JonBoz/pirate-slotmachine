import pygame, random, time,os
from pygame.locals import *
from settings import *

load = pygame.display.set_mode((800,600))

def loadingscreen():
    load.blit(Totenkopf,(100,100))  
    load.fill((255,255,255))
    load.blit(optiona,(40,20))
    load.blit(Totenkopf,(100,100))
    load.blit(Pirat,(230,200))
    load.blit(Anker,(380,300))
    load.blit(Karte,(510,400))
    load.blit(Pistole,(620,520))

    pygame.display.update()
    pygame.time.delay(300)
