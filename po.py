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
        # reset scores to zero
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_y:
                player_left_score = 0
                player_right_score = 0
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_y:
                player_left_score = 0
                player_right_score = 0
        # quit the game
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:
                pygame.quit()
                sys.exit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_n:
                pygame.quit()
                sys.exit()

    # keep playing until someone get three
    if player_left_score < 3 and player_right_score < 3:

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
    # display message to quit or continue
    if player_left_score == 3 or player_right_score == 3:
        player_left_text = score_font.render('Game Over', False, white)
        screen.blit(player_left_text, (440, 260))
        player_left_text = score_font.render('press Y to continue or N to quit', False, white)
        screen.blit(player_left_text, (160, 360))
    # update window
    pygame.display.flip()
    # this means 60 frames per sec
    clock.tick(60)




import pygame, sys
class Button:
    def __init__(self,text,width,height,pos):
        self.shape = pygame.Rect(pos,(width, height))
        self.color = 'pink'
        self.text = score_font.render(text, True, 'black')
        self.text_rect = self.text.get_rect(center = self.shape.center)

    def draw(self):
        pygame.draw.rect(screen, self.color , self.shape)
        screen.blit(self.text, self.text_rect)

# add all pygame modules
pygame.init()
clock = pygame.time.Clock()
# set up the screen
screen_width = 1200
screen_height = 900
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')
options = False
# make the ball
ball = pygame.Rect(585,435,30,30)
bg = pygame.Rect(0,0, 1200,900)
#color white for player and ball
white = (250,250,250)



player_vs_c = False
# set player scores to 0
player_left_score = 0
player_right_score = 0
# font style for the score
score_font = pygame.font.Font('freesansbold.ttf', 60)
button1 = Button('player vs computer',800,150,(200, 500))
# make player left and right
player_left = pygame.Rect(60,350,20,100)
player_right = pygame.Rect(1140,350,20,100)

