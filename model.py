'''
model.py

This is to demonstrate that you can extend unit() class in inheiritance. 
Modifiable methods include 'oncollision' and 'ontimepass'. 

On collision is called when the unit collides, while ontimepass
occurs when passtime is called. 

Remember that the attribute 'speed', is how quickly the unit is moved
everytime the move method is called. 

'''

from src.utils import *
import random


# a model in which message passing will allow the neurons pass the highest color

class model_unit(unit): 
    def __init__(self,screen,startpos, radii=10.0):
        super().__init__(screen,startpos=startpos,radii=radii)
        #declare what to do on collision.
        self.oncollision=self.collideLogic
        #declare what happens when time passes.
        self.ontimepass=self.dostuff
        self.time=0 #other variables. 
        self.age=0 #other variables
        
        ### Randomize their starting movement direction.
        ranspeedx=random.random()*random.randint(-1,1)
        ranspeedy=random.random()*random.randint(-1,1)
        self.speed=[ranspeedx,ranspeedy] 
        #randomize colors
        self.color=[0,0,random.randint(0,255)]

    def collideLogic(self):

        #assuming it's a real collision.
        self.speed[0]=self.speed[0]*-1
        self.speed[1]=self.speed[1]*-1
       
    def dostuff(self): 
        self.time+=1 
        #changes color overtime.
        if self.time>=1000: #remember time here is no ms, it's by number of times this function is called. 
            self.age+=1
            self.time=0
            if self.color[2]-1 >=100:
                self.color[2] =self.color[2]-0.1
                self.color[1] =self.color[1]+0.1
        
        #code to detect the edge of the screen.
        if self.position[0]<=1 or self.position[0]>=self.surface.get_size()[0]:
            self.speed[0]*=-1
        if self.position[1]<=1 or self.position[1]>=self.surface.get_size()[1]:
            self.speed[1]*=-1
            

        

        