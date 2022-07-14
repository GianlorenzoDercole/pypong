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



# set player scores to 0
player_left_score = 0
player_right_score = 0
# font style for the score
score_font = pygame.font.Font('freesansbold.ttf', 60)
# make player left and right
player_left = pygame.Rect(60,350,20,100)
player_right = pygame.Rect(1140,350,20,100)

# this affects the player movement in the game loop
player_left_direction = 0
player_right_direction = 0
# this affects ball movement in the game loop
ball_xdirection = 5
ball_ydirection = 5
play = True
play = play
while play:
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
    # player left collision
    if ball.x == player_left.x + 10 and (ball.y >= player_left.y -15 and ball.y <= player_left.y + 100):
        ball_xdirection = ball_xdirection * -1
    # player right collision
    if ball.x == player_right.x - 20 and (ball.y >= player_right.y -15 and ball.y <= player_right.y + 100):
        ball_xdirection = ball_xdirection * -1
    # wall collision if ball goes off screen reset
    if ball.x > 1290:
        ball_xdirection = ball_xdirection * -1
        ball.x = 585
        ball.y = 435
        player_left_score += 1
    if ball.x < -90:
        ball_xdirection = ball_xdirection * -1
        ball.x = 585
        ball.y = 435
        player_right_score += 1
    # change direction it reaches top or bottom of screen
    if ball.y < 0 or ball.y > 870:
        ball_ydirection = ball_ydirection * -1

    # color for court
    screen.fill('grey')
    # draw the ball
    pygame.draw.ellipse(screen,white, ball)
    # draw players
    pygame.draw.rect(screen, white, player_left)
    pygame.draw.rect(screen, white, player_right)
    # player left score
    player_left_text = score_font.render(f'{player_left_score}', False, white)
    screen.blit(player_left_text, (560, 10))
    # player right score
    player_right_text = score_font.render(f'{player_right_score}', False, white)
    screen.blit(player_right_text, (610, 10))
    # line in middle of screen
    pygame.draw.aaline(screen, white, (600,0),(600,900))
    # finish game
    if player_left_score == 3 or player_right_score == 3:
        play = False

    # update window
    pygame.display.flip()
    # this means 60 frames per sec
    clock.tick(60)
