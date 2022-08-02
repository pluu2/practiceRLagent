'''
This will represent the enviroment for which the agents will exist in. 

In this task, agents will mill around, and then attempt 
to communicate 
'''
import pygame,sys
from src.utils import *
from src.channel import *

from RLagent import *
import random

pygame.init() #initialize the pygame class
size = width, height = 740, 580 #set the window height and width.
black =[0, 0, 0]

screen = pygame.display.set_mode(size)

#instnatiate many units
units=[]
startx=random.sample(range(100,600),200)
starty=random.sample(range(100,600),200)

channel=Channel() #instnatiate channel. 


for i in range(40):
    units.append(RL_agent(screen,startpos=[startx[i],starty[i]],radii=5,name=str(i)))

#unit[0] will be the target. 
units[0].name='0'
units[0].color=[255,255,255]
units[0].radii=10
units[0].speed=[0,0]


'''
Within a time step the following things needs to happen: 
1) Passtime:
    which is an event where  function that runs when nothing happens, or happens
    each time step 
2) Collision Detection:
    utilizs the 'register' method, which draws the unit and also returns if collision occurs. 
    The method is that on a collision detection, a list of objects that have undergone a collision is collected.
    The unit itself stores the other unit it collided with. 
3) Registering collisions - 
    The units are then handed a list of the other units they collided into. 
    This uses utils.unit.collisions() method 
4) The Units can post messages to channel() class. 
5) The units can retrieve messages in chanel() class. 

'''

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

        
        #to detect collisions, and by reunning un.register, it 
        #actually updates all other units. 
        other_units=[]
        for un in units:
            other_units.append(un.register()) 
        
        #use this list of rects for each unit to detect
        for n,un in enumerate(units): 
            un.collisions(n,other_units)

        #send messages
        for un in units: 
            un.send_message(channel)
        #retrieve messages
        for un in units:
            un.retrieve_message(channel)
        
        #print(channel.messages)

        pygame.display.flip()
        pygame.display.update()
        
        for un in units:
            un.move()
        