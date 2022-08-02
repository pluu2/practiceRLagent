import sys
import pygame
from pygame import *
import numpy as np

pygame.init()
#set screen size: 
#set some constants
size = width, height = 640, 480
black = 0, 0, 0


player = pygame.image.load("intro_ball.gif") 
player2= pygame.image.load("intro_ball.gif")


player_rect =player.get_rect() 
player2_rect=player2.get_rect() 

screen = pygame.display.set_mode(size)


#player_rect.move_ip([50,10])
time=0
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit() #standard exit
    
    time+=pygame.time.get_ticks() 
    if time >=16: #60 FPS
        time=0
        screen.fill(black)
        player_rect.move_ip([1,0]) #thsi is much better
        player2_rect.move_ip([0,1]) #thsi is much better
        screen.blit(player,player_rect)   
        screen.blit(player2,player2_rect)
        pygame.display.flip() #This then displays all that was drawn(kind of like py.show()?)