# this affects the player movement in the game loop
player_left_direction = 0
player_right_direction = 0
# this affects ball movement in the game loop
ball_xdirection = 5
ball_ydirection = 5
options = True
play = False
while True:
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
            # reset scores to zero move players to middle
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    player_left_score = 0
                    player_right_score = 0
                    player_left.y = 350
                    player_right.y = 350
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_y:
                    player_left_score = 0
                    player_right_score = 0
                    player_left.y = 350
                    player_right.y = 350



            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_o:
                    player_left_score = 0
                    player_right_score = 0
                    player_left.y = 350
                    player_right.y = 350
                    ball.x = 600
                    ball.y = 450
                    play = False
                    options = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_o:
                    player_left_score = 0
                    player_right_score = 0
                    player_left.y = 350
                    player_right.y = 350
                    ball.x = 600
                    ball.y = 450
                    play = False
                    options = True
        # keep playing until someone get three
        if player_left_score < 3 and player_right_score < 3:

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
        # move player to center if they go off screen
        if player_left.y < -100 or player_left.y > 910:
            player_left.y = 350
        if player_right.y < -100 or player_right.y > 910:
            player_right.y = 350
        # display message to quit or continue
        if player_left.y < -100 or player_left.y > 910:
            player_left.y = 350
        if player_right.y < -100 or player_right.y > 910:
            player_right.y = 350
        if player_left_score == 3 or player_right_score == 3:
            player_left_text = score_font.render('Game Over', False, white)
            screen.blit(player_left_text, (440, 260))
            player_left_text = score_font.render('press Y to continue or O to quit', False, white)
            screen.blit(player_left_text, (160, 360))
        # update window
        pygame.display.flip()
        # this means 60 frames per sec
        clock.tick(60)

    while player_vs_c:
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
            # reset scores to zero
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    player_left.y = 350
                    player_left_score = 0
                    player_right_score = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_y:
                    player_left.y = 350
                    player_left_score = 0
                    player_right_score = 0
            # quit the game
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_n:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_o:
                    player_left_score = 0
                    player_right_score = 0
                    player_left.y = 350
                    player_right.y = 350
                    ball.x = 600
                    ball.y = 450
                    player_vs_c = False
                    options = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_o:
                    player_left_score = 0
                    player_right_score = 0
                    player_left.y = 350
                    player_right.y = 350
                    ball.x = 600
                    ball.y = 450
                    player_vs_c = False
                    options = True
        # keep playing until someone get three
        if player_left_score < 3 and player_right_score < 3:

            # ball movement
            ball.x += ball_xdirection
            ball.y += ball_ydirection
            # player movement
            player_left.y += player_left_direction
            if ball.x >  300:
                if player_right.y < ball.y:
                    player_right.y += 5
                if player_right.y > ball.y:
                    player_right.y -= 5
            # player left collision
            if ball.x == player_left.x + 10 and (ball.y >= player_left.y -15 and ball.y <= player_left.y + 100):
                ball_xdirection = ball_xdirection * -1
                ball_xdirection = ball_xdirection * 1.1
            # player right collision
            if ball.x == player_right.x - 20 and (ball.y >= player_right.y -15 and ball.y <= player_right.y + 100):
                ball_xdirection = ball_xdirection * -1
            # wall collision if ball goes off screen reset
            if ball.x > 1290:
                ball_xdirection = 5
                ball_xdirection = ball_xdirection * -1
                ball.x = 585
                ball.y = 435
                player_left_score += 1
            if ball.x < -90:
                ball_xdirection = 5
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
        if player_left.y < -100 or player_left.y > 910:
            player_left.y = 350
        if player_right.y < -100 or player_right.y > 910:
            player_right.y = 350
        # display message to quit or continue
        if player_left_score == 3 or player_right_score == 3:
            player_left_text = score_font.render('Game Over', False, white)
            screen.blit(player_left_text, (440, 260))
            player_left_text = score_font.render('press Y to continue or O to quit', False, white)
            screen.blit(player_left_text, (160, 360))
        # update window
        pygame.display.flip()
        # this means 60 frames per sec
        clock.tick(60)



    while options:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                options = False
                play = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_p:
                options = False
                play = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                options = False
                play = False
                player_vs_c = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_c:
                options = False
                play = False
                player_vs_c = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:
                pygame.quit()
                sys.exit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_n:
                pygame.quit()
                sys.exit()
        screen.fill('grey')
        pygame.draw.rect(screen, 'black', bg)
        player_left_text = score_font.render('Options', False, white)
        screen.blit(player_left_text, (440, 260))
        player_left_text = score_font.render('press P for two player', False, white)
        screen.blit(player_left_text, (250, 400))
        player_left_text = score_font.render('press C for player vs computer', False, white)
        screen.blit(player_left_text, (150, 500))
        player_left_text = score_font.render('press n to quit', False, white)
        screen.blit(player_left_text, (400, 600))

        # update window
        pygame.display.flip()
        # this means 60 frames per sec
        clock.tick(60)


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
play = False

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
        # reset scores to zero move players to middle
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_y:
                player_left_score = 0
                player_right_score = 0
                player_left.y = 350
                player_right.y = 350
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_y:
                player_left_score = 0
                player_right_score = 0
                player_left.y = 350
                player_right.y = 350

        # quit the game
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:
                pygame.quit()
                sys.exit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_n:
                pygame.quit()
                sys.exit()

    # keep playing until someone get three
    if player_left_score < 3 and player_right_score < 3:

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
    # move player to center if they go off screen
    if player_left.y < -100 or player_left.y > 910:
        player_left.y = 350
    if player_right.y < -100 or player_right.y > 910:
        player_right.y = 350
    # display message to quit or continue
    if player_left_score == 3 or player_right_score == 3:
        player_left_text = score_font.render('Game Over', False, white)
        screen.blit(player_left_text, (440, 260))
        player_left_text = score_font.render('press Y to continue or N to quit', False, white)
        screen.blit(player_left_text, (160, 360))
    # update window
    pygame.display.flip()
    # this means 60 frames per sec
    clock.tick(60)

