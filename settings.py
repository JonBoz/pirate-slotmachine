import pygame, random, time,os
from pygame.locals import *

#Bilder
background_slot_filename = 'slot.JPG'

Totenkopf = pygame.image.load(os.path.join('symbols', '1-p.JPG')).convert()
Pirat = pygame.image.load(os.path.join('symbols', "2-p.JPG")).convert()
Anker = pygame.image.load(os.path.join('symbols', "3-p.JPG")).convert()
Karte = pygame.image.load(os.path.join('symbols', "4-p.JPG")).convert()
Pistole = pygame.image.load(os.path.join('symbols', "5-p.JPG")).convert()
#slotbilder
slot1 = pygame.image.load(background_slot_filename).convert()
slot2 = pygame.image.load(background_slot_filename).convert()
slot3 = pygame.image.load(background_slot_filename).convert()


#Designs
font_smiley = pygame.font.Font(os.path.join('fonts', "Smiley.ttf"),72)
font_vera = pygame.font.Font(os.path.join('fonts', "VeraMoBI.TTF"),24)
font1 = pygame.font.Font(os.path.join('fonts', "Disney.TTF"),36)
font2 = pygame.font.Font(os.path.join('fonts', "Disney.TTF"),72)
font3 = pygame.font.Font(os.path.join('fonts', "Disney.TTF"),24)
font4 = pygame.font.Font(os.path.join('fonts', "Disney.TTF"),60)


#Ingame text
#ergebnis
winner = font2.render("WINNER",True,(0,0,0))
loser = font2.render("LOSER ",True,(0,0,0))
gj = font2.render("GOOD JOB",True,(0,0,0))
#wahrscheinlichkeiten
odds1 = font_vera.render(" ODDS TO GET ALL 3 SLOTS IS 4%", True,(0,0,0))
odds2 = font_vera.render(" ODDS TO GET AT LEAST 2 SLOTS IS 48%", True , (0,0,0))


optiona = font_smiley.render("PIRATE SLOT-MACHINE ",True,(0,0,0))
optionb = font_vera.render("use the up and down arrow keys and enter",True,(0,0,0))
play = font_smiley.render("PLAY" , True,(0,0,0))
quit = font_smiley.render("QUIT" , True,(0,0,0))

