import pygame, sys

from button import *
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



player_vs_c = False
# set player scores to 0
player_left_score = 0
player_right_score = 0
# font style for the score
score_font = pygame.font.Font('freesansbold.ttf', 60)
button1 = Button('press P for player vs player',1000,150,(100, 350))
button2 = Button('press C for player vs computer', 1000, 150, (100, 550))
button3 = Button('PyPong',1000,150,(100, 150))
# make player left and right
player_left = pygame.Rect(40,350,5,100)
player_right = pygame.Rect(1140,350,5,100)

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
            if ball.x == player_left.x + 5 and (ball.y >= player_left.y -15 and ball.y <= player_left.y + 100):
                ball_xdirection = ball_xdirection * -1
            # player right collision
            if ball.x == player_right.x - 30 and (ball.y >= player_right.y -15 and ball.y <= player_right.y + 100):
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
            screen.fill('black')
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
            player_left_text = score_font.render('Game Over', False, 'pink')
            screen.blit(player_left_text, (440, 260))
            player_left_text = score_font.render('press Y to continue or O to quit', False, 'pink')
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
                    player_right.y += 6
                if player_right.y > ball.y:
                    player_right.y -= 6
            # player left collision
            if ball.x == player_left.x + 5 and (ball.y >= player_left.y -15 and ball.y <= player_left.y + 100):
                ball_xdirection = ball_xdirection * -1
                ball_ydirection = ball_ydirection * 1.1
            # player right collision
            if ball.x == player_right.x - 30 and (ball.y >= player_right.y -15 and ball.y <= player_right.y + 100):
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
            screen.fill('black')
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
            player_left_text = score_font.render('Game Over', False, 'pink')
            screen.blit(player_left_text, (440, 260))
            player_left_text = score_font.render('press Y to continue or O to quit', False, 'pink')
            screen.blit(player_left_text, (160, 360))
            # set ball speed to begining
            ball_xdirection = 5
            ball_ydirection = 5
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
        mouse_pos = pygame.mouse.get_pos()
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     if button1.check_click(mouse_pos):
        #         options = False
        #         play = True
        screen.fill('grey')
        pygame.draw.rect(screen, 'black', bg)
        # player_left_text = score_font.render('Options', False, white)
        # screen.blit(player_left_text, (480, 260))
        # player_left_text = score_font.render('press P for two player', False, white)
        # screen.blit(player_left_text, (310, 400))
        # player_left_text = score_font.render('press C for player vs computer', False, white)
        # screen.blit(player_left_text, (180, 500))
        # player_left_text = score_font.render('press n to quit', False, white)
        # screen.blit(player_left_text, (400, 600))
        # draw players
        pygame.draw.rect(screen, white, player_left)
        player_left.y = 350
        # draw ball
        pygame.draw.rect(screen, white, player_right)
        #pygame.draw.ellipse(screen,white, ball)
        ball.x = 760
        ball.y = 200
        player_right.y = 350
            #player left score
        player_left_text = score_font.render(f'{player_left_score}', False, white)
        screen.blit(player_left_text, (560, 10))
            # player right score
        player_right_text = score_font.render(f'{player_right_score}', False, white)
        screen.blit(player_right_text, (610, 10))
        button3.draw()
        button1.draw()
        button2.draw()

        # update window
        pygame.display.flip()
        # this means 60 frames per sec
        clock.tick(60)
