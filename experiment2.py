'''
Expermiment2.py
practicing sending messages aronud. 

IN this experiment a set of units are instantiated, upon collision
only the units who experience a collision will send a message. 
This is O(c*N_collisions) complexcity, where N_collisions is number of collisions
where each of the unit participating in the collision (c) sends a message. 


On the message retrieval step, all units will search for messages in a process
that is O(N) complexity, where N = total units. 

'''

import pygame,sys
from src.utils import *
from src.channel import *

from model2 import *
import random

pygame.init() #initialize the pygame class
size = width, height = 640, 480 #set the window height and width.
black =[0, 0, 0]

screen = pygame.display.set_mode(size)

#instnatiate many units
units=[]
startx=random.sample(range(100,600),200)
starty=random.sample(range(100,600),200)

channel=Channel() #instnatiate channel. 

for i in range(200):
    units.append(model_unit_communication(screen,startpos=[startx[i],starty[i]],radii=5,name=str(i)))

#All units by default will have no speed. 

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
        
        
