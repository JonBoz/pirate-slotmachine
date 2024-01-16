

import pygame, random, time,os
from pygame.locals import *
from settings import *
from loadingscreen import loadingscreen



def game(screen):
    
    image = pygame.Surface((50,50))
    image.fill((255,255,255))
    pygame.draw.circle(image,(0,0,0),(15,15),12)
    
    pos = 1
    

    loadingscreen()
    
    pygame.display.update()
    pygame.time.delay(3000)
           
    while 1:
        screen.fill((255,255,255))
        screen.blit(optiona,(40,20))
        screen.blit(optionb,(110,100))
        screen.blit(odds1,(5,480))
        screen.blit(odds2,(5,540))
        screen.blit(play,(350,180))
        screen.blit(quit,(350,380))
              
        screen.blit(image,(300,pos*200))       

        for event in pygame.event.get():
           if event.type == QUIT:
               exit()
               
           elif event.type == KEYDOWN:
               if event.key == K_ESCAPE:
                 exit() 
               elif event.key == K_DOWN:
                  pos += 1
                  if pos > 2: pos = 1
               elif event.key == K_UP:
                    pos -= 1
                    if pos < 1: pos = 2
                    
               elif event.key == K_RETURN:
                
                    if pos == 2.:  
                       exit()
                
                    if pos == 1.:
                            screen.fill((255,255,255))
                            screen.blit(slot1,(50,40))
                            screen.blit(slot2,(300,40))
                            screen.blit(slot3,(550,40))
                            pygame.display.update()
                            pygame.time.delay(600)
                            
                    for roll in range(1):
                             p = random.randint(1,5)
                             q = random.randint(1,5)
                             r = random.randint(1,5)
                    
                    if p == 1.:
                        screen.blit(Totenkopf,(65,100))
                        pygame.display.update()
                        pygame.time.delay(300)
                        if q == 1.:
                            screen.blit(Totenkopf,(320,100))
                            screen.blit(Totenkopf,(320,100))
                            pygame.display.update()
                            pygame.time.delay(300)
                            if r == 1.:
                             screen.blit(Totenkopf,(570,100))
                             pygame.time.delay(150)
                             screen.blit(winner,(250,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 2.:
                             screen.blit(Pirat,(570,100))
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 3.:
                             screen.blit(Anker,(590,100)) 
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 4.:
                             screen.blit(Karte,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 5.:
                             screen.blit(Pistole,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)     
                            
                        pygame.time.delay(1000)    
       
                        if q == 2.:
                            screen.blit(Pirat,(315,100))
                            pygame.display.update()
                            pygame.time.delay(300)
                            if r == 1.:
                             screen.blit(Totenkopf,(570,100))
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(500)
                            if r == 2.:
                             screen.blit(Pirat,(570,100))
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 3.:
                             screen.blit(Anker,(590,100)) 
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 4.:
                             screen.blit(Karte,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 5.:
                             screen.blit(Pistole,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                     
                        pygame.time.delay(100) 
                        
                        if q == 3.:
                            screen.blit(Anker,(340,100))
                            pygame.display.update()
                            pygame.time.delay(300)
                            if r == 1.:
                             screen.blit(Totenkopf,(570,100))
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 2.:
                             screen.blit(Pirat,(570,100))
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 3.:
                             screen.blit(Anker,(590,100)) 
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 4.:
                             screen.blit(Karte,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 5.:
                             screen.blit(Pistole,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update() 
                             pygame.time.delay(300)
                        
                        pygame.time.delay(100) 
                        
                        if q == 4.:
                            screen.blit(Karte,(320,100))
                            pygame.display.update()
                            pygame.time.delay(300)
                            if r == 1.:
                             screen.blit(Totenkopf,(570,100))
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 2.:
                             screen.blit(Pirat,(570,100))
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 3.:
                             screen.blit(Anker,(590,100)) 
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 4.:
                             screen.blit(Karte,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 5.:
                             screen.blit(Pistole,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            
                        pygame.time.delay(100)     
                            
                        if q == 5.:
                            screen.blit(Pistole,(320,100))
                            pygame.display.update()
                            pygame.time.delay(300)
                            if r == 1.:
                             screen.blit(Totenkopf,(570,100))
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 2.:
                             screen.blit(Pirat,(570,100))
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 3.:
                             screen.blit(Anker,(590,100)) 
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 4.:
                             screen.blit(Karte,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 5.:
                             screen.blit(Pistole,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            
                        pygame.time.delay(100)     
                            
                    if p == 2.:
                        screen.blit(Pirat,(65,100))
                        pygame.display.update()
                        if q == 1.:
                            screen.blit(Totenkopf,(320,100))
                            pygame.display.update()
                            pygame.time.delay(300)
                            if r == 1.:
                             screen.blit(Totenkopf,(570,100))
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 2.:
                             screen.blit(Pirat,(570,100))
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 3.:
                             screen.blit(Anker,(590,100)) 
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 4.:
                             screen.blit(Karte,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 5.:
                             screen.blit(Pistole,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)  
                            
                        pygame.time.delay(100)     
       
                        if q == 2.:
                            screen.blit(Pirat,(320,100))
                            pygame.display.update()
                            pygame.time.delay(300)
                            if r == 1.:
                             screen.blit(Totenkopf,(570,100))
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 2.:
                             screen.blit(Pirat,(570,100))
                             pygame.time.delay(150)
                             screen.blit(winner,(250,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 3.:
                             screen.blit(Anker,(590,100)) 
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 4.:
                             screen.blit(Karte,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 5.:
                             screen.blit(Pistole,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            
                        pygame.time.delay(100)                     
     
                        if q == 3.:
                            screen.blit(Anker,(340,100))
                            pygame.display.update()
                            pygame.time.delay(300)
                            if r == 1.:
                             screen.blit(Totenkopf,(570,100))
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 2.:
                             screen.blit(Pirat,(570,100))
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 3.:
                             screen.blit(Anker,(590,100)) 
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 4.:
                             screen.blit(Karte,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 5.:
                             screen.blit(Pistole,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update() 
                             pygame.time.delay(300)
                            
                        pygame.time.delay(100)     
                        
                        if q == 4.:
                            screen.blit(Karte,(320,100))
                            pygame.display.update()
                            pygame.time.delay(300)
                            if r == 1.:
                             screen.blit(Totenkopf,(570,100))
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 2.:
                             screen.blit(Pirat,(570,100))
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 3.:
                             screen.blit(Anker,(590,100)) 
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 4.:
                             screen.blit(Karte,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 5.:
                             screen.blit(Pistole,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            
                        pygame.time.delay(100)     
                            
                        if q == 5.:
                            screen.blit(Pistole,(320,100))
                            pygame.display.update()
                            pygame.time.delay(300)
                            if r == 1.:
                             screen.blit(Totenkopf,(570,100))
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 2.:
                             screen.blit(Pirat,(570,100))
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 3.:
                             screen.blit(Anker,(590,100)) 
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 4.:
                             screen.blit(Karte,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 5.:
                             screen.blit(Pistole,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300) 
                            
                        pygame.time.delay(100)     

                    if p == 3.:
                        screen.blit(Anker,(85,100))
                        pygame.display.update()
                        if q == 1.:
                            screen.blit(Totenkopf,(320,100))
                            pygame.display.update()
                            pygame.time.delay(300)
                            if r == 1.:
                             screen.blit(Totenkopf,(570,100))
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 2.:
                             screen.blit(Pirat,(570,100))
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 3.:
                             screen.blit(Anker,(590,100)) 
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 4.:
                             screen.blit(Karte,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 5.:
                             screen.blit(Pistole,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)    
                            
                        pygame.time.delay(100)
                        
                        if q == 2.:
                            screen.blit(Pirat,(320,100))
                            pygame.display.update()
                            pygame.time.delay(300)
                            if r == 1.:
                             screen.blit(Totenkopf,(570,100))
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 2.:
                             screen.blit(Pirat,(570,100))
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 3.:
                             screen.blit(Anker,(590,100)) 
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 4.:
                             screen.blit(Karte,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 5.:
                             screen.blit(Pistole,(570,100))
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            
                        pygame.time.delay(100)                     
     
                        if q == 3.:
                            screen.blit(Anker,(340,100))
                            pygame.display.update()
                            pygame.time.delay(300)
                            if r == 1.:
                             screen.blit(Totenkopf,(570,100))
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 2.:
                             screen.blit(Pirat,(570,100))
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 3.:
                             screen.blit(Anker,(590,100)) 
                             pygame.time.delay(150)
                             screen.blit(winner,(250,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 4.:
                             screen.blit(Karte,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 5.:
                             screen.blit(Pistole,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update() 
                             pygame.time.delay(300)
                            
                        pygame.time.delay(100)     
                        
                        if q == 4.:
                            screen.blit(Karte,(320,100))
                            pygame.display.update()
                            pygame.time.delay(300)
                            if r == 1.:
                             screen.blit(Totenkopf,(570,100))
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 2.:
                             screen.blit(Pirat,(570,100))
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 3.:
                             screen.blit(Anker,(590,100)) 
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 4.:
                             screen.blit(Karte,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 5.:
                             screen.blit(Pistole,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            
                        pygame.time.delay(100)     
                            
                        if q == 5.:
                            screen.blit(Pistole,(320,100))
                            pygame.display.update()
                            pygame.time.delay(300)
                            if r == 1.:
                             screen.blit(Totenkopf,(570,100))
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 2.:
                             screen.blit(Pirat,(570,100))
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 3.:
                             screen.blit(Anker,(590,100)) 
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 4.:
                             screen.blit(Karte,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 5.:
                             screen.blit(Pistole,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            
                        pygame.time.delay(100)     

                    if p == 4.:
                        screen.blit(Karte,(65,100))
                        pygame.display.update()
                        if q == 1.:
                            screen.blit(Totenkopf,(320,100))
                            pygame.display.update()
                            pygame.time.delay(300)
                            if r == 1.:
                             screen.blit(Totenkopf,(570,100))
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 2.:
                             screen.blit(Pirat,(570,100))
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 3.:
                             screen.blit(Anker,(590,100)) 
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 4.:
                             screen.blit(Karte,(570,100)) 
                             pygame.display.update()
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.time.delay(300)
                            if r == 5.:
                             screen.blit(Pistole,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)  
                            
                        pygame.time.delay(100)     
       
                        if q == 2.:
                            screen.blit(Pirat,(320,100))
                            pygame.display.update()
                            pygame.time.delay(300)
                            if r == 1.:
                             screen.blit(Totenkopf,(570,100))
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 2.:
                             screen.blit(Pirat,(570,100))
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 3.:
                             screen.blit(Anker,(590,100)) 
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 4.:
                             screen.blit(Karte,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 5.:
                             screen.blit(Pistole,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            
                        pygame.time.delay(100)                     
     
                        if q == 3.:
                            screen.blit(Anker,(340,100))
                            pygame.display.update()
                            pygame.time.delay(300)
                            if r == 1.:
                             screen.blit(Totenkopf,(570,100))
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 2.:
                             screen.blit(Pirat,(570,100))
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 3.:
                             screen.blit(Anker,(590,100)) 
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 4.:
                             screen.blit(Karte,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 5.:
                             screen.blit(Pistole,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update() 
                             pygame.time.delay(300)
                            
                        pygame.time.delay(100)     
                        
                        if q == 4.:
                            screen.blit(Karte,(320,100))
                            pygame.display.update()
                            pygame.time.delay(300)
                            if r == 1.:
                             screen.blit(Totenkopf,(570,100))
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 2.:
                             screen.blit(Pirat,(570,100))
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 3.:
                             screen.blit(Anker,(590,100)) 
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 4.:
                             screen.blit(Karte,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(winner,(250,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 5.:
                             screen.blit(Pistole,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            
                        pygame.time.delay(100)     
                            
                        if q == 5.:
                            screen.blit(Pistole,(320,100))
                            pygame.display.update()
                            pygame.time.delay(300)
                            if r == 1.:
                             screen.blit(Totenkopf,(570,100))
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 2.:
                             screen.blit(Pirat,(570,100))
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 3.:
                             screen.blit(Anker,(590,100)) 
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 4.:
                             screen.blit(Karte,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 5.:
                             screen.blit(Pistole,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            
                        pygame.time.delay(100)     
                    
                    if p == 5.:
                        screen.blit(Pistole,(65,100))
                        pygame.display.update()
                        if q == 1.:
                            screen.blit(Totenkopf,(320,100))
                            pygame.display.update()
                            pygame.time.delay(300)
                            if r == 1.:
                             screen.blit(Totenkopf,(570,100))
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 2.:
                             screen.blit(Pirat,(570,100))
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 3.:
                             screen.blit(Anker,(590,100)) 
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 4.:
                             screen.blit(Karte,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 5.:
                             screen.blit(Pistole,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)   
                            
                        pygame.time.delay(100)     
       
                        if q == 2.:
                            screen.blit(Pirat,(320,100))
                            pygame.display.update()
                            pygame.time.delay(300)
                            if r == 1.:
                             screen.blit(Totenkopf,(570,100))
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 2.:
                             screen.blit(Pirat,(570,100))
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 3.:
                             screen.blit(Anker,(590,100)) 
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 4.:
                             screen.blit(Karte,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 5.:
                             screen.blit(Pistole,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            
                        pygame.time.delay(100)                      
     
                        if q == 3.:
                            screen.blit(Anker,(340,100))
                            pygame.display.update()
                            pygame.time.delay(300)
                            if r == 1.:
                             screen.blit(Totenkopf,(570,100))
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 2.:
                             screen.blit(Pirat,(570,100))
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 3.:
                             screen.blit(Anker,(590,100)) 
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 4.:
                             screen.blit(Karte,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 5.:
                             screen.blit(Pistole,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update() 
                             pygame.time.delay(300)
                            
                        pygame.time.delay(100)     
                        
                        if q == 4.:
                            screen.blit(Karte,(320,100))
                            pygame.display.update()
                            pygame.time.delay(300)
                            if r == 1.:
                             screen.blit(Totenkopf,(570,100))
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 2.:
                             screen.blit(Pirat,(570,100))
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 3.:
                             screen.blit(Anker,(590,100)) 
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 4.:
                             screen.blit(Karte,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 5.:
                             screen.blit(Pistole,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            
                        pygame.time.delay(100)     
                            
                        if q == 5.:
                            screen.blit(Pistole,(320,100))
                            pygame.display.update()
                            pygame.time.delay(300)
                            if r == 1.:
                             screen.blit(Totenkopf,(570,100))
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 2.:
                             screen.blit(Pirat,(570,100))
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 3.:
                             screen.blit(Anker,(590,100)) 
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 4.:
                             screen.blit(Karte,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 5.:
                             screen.blit(Pistole,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(winner,(250,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            
                        pygame.time.delay(100)     
                            
        pygame.time.delay(1000)                                
        pygame.display.update()                 
                    