player_vs_c = True
while player_vs_c:
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
        # reset scores to zero
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_y:
                player_left_score = 0
                player_right_score = 0
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_y:
                player_left_score = 0
                player_right_score = 0
        # quit the game
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:
                pygame.quit()
                sys.exit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_n:
                pygame.quit()
                sys.exit()

    # keep playing until someone get three
    if player_left_score < 3 and player_right_score < 3:

        # ball movement
        ball.x += ball_xdirection
        ball.y += ball_ydirection
        # player movement
        player_left.y += player_left_direction
        if ball.x >  300:
            if player_right.y < ball.y:
                player_right.y += 5
            if player_right.y > ball.y:
                player_right.y -= 5
        # player left collision
        if ball.x == player_left.x + 10 and (ball.y >= player_left.y -15 and ball.y <= player_left.y + 100):
            ball_xdirection = ball_xdirection * -1
            ball_xdirection = ball_xdirection * 1.1
        # player right collision
        if ball.x == player_right.x - 20 and (ball.y >= player_right.y -15 and ball.y <= player_right.y + 100):
            ball_xdirection = ball_xdirection * -1
        # wall collision if ball goes off screen reset
        if ball.x > 1290:
            ball_xdirection = 5
            ball_xdirection = ball_xdirection * -1
            ball.x = 585
            ball.y = 435
            player_left_score += 1
        if ball.x < -90:
            ball_xdirection = 5
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
    # move player to center if they go off screen
    if player_left.y < -100 or player_left.y > 910:
        player_left.y = 350
    if player_right.y < -100 or player_right.y > 910:
        player_right.y = 350
    # display message to quit or continue
    if player_left_score == 3 or player_right_score == 3:
        player_left_text = score_font.render('Game Over', False, white)
        screen.blit(player_left_text, (440, 260))
        player_left_text = score_font.render('press Y to continue or N to quit', False, white)
        screen.blit(player_left_text, (160, 360))
    # update window
    pygame.display.flip()
    # this means 60 frames per sec
    clock.tick(60)

# screen.blit(text, (600, 140))

