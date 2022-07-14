import pygame, sys

# add all pygame modules
pygame.init()
clock = pygame.time.Clock()
# set up the screen
screen_width = 1200
screen_height = 900
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')
# make the ball
ball = pygame.Rect(585,435,30,30)
white = (250,250,250)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill('grey')
    # draw the ball
    pygame.draw.ellipse(screen,white, ball)


    # update window
    pygame.display.flip()
    # this means 60 frames per sec
    clock.tick(60)
