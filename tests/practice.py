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
player_rect =player.get_rect() 
screen = pygame.display.set_mode(size)


player_rect.move_ip([50,10])
time=0
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit() #standard exit
    
    time+=pygame.time.get_ticks() 
    if time >=16:
        time=0
        screen.fill(black)
        screen.blit(player,player_rect)
        player_rect.move_ip([1,1]) #thsi is much better
        pygame.display.flip() #This then displays all that was drawn(kind of like py.show()?)


        