# # font = pygame.font.SysFont('geneva', 130)
# # text = font.render('u', True, white)
# s = pygame.font.get_fonts()
# # for n in s:
# #     font = pygame.font.SysFont(s[n], 130)
# #     text = font.render('u', True, white)
# font = pygame.font.SysFont(f'{s[30]}', 130)
# text = font.render('u', True, white)







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
bg = pygame.Rect(0,0, 1200,900)
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
# set up game to start from options page
options = True
play = False
player_vs_c = False
# this loop runs logic for the whole game
while True:
    # this loop runs logic for player vs player
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
            # reset scores to zero move players to middle
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    player_left_score = 0
                    player_right_score = 0
                    player_left.y = 350
                    player_right.y = 350
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_y:
                    player_left_score = 0
                    player_right_score = 0
                    player_left.y = 350
                    player_right.y = 350


            # quit game and go back to options menu
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_o:
                    player_left_score = 0
                    player_right_score = 0
                    player_left.y = 350
                    player_right.y = 350
                    ball.x = 600
                    ball.y = 450
                    play = False
                    options = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_o:
                    player_left_score = 0
                    player_right_score = 0
                    player_left.y = 350
                    player_right.y = 350
                    ball.x = 600
                    ball.y = 450
                    play = False
                    options = True
        # keep playing until someone get three
        if player_left_score < 3 and player_right_score < 3:

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
        # move player to center if they go off screen
        if player_left.y < -100 or player_left.y > 910:
            player_left.y = 350
        if player_right.y < -100 or player_right.y > 910:
            player_right.y = 350
        # display message to quit or continue
        if player_left_score == 3 or player_right_score == 3:
            player_left_text = score_font.render('Game Over', False, white)
            screen.blit(player_left_text, (440, 260))
            player_left_text = score_font.render('press Y to continue or O to quit', False, white)
            screen.blit(player_left_text, (160, 360))
        # update window
        pygame.display.flip()
        # this means 60 frames per sec
        clock.tick(60)
    # logic for player vs computer
    while player_vs_c:
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
            # reset scores to zero
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    player_left.y = 350
                    player_left_score = 0
                    player_right_score = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_y:
                    player_left.y = 350
                    player_left_score = 0
                    player_right_score = 0
            # quit the game
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_n:
                    pygame.quit()
                    sys.exit()
            # quit game and return to options menu
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_o:
                    player_left_score = 0
                    player_right_score = 0
                    player_left.y = 350
                    player_right.y = 350
                    ball.x = 600
                    ball.y = 450
                    player_vs_c = False
                    options = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_o:
                    player_left_score = 0
                    player_right_score = 0
                    player_left.y = 350
                    player_right.y = 350
                    ball.x = 600
                    ball.y = 450
                    player_vs_c = False
                    options = True
        # keep playing until someone get three
        if player_left_score < 3 and player_right_score < 3:

            # ball movement
            ball.x += ball_xdirection
            ball.y += ball_ydirection
            # player movement
            player_left.y += player_left_direction
            player_right_move = 5
            if ball.x >  300:
                if player_right.y < ball.y:
                    player_right.y += player_right_move
                if player_right.y > ball.y:
                    player_right.y -= player_right_move
            # player left collision
            if ball.x == player_left.x + 10 and (ball.y >= player_left.y -15 and ball.y <= player_left.y + 100):
                ball_xdirection = ball_xdirection * -1
                ball_xdirection = ball_xdirection * 1.1
                player_right_move = player_right_move * 1.05
            # player right collision
            if ball.x == player_right.x - 20 and (ball.y >= player_right.y -15 and ball.y <= player_right.y + 100):
                ball_xdirection = ball_xdirection * -1
            # wall collision if ball goes off screen reset
            if ball.x > 1290:
                ball_xdirection = 5
                ball_xdirection = ball_xdirection * -1
                ball.x = 585
                ball.y = 435
                player_left_score += 1
            if ball.x < -90:
                ball_xdirection = 5
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
        # move player to center if they off screen
        if player_left.y < -100 or player_left.y > 910:
            player_left.y = 350
        if player_right.y < -100 or player_right.y > 910:
            player_right.y = 350
        # display message to quit or continue
        if player_left_score == 3 or player_right_score == 3:
            player_left_text = score_font.render('Game Over', False, white)
            screen.blit(player_left_text, (440, 260))
            player_left_text = score_font.render('press Y to continue or O to quit', False, white)
            screen.blit(player_left_text, (160, 360))
        # update window
        pygame.display.flip()
        # this means 60 frames per sec
        clock.tick(60)



    # logic for options menu
    while options:
        # start player vs player
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                options = False
                play = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_p:
                options = False
                play = True
        # switch to player vs computer
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                options = False
                play = False
                player_vs_c = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_c:
                options = False
                play = False
                player_vs_c = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:
                pygame.quit()
                sys.exit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_n:
                pygame.quit()
                sys.exit()
        mouse_pos = pygame.mouse.get_pos()
        # display game options
        screen.fill('grey')
        pygame.draw.rect(screen, 'black', bg)
        player_left_text = score_font.render('Options', False, white)
        screen.blit(player_left_text, (440, 260))
        player_left_text = score_font.render('press P for two player', False, white)
        screen.blit(player_left_text, (250, 400))
        player_left_text = score_font.render('press C for player vs computer', False, white)
        screen.blit(player_left_text, (150, 500))
        player_left_text = score_font.render('press n to quit', False, white)
        screen.blit(player_left_text, (400, 600))

        # update window
        pygame.display.flip()
        # this means 60 frames per sec
        clock.tick(60)
