import sys, pygame

pygame.init() #initialize the pygame class
size = width, height = 640, 480 #set the window height and width.
speed = [2, 2] #arbitrary code here?
black = 0, 0, 0
screen = pygame.display.set_mode(size) #instnatiate the screen, 

ball = pygame.image.load("intro_ball.gif") 
ballrect = ball.get_rect() #ah this is a surface.


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
    screen.fill(black) #This updates the screen, by blacking it out.
    screen.blit(ball, ballrect) #This draws the ball on to the ball rectangle? 
    pygame.display.flip() #This then displays all that was drawn(kind of like py.show()?)

