import pygame,sys
from pygame import * 
from pygame.locals import *

#initializations
pygame.init() 
pygame.key.set_repeat(1,10)


size = width, height = 640, 480
black=0, 0, 0
screen = pygame.display.set_mode(size)


player=[] #create a list of images
player_rect=[]
move=[]

player.append(pygame.image.load("intro_ball.gif"))
player_rect.append(player[0].get_rect())
player_rect[0].move([0,0])


while 1: 
    for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player_rect[0].move_ip([-5,0])
                elif event.key == pygame.K_d: 
                    player_rect[0].move_ip([5,0])
                elif event.key == pygame.K_w: 
                    player_rect[0].move_ip([0,-5])
                elif event.key == pygame.K_s: 
                    player_rect[0].move_ip([0,5])
                elif event.key == pygame.K_q: 
                    print ("Quitting....")
                    pygame.quit()
                    sys.exit()
    screen.fill(black)
    screen.blit(player[0],player_rect[0])
    pygame.display.flip()
                   

    