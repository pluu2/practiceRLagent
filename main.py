import pygame,sys
from src.utils import *
from model import *
import random

pygame.init() #initialize the pygame class
size = width, height = 640, 480 #set the window height and width.
black =[0, 0, 0]

screen = pygame.display.set_mode(size)

#instnatiate many units
units=[]
startx=random.sample(range(100,600),200)
starty=random.sample(range(100,600),200)

for i in range(200):
    units.append(model_unit(screen,startpos=[startx[i],starty[i]],radii=5))

 #for all units do something set random speed. 
 
for un in units: 
    ranspeedx=random.random()*random.randint(-1,1)
    ranspeedy=random.random()*random.randint(-1,1)
    un.set_speed([ranspeedx,ranspeedy])


time=0
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    time+=pygame.time.get_ticks() 
    if time >=60: #set to prevent underrun due to the for loop
        time=0
        screen.fill(black)
        
        #run whatever funcion occurs in passtime.
        for un in units: 
            un.passtime()


        #for all units, register, detect collisions, then 
       
        
        other_units=[]
        for un in units:
            other_units.append(un.register()) 
        #use this list of rects for each unit to detect
        for n,un in enumerate(units): 
            un.collisions(n,other_units)

        pygame.display.flip()
        pygame.display.update()
        
        for un in units:
            un.move()
        
        
