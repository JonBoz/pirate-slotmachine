import pygame, random, time,os
from pygame.locals import *
from settings import *

WIDTH = 800

menu = pygame.display.set_mode((800,600))
PlayButton = pygame.Rect(WIDTH/2 - 195/2, 165, 195, 90)
QuitButton = pygame.Rect(WIDTH/2 - 195/2, 300, 195, 90)


def function_menu():
    pygame.display.update()
    pygame.time.delay(300)
    menu.fill((255,255,255))
    menu.blit(optiona,(40,20))
    menu.blit(optionb,(WIDTH/2-190,100))
    menu.blit(odds1,(5,480))
    menu.blit(odds2,(5,540))
    
    BUTTON_NORMAL = (255, 100, 100)
    TEXTCOLOUR = (0, 0, 0)
    #PlayButton = pygame.Rect(280, 165, 175, 80)
    PlayText = font_smiley.render('PLAY', True, TEXTCOLOUR, None)

    pygame.draw.rect(menu, BUTTON_NORMAL, PlayButton)
    menu.blit(PlayText, (325, 183))
    
    #QuitButton = pygame.Rect(335, 265, 175, 80)
    QuitText = font_smiley.render('QUIT', True, TEXTCOLOUR, None)

    pygame.draw.rect(menu, BUTTON_NORMAL, QuitButton)
    menu.blit(QuitText, (318, 318))  

    pygame.display.update()
    pygame.time.delay(300)

    
