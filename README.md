Notes: 
This is a project to learn how to create animations using basic python. 


Feb 19 2022:

- If you get a GPU error, check if Ubuntu has updated any drivers, you may have to restart if required. 


-So with pygame the apparently key function here is the use of a blit, which you basically transfer pixels stored in a buffer to the screen. THe use of it is after instaitating a screen is.

	Screen.blit([object/image],[surface])

-A surface is basically a place on the screen that is the object or image will be draw in. 

-You move the surface around, using 

	surface.move_ip([x,y]), and this moves the item around relative to last position. 

- You then have to display or update the screen, after moving everything around in memory using 
	pygame.display.flip()

You instnatiate a surface by using:
	name=object.get_rect() 


-Drawing Multiple objects is similar idea, you instantiate multiple surfaces, blit them, and then use display.flip() 


-I will next try to figure out if this can be done in vectorized way. I need to move 'n' amount of items.
	- You can assign objects in list and then move through them. You can use a for loop to loop through the objects, I wish there was a faster vcctorized way to do this with blit. 

-Collision: 
	- This is interesting, as you will have to figure out how to detect screen edges, and also collisions with one another.

	- There is a function called 
	collidlistall ([list]) which will detect if there is any collision, and return the index. The collision is two way, so if 0 collides into 1, it will output 0, and object 1 as colliding. 


	- What is more odd is that since collidelistall is a method under the rect surface object, you can typically instantiate a empty object to use the method in other languages. For some reason I cannot do that and as a result you haev to instantiate a 'placeholder' object that exists outside the screen and then use that object as a method. 
	

Feb 20 2022: 

-Movement: Check the following Code: 
while 1: 
    for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            elif event.type==pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    print("Key A has been pressed")


- With the above code, it's one press, one response, to do a repeat, you have to add the code at the start of the code: 

	pygame.key.set_repeat(1,10)

Feb 21 2022: 
- So I have the ability to move an object now and detect collisions. 

Feb 23 -2022: 
- Wrap this into object based form and create a library. 
- I have created a basic class for each 'unit' that will move around the screen, each can be controlled.
- Need to check for collision, and figure out how to implement this. 
- The issue here is the way collisions work, pygame only tells you when something has collided, but does not say anything about how movement works (ie: whch direction). 


Feb 26, 2022: 
- A method for each unit to detect all other objects is to have system that registers all currently existing units. I will do this by having a method that returns the unit's surface, however I'm pretty sure this is probably a really inefficient way of doing this. 

- So that being said, with the main.py here, the loop will be something like , 
	1. gather all rects() from all units, 
	2. detect if there are collisions, 
	3. have each unit respond to the collision, 
	4. then draw. 

- Apparently, once you do a draw object, it actually automatically creates a rect(), which you can use for collision detection. Maybe I can collect all these and then draw. 
- So collisions have been updated, and collisions for any combintion
- Next I will have to technically implement side screen collisions.
- Then I will have to code something that allows the behaviour of each unit to be dictated by some script. Also implement inputs and outputs and various responses. I will have to code an API, 


Feb 27, 2022: 
- I can see if you wanted to code an API or a usable library, the base class "unit" would be inheiritable, where the user would define their own class to inheirit the unit class, and subsequently code their own script. 
- In addition, main.py would be more abstracted to improve useability.

-For now let's see if a neural network can be coded. 

- To do this, let's revisit the list above: A standard loop would look like this: 

	1. gather all rects() from all units, 
	2. detect if there are collisions, 
	3. have each unit respond to the collision, 
	4. then draw. 

- but to add a neural network script, it would be like: 

	1. Gather all stimuli from units.
	2. Calculate/Run Script using stimuli
	3. Calculate what has to be moved or unit responses
	4. gather all rects() from all units, 
	5. detect if there are collisions, 
	6. have each unit respond to the collision, 
	7. then draw. 

- I have allowed for subclassing of the Unit class, this will make it more clea to code up model for this library. 
- I have added some attributes in which various methods can be added
	1. oncollision attribute requires a method to be assigned and will be run when the unit detects a collision.
	2. ontimepass attribute which will run as time passe. 
-This has all been implemented. 

I will add another attribute or input to figure out inputs into the units. 

I think at this point I have the basics designed to create a library that can allow these units to do something once this last point is done. It'll be interesting to see what will happen .


TODO: Communication system.
- What I also need to implement is a communication system. Maybe ther is something like a 'gather' sensor kind of thing. I believe I can implement this using possibly on the collision setting.
- I created another attribute called allCollisions, which list all the collisions are stored (which again includes itself), remember that.

- So with a communication system, you need a few things. With communication systems, you need a sender and a receiver indication. 

March 5 2022- 

- Communications. There were several yotube videos I watched about different paradigms in regards to communication or message passing between classes. The old method was if you have two classes, and a form of non-determinatistic communication occured,  the two classes would have to self instantiate a communication class. 
- However, more modern methods especially those found in JS, or c# allow the use of something called 'channels', which is apparently an object that kind of runs in the background, where classes send information to, and the classes in their own time can query for messages from other classes.  

	- The advantage of this method is that the classes are isolated from each other, modifications to the units themselves do not require further code modification to the communication classes or other classes. 


- In python, I can do this currently only synchroniously, so all units need to put data down into this channel obbject, then all units need to draw from the channel object. This is probably slightly less efficient, than async. I will have to examine other methods, like multi-threading, or the use of GPUs, but that is a bit different but it is something I will examiine in the future. 

- The rationale behind this entire project is to allow units to communicate and perhaps comlpete some task in ensembles. Synchronous communication may not be the best here since some tasks require procedural or sequential information. We will see. 


- I have technically implemented the communication, I have to think more carefully on how to demonstrate it. I am thinking of demonstrating maybe something where the color changes to the higher value and then speed information is passed and that unit will move the same 'speed' as the one it collided to. I will do this tommorow.

March 11, 2022: 
- As a note in the past, I have to mention that the collision mechanism is a bit odd. Given the object, when collisions are generated, the list of collisions include collisinos with itself. This movement selected against, by using the list comprehension: 
	- [x for x in self.allCollisions if x!=int(self.name)]] 
	- Where self.name is the name of the current object. 
-TODO : REmember also that currently the create_message function only allows a single recipient. Technically speaking this should accept as many messages as possible. 


June 19, 2022: 
- Correcting and updating comments. Thinking of method in which to integrate RL or ML algorithms. 
- Previously, I have struggled with installing Jax here (which I will learn), but working with Forward Gradients, specifically presented by Baydin et al. (2022), I think I have a more simple way of implementing a learning algorithm. Let's take a look. 

- How to integrate RL here? 
- RL can be divided into a process relative to the agent.  
	1) Agent checks state by probing enviroment. 
	2) Agent takes action on enviroment
	3) Enviroment returns reward to the agent. 
	

June 23 , 2022: 
- What are the inputs and outputs of these agents? 
- Inputs:
	1) Inputs are movement direction (delta X, delta Y)
	2) Current X,Y positions (?Unsure if this is the best way)
	3) Who they have collided into. 
	4) Communication Messages
- Outputs: 
	1) Communcation message
	2) Movement Direction
- Loss/Reward Function:
	1) Reward accross all agents (sum_all_agents)
	