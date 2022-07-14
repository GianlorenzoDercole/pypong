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

#color white for player and ball
white = (250,250,250)



# make player left and right
player_left = pygame.Rect(60,350,20,100)
player_right = pygame.Rect(1140,350,20,100)

# this affects the player movement in the game loop
player_left_direction = 0
player_right_direction = 0
# this affects ball movement in the game loop
ball_xdirection = 5
ball_ydirection = 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # handle player left movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                player_left_direction += 7
            if event.key == pygame.K_w:
                player_left_direction -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                player_left_direction -= 7
            if event.key == pygame.K_w:
                player_left_direction += 7
        # player right movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_right_direction += 7
            if event.key == pygame.K_UP:
                player_right_direction -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_right_direction -= 7
            if event.key == pygame.K_UP:
                player_right_direction += 7


    # ball movement
    ball.x += ball_xdirection
    ball.y += ball_ydirection
    # player movement
    player_left.y += player_left_direction
    player_right.y += player_right_direction
    if ball.x > 1200 or ball.x < 10:
        ball_xdirection = ball_xdirection * -1
    if ball.y < 10 or ball.y > 910:
        ball_ydirection = ball_ydirection * -1
    # color for court
    screen.fill('grey')
    # draw the ball
    pygame.draw.ellipse(screen,white, ball)
    # draw players
    pygame.draw.rect(screen, white, player_left)
    pygame.draw.rect(screen, white, player_right)

    # update window
    pygame.display.flip()
    # this means 60 frames per sec
    clock.tick(60)
