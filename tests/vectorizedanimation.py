import sys
import pygame
from pygame import *
import numpy as np

pygame.init()
#set screen size: 
#set some constants
size = width, height = 640, 480
black = 0, 0, 0
screen = pygame.display.set_mode(size)
placeholder=pygame.image.load("intro_ball.gif")#placeholder
placeholderRect=placeholder.get_rect().move(-20,-20)



player=[] #create a list of images
player_rect=[]
move=[]

player.append(pygame.image.load("intro_ball.gif") )
player.append( pygame.image.load("intro_ball.gif"))

#instantiate surfaces.
for n in range(len(player)):
    player_rect.append(player[n].get_rect())

#assign movement
move.append([1,0])
move.append([0,1])

time=0
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit() #standard exit
    
    time+=pygame.time.get_ticks() 
    if time >=30: #set to prevent underrun due to the for loop
        time=0
        screen.fill(black)
        for i in range(len(player)): #for all players
            player_rect[i].move_ip(move[i]) #thsi is much better
            screen.blit(player[i],player_rect[i])           
        temp=placeholderRect.collidelistall(player_rect)
      
        pygame.display.flip() #This then displays all that was drawn(kind of like py.show()?)

