import sys, pygame
from pygame import *

pygame.init() 
size = width, height = 640, 480 #set the window height and width.
speed = [2, 2] #arbitrary code here?
black = 0, 0, 0
screen = pygame.display.set_mode(size) #instnatiate the screen, 

def draw_object(position):
    circle=pygame.draw.circle(screen,[0,0,255],)


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit() #standard exit
    
    
    pygame.draw.circle(screen,[0,0,255],[10,10],100)
    pygame.display.flip()
    pygame.display.update()