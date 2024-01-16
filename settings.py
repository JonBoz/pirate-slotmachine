import pygame
import pygame, random, time,os
from pygame.locals import *
#pygame.init()

background_slot_filename = 'slot.JPG'
Totenkopf = '1-p.JPG'
Pirat = "2-p.JPG"
Anker = "3-p.JPG"
Karte = "4-p.JPG"
Pistole = "5-p.JPG"

one = pygame.image.load(os.path.join('symbols', Totenkopf)).convert()
two = pygame.image.load(os.path.join('symbols', Pirat)).convert()
three = pygame.image.load(os.path.join('symbols', Anker)).convert()
four = pygame.image.load(os.path.join('symbols', Karte)).convert()
five = pygame.image.load(os.path.join('symbols', Pistole)).convert()