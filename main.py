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
player_left = pygame.Rect(60,350,20,100)
player_right = pygame.Rect(1140,350,20,100)
white = (250,250,250)
player_direction = 0
ball_xdirection = 5
ball_ydirection = 5
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                player_direction += 7
            if event.key == pygame.K_w:
                player_direction -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                player_direction -= 7
            if event.key == pygame.K_w:
                player_direction += 7



    ball.x += ball_xdirection
    ball.y += ball_ydirection
    player_left.y += player_direction
    if ball.x > 1100 or ball.x < 100:
        ball_xdirection = ball_xdirection * -1
    if ball.y < 100 or ball.y > 800:
        ball_ydirection = ball_ydirection * -1
    # color for court
    screen.fill('grey')
    # draw the ball
    pygame.draw.ellipse(screen,white, ball)
    pygame.draw.rect(screen, white, player_left)

    # update window
    pygame.display.flip()
    # this means 60 frames per sec
    clock.tick(60)
