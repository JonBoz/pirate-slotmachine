background_1_filename = '1-p.JPG'
background_2_filename = '2-p.JPG'
background_3_filename = '3-p.JPG'
background_4_filename = '4-p.JPG'
background_5_filename = '5-p.JPG'
background_slot_filename = 'slot.JPG'

import pygame, random, time,os
from pygame.locals import *

def game(screen):

    font1 = pygame.font.Font(os.path.join("Disney.TTF"),36)
    font2 = pygame.font.Font(os.path.join("Disney.TTF"),72)
    font3 = pygame.font.Font(os.path.join("Disney.TTF"),24)
    font4 = pygame.font.Font(os.path.join("Disney.TTF"),60)
    font5 = pygame.font.Font(os.path.join("Smiley.TTF"),72)
    font6 = pygame.font.Font(os.path.join("VeraMoBI.TTF"),24)
    
    winner =font2.render("WINNER",True,(0,0,0))
    loser = font2.render("LOSER ",True,(0,0,0))
    gj = font2.render("GOOD JOB",True,(0,0,0))
    
    odds1 = font6.render(" ODDS TO GET ALL 3 SLOTS IS 4%", True,(0,0,0))
    odds2 = font6.render(" ODDS TO GET AT LEAST 2 SLOTS IS 48%", True , (0,0,0))
        
    image = pygame.Surface((50,50))
    image.fill((255,255,255))
    pygame.draw.circle(image,(0,0,0),(15,15),12)
    
    one = pygame.image.load(background_1_filename).convert()
    two = pygame.image.load(background_2_filename).convert()
    three = pygame.image.load(background_3_filename).convert()
    four = pygame.image.load(background_4_filename).convert()
    five = pygame.image.load(background_5_filename).convert()
    
    slot1 = pygame.image.load(background_slot_filename).convert()
    slot2 = pygame.image.load(background_slot_filename).convert()
    slot3 = pygame.image.load(background_slot_filename).convert()
    
    pos = 1
    
    optiona = font5.render("PIRATE SLOT-MACHINE ",True,(0,0,0))
    optionb = font6.render("use the up and down arrow keys and enter",True,(0,0,0))
    play = font5.render("PLAY" , True,(0,0,0))
    quit = font5.render("QUIT" , True,(0,0,0))  
    
    screen.fill((255,255,255))
    screen.blit(optiona,(40,20))
    screen.blit(one,(100,100))
    screen.blit(two,(230,200))
    screen.blit(three,(380,300))
    screen.blit(four,(510,400))
    screen.blit(five,(620,520))
    
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
                            
                    for roll in xrange(1):
                             p = random.randint(1,5)
                             q = random.randint(1,5)
                             r = random.randint(1,5)
                    
                    if p == 1.:
                        screen.blit(one,(65,100))
                        pygame.display.update()
                        pygame.time.delay(300)
                        if q == 1.:
                            screen.blit(one,(320,100))
                            screen.blit(one,(320,100))
                            pygame.display.update()
                            pygame.time.delay(300)
                            if r == 1.:
                             screen.blit(one,(570,100))
                             pygame.time.delay(150)
                             screen.blit(winner,(250,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 2.:
                             screen.blit(two,(570,100))
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 3.:
                             screen.blit(three,(590,100)) 
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 4.:
                             screen.blit(four,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 5.:
                             screen.blit(five,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)     
                            
                        pygame.time.delay(1000)    
       
                        if q == 2.:
                            screen.blit(two,(315,100))
                            pygame.display.update()
                            pygame.time.delay(300)
                            if r == 1.:
                             screen.blit(one,(570,100))
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(500)
                            if r == 2.:
                             screen.blit(two,(570,100))
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 3.:
                             screen.blit(three,(590,100)) 
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 4.:
                             screen.blit(four,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 5.:
                             screen.blit(five,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                     
                        pygame.time.delay(100) 
                        
                        if q == 3.:
                            screen.blit(three,(340,100))
                            pygame.display.update()
                            pygame.time.delay(300)
                            if r == 1.:
                             screen.blit(one,(570,100))
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 2.:
                             screen.blit(two,(570,100))
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 3.:
                             screen.blit(three,(590,100)) 
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 4.:
                             screen.blit(four,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 5.:
                             screen.blit(five,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update() 
                             pygame.time.delay(300)
                        
                        pygame.time.delay(100) 
                        
                        if q == 4.:
                            screen.blit(four,(320,100))
                            pygame.display.update()
                            pygame.time.delay(300)
                            if r == 1.:
                             screen.blit(one,(570,100))
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 2.:
                             screen.blit(two,(570,100))
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 3.:
                             screen.blit(three,(590,100)) 
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 4.:
                             screen.blit(four,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 5.:
                             screen.blit(five,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            
                        pygame.time.delay(100)     
                            
                        if q == 5.:
                            screen.blit(five,(320,100))
                            pygame.display.update()
                            pygame.time.delay(300)
                            if r == 1.:
                             screen.blit(one,(570,100))
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 2.:
                             screen.blit(two,(570,100))
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 3.:
                             screen.blit(three,(590,100)) 
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 4.:
                             screen.blit(four,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 5.:
                             screen.blit(five,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            
                        pygame.time.delay(100)     
                            
                    if p == 2.:
                        screen.blit(two,(65,100))
                        pygame.display.update()
                        if q == 1.:
                            screen.blit(one,(320,100))
                            pygame.display.update()
                            pygame.time.delay(300)
                            if r == 1.:
                             screen.blit(one,(570,100))
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 2.:
                             screen.blit(two,(570,100))
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 3.:
                             screen.blit(three,(590,100)) 
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 4.:
                             screen.blit(four,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 5.:
                             screen.blit(five,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)  
                            
                        pygame.time.delay(100)     
       
                        if q == 2.:
                            screen.blit(two,(320,100))
                            pygame.display.update()
                            pygame.time.delay(300)
                            if r == 1.:
                             screen.blit(one,(570,100))
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 2.:
                             screen.blit(two,(570,100))
                             pygame.time.delay(150)
                             screen.blit(winner,(250,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 3.:
                             screen.blit(three,(590,100)) 
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 4.:
                             screen.blit(four,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 5.:
                             screen.blit(five,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            
                        pygame.time.delay(100)                     
     
                        if q == 3.:
                            screen.blit(three,(340,100))
                            pygame.display.update()
                            pygame.time.delay(300)
                            if r == 1.:
                             screen.blit(one,(570,100))
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 2.:
                             screen.blit(two,(570,100))
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 3.:
                             screen.blit(three,(590,100)) 
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 4.:
                             screen.blit(four,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 5.:
                             screen.blit(five,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update() 
                             pygame.time.delay(300)
                            
                        pygame.time.delay(100)     
                        
                        if q == 4.:
                            screen.blit(four,(320,100))
                            pygame.display.update()
                            pygame.time.delay(300)
                            if r == 1.:
                             screen.blit(one,(570,100))
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 2.:
                             screen.blit(two,(570,100))
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 3.:
                             screen.blit(three,(590,100)) 
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 4.:
                             screen.blit(four,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 5.:
                             screen.blit(five,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            
                        pygame.time.delay(100)     
                            
                        if q == 5.:
                            screen.blit(five,(320,100))
                            pygame.display.update()
                            pygame.time.delay(300)
                            if r == 1.:
                             screen.blit(one,(570,100))
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 2.:
                             screen.blit(two,(570,100))
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 3.:
                             screen.blit(three,(590,100)) 
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 4.:
                             screen.blit(four,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 5.:
                             screen.blit(five,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300) 
                            
                        pygame.time.delay(100)     

                    if p == 3.:
                        screen.blit(three,(85,100))
                        pygame.display.update()
                        if q == 1.:
                            screen.blit(one,(320,100))
                            pygame.display.update()
                            pygame.time.delay(300)
                            if r == 1.:
                             screen.blit(one,(570,100))
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 2.:
                             screen.blit(two,(570,100))
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 3.:
                             screen.blit(three,(590,100)) 
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 4.:
                             screen.blit(four,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 5.:
                             screen.blit(five,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)    
                            
                        pygame.time.delay(100)
                        
                        if q == 2.:
                            screen.blit(two,(320,100))
                            pygame.display.update()
                            pygame.time.delay(300)
                            if r == 1.:
                             screen.blit(one,(570,100))
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 2.:
                             screen.blit(two,(570,100))
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 3.:
                             screen.blit(three,(590,100)) 
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 4.:
                             screen.blit(four,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 5.:
                             screen.blit(five,(570,100))
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            
                        pygame.time.delay(100)                     
     
                        if q == 3.:
                            screen.blit(three,(340,100))
                            pygame.display.update()
                            pygame.time.delay(300)
                            if r == 1.:
                             screen.blit(one,(570,100))
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 2.:
                             screen.blit(two,(570,100))
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 3.:
                             screen.blit(three,(590,100)) 
                             pygame.time.delay(150)
                             screen.blit(winner,(250,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 4.:
                             screen.blit(four,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 5.:
                             screen.blit(five,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update() 
                             pygame.time.delay(300)
                            
                        pygame.time.delay(100)     
                        
                        if q == 4.:
                            screen.blit(four,(320,100))
                            pygame.display.update()
                            pygame.time.delay(300)
                            if r == 1.:
                             screen.blit(one,(570,100))
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 2.:
                             screen.blit(two,(570,100))
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 3.:
                             screen.blit(three,(590,100)) 
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 4.:
                             screen.blit(four,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 5.:
                             screen.blit(five,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            
                        pygame.time.delay(100)     
                            
                        if q == 5.:
                            screen.blit(five,(320,100))
                            pygame.display.update()
                            pygame.time.delay(300)
                            if r == 1.:
                             screen.blit(one,(570,100))
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 2.:
                             screen.blit(two,(570,100))
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 3.:
                             screen.blit(three,(590,100)) 
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 4.:
                             screen.blit(four,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 5.:
                             screen.blit(five,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            
                        pygame.time.delay(100)     

                    if p == 4.:
                        screen.blit(four,(65,100))
                        pygame.display.update()
                        if q == 1.:
                            screen.blit(one,(320,100))
                            pygame.display.update()
                            pygame.time.delay(300)
                            if r == 1.:
                             screen.blit(one,(570,100))
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 2.:
                             screen.blit(two,(570,100))
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 3.:
                             screen.blit(three,(590,100)) 
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 4.:
                             screen.blit(four,(570,100)) 
                             pygame.display.update()
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.time.delay(300)
                            if r == 5.:
                             screen.blit(five,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)  
                            
                        pygame.time.delay(100)     
       
                        if q == 2.:
                            screen.blit(two,(320,100))
                            pygame.display.update()
                            pygame.time.delay(300)
                            if r == 1.:
                             screen.blit(one,(570,100))
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 2.:
                             screen.blit(two,(570,100))
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 3.:
                             screen.blit(three,(590,100)) 
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 4.:
                             screen.blit(four,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 5.:
                             screen.blit(five,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            
                        pygame.time.delay(100)                     
     
                        if q == 3.:
                            screen.blit(three,(340,100))
                            pygame.display.update()
                            pygame.time.delay(300)
                            if r == 1.:
                             screen.blit(one,(570,100))
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 2.:
                             screen.blit(two,(570,100))
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 3.:
                             screen.blit(three,(590,100)) 
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 4.:
                             screen.blit(four,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 5.:
                             screen.blit(five,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update() 
                             pygame.time.delay(300)
                            
                        pygame.time.delay(100)     
                        
                        if q == 4.:
                            screen.blit(four,(320,100))
                            pygame.display.update()
                            pygame.time.delay(300)
                            if r == 1.:
                             screen.blit(one,(570,100))
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 2.:
                             screen.blit(two,(570,100))
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 3.:
                             screen.blit(three,(590,100)) 
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 4.:
                             screen.blit(four,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(winner,(250,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 5.:
                             screen.blit(five,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            
                        pygame.time.delay(100)     
                            
                        if q == 5.:
                            screen.blit(five,(320,100))
                            pygame.display.update()
                            pygame.time.delay(300)
                            if r == 1.:
                             screen.blit(one,(570,100))
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 2.:
                             screen.blit(two,(570,100))
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 3.:
                             screen.blit(three,(590,100)) 
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 4.:
                             screen.blit(four,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 5.:
                             screen.blit(five,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            
                        pygame.time.delay(100)     
                    
                    if p == 5.:
                        screen.blit(five,(65,100))
                        pygame.display.update()
                        if q == 1.:
                            screen.blit(one,(320,100))
                            pygame.display.update()
                            pygame.time.delay(300)
                            if r == 1.:
                             screen.blit(one,(570,100))
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 2.:
                             screen.blit(two,(570,100))
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 3.:
                             screen.blit(three,(590,100)) 
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 4.:
                             screen.blit(four,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 5.:
                             screen.blit(five,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)   
                            
                        pygame.time.delay(100)     
       
                        if q == 2.:
                            screen.blit(two,(320,100))
                            pygame.display.update()
                            pygame.time.delay(300)
                            if r == 1.:
                             screen.blit(one,(570,100))
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 2.:
                             screen.blit(two,(570,100))
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 3.:
                             screen.blit(three,(590,100)) 
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 4.:
                             screen.blit(four,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 5.:
                             screen.blit(five,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            
                        pygame.time.delay(100)                      
     
                        if q == 3.:
                            screen.blit(three,(340,100))
                            pygame.display.update()
                            pygame.time.delay(300)
                            if r == 1.:
                             screen.blit(one,(570,100))
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 2.:
                             screen.blit(two,(570,100))
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 3.:
                             screen.blit(three,(590,100)) 
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 4.:
                             screen.blit(four,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 5.:
                             screen.blit(five,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update() 
                             pygame.time.delay(300)
                            
                        pygame.time.delay(100)     
                        
                        if q == 4.:
                            screen.blit(four,(320,100))
                            pygame.display.update()
                            pygame.time.delay(300)
                            if r == 1.:
                             screen.blit(one,(570,100))
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 2.:
                             screen.blit(two,(570,100))
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 3.:
                             screen.blit(three,(590,100)) 
                             pygame.time.delay(150)
                             screen.blit(loser,(270,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 4.:
                             screen.blit(four,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 5.:
                             screen.blit(five,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            
                        pygame.time.delay(100)     
                            
                        if q == 5.:
                            screen.blit(five,(320,100))
                            pygame.display.update()
                            pygame.time.delay(300)
                            if r == 1.:
                             screen.blit(one,(570,100))
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 2.:
                             screen.blit(two,(570,100))
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 3.:
                             screen.blit(three,(590,100)) 
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 4.:
                             screen.blit(four,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(gj,(200,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            if r == 5.:
                             screen.blit(five,(570,100)) 
                             pygame.time.delay(150)
                             screen.blit(winner,(250,480))
                             pygame.display.update()
                             pygame.time.delay(300)
                            
                        pygame.time.delay(100)     
                            
        pygame.time.delay(1000)                                
        pygame.display.update()                 
                    








