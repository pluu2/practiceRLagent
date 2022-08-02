'''
RLagent.py

This subclass of utils.unit, will allow RL to be performed on these units. 

Design: 
- Agent will have a collision method between the walls and other units. 
- What will be different is that the 'ontimepass' attribute willcontain 
    method by which the agent will collect the enviroment state and it's own state. 
    For RL I will 



'''

from src.utils import *
import random


# a model in which message passing will allow the neurons pass the highest color

class RL_agent(unit): 
    def __init__(self,screen,startpos, radii=10.0,name='none'):
        super().__init__(screen,startpos=startpos,radii=radii,name=name)
        #declare what to do on collision.
        self.oncollision=self.collideLogic
        #declare what happens when time passes.
        self.ontimepass=self.process
        self.time=0 #other variables. 
        self.age=0 #other variables
        
        self.propercollisions =0 #new variable to contain all proper collisions (ie: not including itself)

        
        ### Randomize their starting movement direction.
        ranspeedx=random.random()*random.randint(-1,1)
        ranspeedy=random.random()*random.randint(-1,1)
        self.speed=[ranspeedx,ranspeedy] 
        
        
        
        #randomize colors
        self.color=[0,0,random.randint(0,255)]

#Most likely the collide logic is where we will collect data. 

    def collideLogic(self):

        #assuming it's a real collision.
        self.speed[0]=self.speed[0]*-1
        self.speed[1]=self.speed[1]*-1

        #exclude self collisions.
        propercollisions=[x for x in self.allCollisions if x!=int(self.name)]

        self.propercollisions=propercollisions 
        
        #sends messages only if collides.
        if 0 in propercollisions:
            #send out a message, for RL the agent just has to say it collided with [0]
            mess=str(self.name) + ' : '+ str(0)#str(propercollisions)
            
        #remember create_message for now only can deal with one colliions and one message 
        #NEED to code to broad cast. 
        #TODO : check    utils.py under create_message
            self.create_message('broadcast',mess)


#This is what is done overtime. This is where data is collected. 

#For the RL agent this is where the AI is coded. The agent will collect information of the enviroment. 


    def process(self): 
        '''
        gather:
        inputs:
         self.position[0] and self.position[1] - contains positions
         self.speed[0], self.speed[1] -contains delta x, and y
         self.propercollisions contains all collisions, but just check if the target was hit. (value is 0 or 1? )
            I suspect there may be an issue if the network returns large changes. (ie: Breaches lipshitz continuity/non-smooth manifold.)
        
        output: action

        loss function: reward? 

         
         
        

        
        '''
        
        network_inputs[0]
        


        #print('u1: ,', self.inbox)



    
        



        #code to detect the edge of the screen.
        if self.position[0]<=1 or self.position[0]>=self.surface.get_size()[0]:
            self.speed[0]*=-1
        if self.position[1]<=1 or self.position[1]>=self.surface.get_size()[1]:
            self.speed[1]*=-1
            
