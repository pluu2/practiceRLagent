#this is the basic unit, which will contain movement and drawing
"""
Attributes:
name:string (default 'None')
    Specify the name of unit as a string. Required for communication.

surface : pygame.surface 
     Specify the surface the unit has to be draw to.
color : tuple
    Specify the color of the unit [r,g,b] (default is 0,0,255)
startpos: tuple
    Specify the start position of the unit [x,y] (default 0,0)
radii: int
    Specifies the radii (default is 10)
object: pygame.draw.circle
    pygame rect location, represents the location of the unit.
collided:boolean
    Indicates whether or not the object has collided with something.

speed: tuple: (default is [0,0])
    Speed in which the object will move everytime unit.move() is called

allCollisions:list (default is 0)
    attribute that stores all collisions.



COMMUNICATION ATTRIBUTES: 
message:list (default is empty): 
    contains all the messages to be sent.

recipients:list (default is empty): 
    contains all the receipients of messages. 

inbox:list(default is empty): 
    contains all the retrieved messages.


INTERACTION ATTRIBUTES: 
Assign methods to these following attributes to determine how unit 
will respond to certain stimuli. 

oncollision:obj
    Function to be run when a collision is detected. 
ontimepass:obj
    Function to be run when a frame passes. Can be used to gather 
    information. 




Methods: 
register(self)
    will draw the unit circle to the objects Attributes to the specified surface
    In addition, it will return the rect of the drawn object for collision detection.

move(self)
    will move the unit by [x,y] units as defined by speed attrribute. 
    
passtime(self)
    runs method found in the attribute ontimepass

collisions(self,self_id : int,other_objects : list)
    return a list of collided objects. 
    This is done using pygame.collidelistall(), which check if
    a current rect collides with all other rects in other_objects. Due to the way the code is done 
    other_objects will contain the current unit's rect and as a result will always
    detect itself.
    This code is really dirty.


create_message (self,recipient:string, message:string)
    puts into memory a message to be sent to an appropriate channel object. 


send_message(self,channel:string)
    send a message to channel obj. 
    this sends a message to channel, with the addressee , and message 

retrieve_message(self,channel:string,mode='broadcast'): 
        mode = 'broadcast' --> will retrieve all broadcasted messages
        mode= 'focused' --> will retrieve messages addressed to that unit
    retrieve message from channel obj 
    There are two modes, either:
    1) "focused' will attempt to retrieve via unit's name, will return None if no message.
    
    2)'broadcast' it will attempt to retrieve messages with the address of 'broadcast', which is a message 
    for all units. 


"""

import sys, pygame


class unit(): 
    def __init__(self,surface,color=[0,0,255],startpos=[0,0],radii=10,name='None'):
        self.name=name
        self.surface=surface
        self.color=color
        self.position = startpos
        self.radii=radii
        self.object = pygame.draw.circle(self.surface,self.color,self.position,self.radii)
        self.collided=False
        self.speed=[0,0]
        self.allCollisions=0
        

        '''
        communication attributes
        '''
        self.messages=[]
        self.recipients=[]
        self.inbox=[]

        '''
        Interaction Functions: 
        '''
        self.oncollision=0
        self.ontimepass=0
        

    def register (self): 
        self.object= pygame.draw.circle(self.surface,self.color,self.position,self.radii)
        return self.object

    def set_speed(self,speed): 
        self.speed=speed

    def move (self): 
        self.position[0]+=self.speed[0]
        self.position[1]+=self.speed[1]
        self.object.move_ip((self.speed[0],self.speed[1]))

    '''
    communication methods
    '''
    def create_message(self,recipient,message): 
        self.recipients.append(recipient)
        self.messages.append(message)


    def send_message(self,channel):
        #TODO: this should technically be expanded to allow 
        #for any number of receipeints or messages.
        #check is messages are empty

        #The messages are stored by name of the agent. 
        if (self.recipients) and (self.messages):
            channel.messages[self.recipients[0]]=self.messages[0] 

    def retrieve_message(self,channel,mode='broadcast'): 
        if mode=='broadcast':
            self.inbox=channel.messages.get('broadcast',None)
        elif mode=='focused':
            self.inbox=channel.messages.get(self.name,None)
        
        
    
    
    
    '''
    interaction methods
    '''
    def passtime(self):
        if self.ontimepass==0:
            pass
        else:
            self.ontimepass()

    


    def collisions(self,self_id,other_objects): 
        self.allCollisions=self.object.collidelistall(other_objects)
        if (len(self.allCollisions)==1 and self.allCollisions[0] ==self_id) or not(self.allCollisions):
            #no collisions detected
            self.collided=False
            pass
            
        else:
            #collisions detected
            self.collided=True
            if self.oncollision ==0: 
                pass
            else: 
                self.oncollision()

        


    
        