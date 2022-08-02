'''
model2.py

utils.unit is how one can draw and instiatiate an agent to present
It is assumed that in order to add functionality, you will 
subclass. 

Below is subclass of utils.unit, adding functions specifically related 
to collisions, logic etc....


This is same as model.py, but  for model2 I will demonstrate communication

'''

from src.utils import *
import random


# a model in which message passing will allow the neurons pass the highest color

class model_unit_communication(unit): 
    def __init__(self,screen,startpos, radii=10.0,name='none'):
        super().__init__(screen,startpos=startpos,radii=radii,name=name)
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

        propercollisions=[x for x in self.allCollisions if x!=int(self.name)]
        mess=str(self.name) + ' collided with ' + str(propercollisions)
        #remember create_message for now only can deal with one colliions and one message 
        #TODO : check utils.py under create_message
        self.create_message(str(propercollisions[0]),mess)


#This is what is done overtime. 
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
            

        

        