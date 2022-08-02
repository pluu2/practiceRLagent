'''
channel.py
Method of communication between classes. This will probably be synchronous

Attributes:

messages:dict  ([recipient]=messages):str
    Will store messages, with the key being who the message is intended for.


'''


class Channel (): 
    def __init__(self): 
        self.messages={} 

    def send(self,recipient,message):
        self.messages[recipient] =message

    def retrieve(self,recipient): 
        return self.messages[recipient]
    



