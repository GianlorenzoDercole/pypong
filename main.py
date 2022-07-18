import pygame, sys

from button import *
#set up variables to choose game mode
options = True
play = False
player_vs_c = False
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
            pygame.draw.ellipse(screen,'hotpink', ball)
            # draw players
            pygame.draw.rect(screen, 'green', player_left)
            pygame.draw.rect(screen, 'green', player_right)
            # player left score
            player_left_text = score_font.render(f'{player_left_score}', False, 'green')
            screen.blit(player_left_text, (560, 10))
            # player right score
            player_right_text = score_font.render(f'{player_right_score}', False, 'green')
            screen.blit(player_right_text, (610, 10))
            # line in middle of screen
            pygame.draw.aaline(screen, 'blue', (600,0),(600,900))
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
            player_left_text = score_font.render('Game Over', False, 'hotpink')
            screen.blit(player_left_text, (440, 260))
            player_left_text = score_font.render('press Y to continue or O to quit', False, 'hotpink')
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
            pygame.draw.ellipse(screen,'hotpink', ball)
            # draw players
            pygame.draw.rect(screen, 'green', player_left)
            pygame.draw.rect(screen, 'green', player_right)
            # player left score
            player_left_text = score_font.render(f'{player_left_score}', False, 'green')
            screen.blit(player_left_text, (560, 10))
            # player right score
            player_right_text = score_font.render(f'{player_right_score}', False, 'green')
            screen.blit(player_right_text, (610, 10))
            # line in middle of screen
            pygame.draw.aaline(screen, 'blue', (600,0),(600,900))
        if player_left.y < -100 or player_left.y > 910:
            player_left.y = 350
        if player_right.y < -100 or player_right.y > 910:
            player_right.y = 350
        # display message to quit or continue
        if player_left_score == 3 or player_right_score == 3:
            player_left_text = score_font.render('Game Over', False, 'hotpink')
            screen.blit(player_left_text, (440, 260))
            player_left_text = score_font.render('press Y to continue or O to quit', False, 'hotpink')
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

        screen.fill('grey')
        pygame.draw.rect(screen, 'black', bg)
        pygame.draw.rect(screen, 'green', player_left)
        player_left.y = 350
        # draw ball
        pygame.draw.rect(screen, 'green', player_right)
        #pygame.draw.ellipse(screen,white, ball)
        ball.x = 760
        ball.y = 200
        player_right.y = 350
            #player left score
        player_left_text = score_font.render(f'{player_left_score}', False, 'green')
        screen.blit(player_left_text, (560, 10))
            # player right score
        player_right_text = score_font.render(f'{player_right_score}', False, 'green')
        screen.blit(player_right_text, (610, 10))
        # center line
        pygame.draw.aaline(screen, 'blue', (600,0),(600,290))
        pygame.draw.aaline(screen, 'blue', (600,700),(600,900))
        button3.draw()
        button1.draw()
        button2.draw()


        # update window
        pygame.display.flip()
        # this means 60 frames per sec
        clock.tick(60)


# import pygame, sys

# options = True
# play = False
# player_vs_c = False
# def player_vs_player():
#     global options
#     global play
#     options = False
#     play = True
# def player_vs_compute():
#     global options
#     global player_vs_c
#     options = False
#     player_vs_c = True
# class Button:
#     def __init__(self,text,width,height,pos):
#         self.shape = pygame.Rect(pos,(width, height))
#         self.color = 'black'
#         self.text = score_font.render(text, True, 'hotpink')
#         self.text_rect = self.text.get_rect(center = self.shape.center)
#         self.pressed = False
#     def draw(self):
#         pygame.draw.rect(screen, self.color , self.shape)
#         screen.blit(self.text, self.text_rect)
#         self.check_click()

#     def check_click(self):
#         mouse_pos = pygame.mouse.get_pos()
#         if self.shape.collidepoint(mouse_pos):
#             if pygame.mouse.get_pressed()[0]:
#                 self.pressed = True
#             else:
#                 if self.pressed == True:

#                     print('y')
#                     player_vs_player()
#                     self.pressed = False

# class Button1:
#     def __init__(self,text,width,height,pos):
#         self.shape = pygame.Rect(pos,(width, height))
#         self.color = 'black'
#         self.text = score_font.render(text, True, 'hotpink')
#         self.text_rect = self.text.get_rect(center = self.shape.center)
#         self.pressed = False
#     def draw(self):
#         pygame.draw.rect(screen, self.color , self.shape)
#         screen.blit(self.text, self.text_rect)
#         self.check_click()

#     def check_click(self):
#         mouse_pos = pygame.mouse.get_pos()
#         if self.shape.collidepoint(mouse_pos):
#             if pygame.mouse.get_pressed()[0]:
#                 self.pressed = True
#             else:
#                 if self.pressed == True:

#                     print('y')
#                     player_vs_compute()
#                     self.pressed = False

# # add all pygame modules
# pygame.init()
# clock = pygame.time.Clock()
# # set up the screen
# screen_width = 1200
# screen_height = 900
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption('Pong')
# # make the ball
# ball = pygame.Rect(585,435,30,30)
# bg = pygame.Rect(0,0, 1200,900)
# #color white for player and ball
# white = (250,250,250)




# # set player scores to 0
# player_left_score = 0
# player_right_score = 0
# # font style for the score
# score_font = pygame.font.Font('freesansbold.ttf', 45)
# button1 = Button('Click here or press P for player vs player',1000,150,(100, 350))
# button2 = Button1('Click here or press C for player vs computer', 1000, 150, (100, 550))
# button3 = Button('PyPong',1000,150,(100, 150))
# # make player left and right
# player_left = pygame.Rect(40,350,5,100)
# player_right = pygame.Rect(1140,350,5,100)
# # this affects the player movement in the game loop
# player_left_direction = 0
# player_right_direction = 0
# # this affects ball movement in the game loop
# ball_xdirection = 5
# ball_ydirection = 5



# while True:
#     while play:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             # handle player left movement
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_s:
#                     player_left_direction += 7
#                 if event.key == pygame.K_w:
#                     player_left_direction -= 7
#             if event.type == pygame.KEYUP:
#                 if event.key == pygame.K_s:
#                     player_left_direction -= 7
#                 if event.key == pygame.K_w:
#                     player_left_direction += 7

#             # player right movement
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_DOWN:
#                     player_right_direction += 7
#                 if event.key == pygame.K_UP:
#                     player_right_direction -= 7
#             if event.type == pygame.KEYUP:
#                 if event.key == pygame.K_DOWN:
#                     player_right_direction -= 7
#                 if event.key == pygame.K_UP:
#                     player_right_direction += 7
#             # reset scores to zero move players to middle
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_y:
#                     player_left_score = 0
#                     player_right_score = 0
#                     player_left.y = 350
#                     player_right.y = 350
#             if event.type == pygame.KEYUP:
#                 if event.key == pygame.K_y:
#                     player_left_score = 0
#                     player_right_score = 0
#                     player_left.y = 350
#                     player_right.y = 350



#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_o:
#                     player_left_score = 0
#                     player_right_score = 0
#                     player_left.y = 350
#                     player_right.y = 350
#                     ball.x = 600
#                     ball.y = 450
#                     play = False
#                     options = True
#             if event.type == pygame.KEYUP:
#                 if event.key == pygame.K_o:
#                     player_left_score = 0
#                     player_right_score = 0
#                     player_left.y = 350
#                     player_right.y = 350
#                     ball.x = 600
#                     ball.y = 450
#                     play = False
#                     options = True
#         # keep playing until someone get three
#         if player_left_score < 3 and player_right_score < 3:
#             # ball movement
#             ball.x += ball_xdirection
#             ball.y += ball_ydirection
#             # player movement
#             player_left.y += player_left_direction
#             player_right.y += player_right_direction
#             # player left collision
#             if ball.x == player_left.x + 5 and (ball.y >= player_left.y -15 and ball.y <= player_left.y + 100):
#                 ball_xdirection = ball_xdirection * -1
#             # player right collision
#             if ball.x == player_right.x - 30 and (ball.y >= player_right.y -15 and ball.y <= player_right.y + 100):
#                 ball_xdirection = ball_xdirection * -1
#             # wall collision if ball goes off screen reset
#             if ball.x > 1290:
#                 ball_xdirection = ball_xdirection * -1
#                 ball.x = 585
#                 ball.y = 435
#                 player_left_score += 1
#             if ball.x < -90:
#                 ball_xdirection = ball_xdirection * -1
#                 ball.x = 585
#                 ball.y = 435
#                 player_right_score += 1
#             # change direction it reaches top or bottom of screen
#             if ball.y < 0 or ball.y > 870:
#                 ball_ydirection = ball_ydirection * -1

#             # color for court
#             screen.fill('black')
#             # draw the ball
#             pygame.draw.ellipse(screen,'hotpink', ball)
#             # draw players
#             pygame.draw.rect(screen, 'green', player_left)
#             pygame.draw.rect(screen, 'green', player_right)
#             # player left score
#             player_left_text = score_font.render(f'{player_left_score}', False, 'green')
#             screen.blit(player_left_text, (560, 10))
#             # player right score
#             player_right_text = score_font.render(f'{player_right_score}', False, 'green')
#             screen.blit(player_right_text, (610, 10))
#             # line in middle of screen
#             pygame.draw.aaline(screen, 'blue', (600,0),(600,900))
#         # move player to center if they go off screen
#         if player_left.y < -100 or player_left.y > 910:
#             player_left.y = 350
#         if player_right.y < -100 or player_right.y > 910:
#             player_right.y = 350
#         # display message to quit or continue
#         if player_left.y < -100 or player_left.y > 910:
#             player_left.y = 350
#         if player_right.y < -100 or player_right.y > 910:
#             player_right.y = 350
#         if player_left_score == 3 or player_right_score == 3:
#             player_left_text = score_font.render('Game Over', False, 'hotpink')
#             screen.blit(player_left_text, (440, 260))
#             player_left_text = score_font.render('press Y to continue or O to quit', False, 'hotpink')
#             screen.blit(player_left_text, (160, 360))
#         # update window
#         pygame.display.flip()
#         # this means 60 frames per sec
#         clock.tick(60)

#     while player_vs_c:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             # handle player left movement
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_s:
#                     player_left_direction += 7
#                 if event.key == pygame.K_w:
#                     player_left_direction -= 7
#             if event.type == pygame.KEYUP:
#                 if event.key == pygame.K_s:
#                     player_left_direction -= 7
#                 if event.key == pygame.K_w:
#                     player_left_direction += 7

#             # player right movement
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_DOWN:
#                     player_right_direction += 7
#                 if event.key == pygame.K_UP:
#                     player_right_direction -= 7
#             if event.type == pygame.KEYUP:
#                 if event.key == pygame.K_DOWN:
#                     player_right_direction -= 7
#                 if event.key == pygame.K_UP:
#                     player_right_direction += 7
#             # reset scores to zero
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_y:
#                     player_left.y = 350
#                     player_left_score = 0
#                     player_right_score = 0
#             if event.type == pygame.KEYUP:
#                 if event.key == pygame.K_y:
#                     player_left.y = 350
#                     player_left_score = 0
#                     player_right_score = 0
#             # quit the game
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_n:
#                     pygame.quit()
#                     sys.exit()
#             if event.type == pygame.KEYUP:
#                 if event.key == pygame.K_n:
#                     pygame.quit()
#                     sys.exit()

#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_o:
#                     player_left_score = 0
#                     player_right_score = 0
#                     player_left.y = 350
#                     player_right.y = 350
#                     ball.x = 600
#                     ball.y = 450
#                     player_vs_c = False
#                     options = True
#             if event.type == pygame.KEYUP:
#                 if event.key == pygame.K_o:
#                     player_left_score = 0
#                     player_right_score = 0
#                     player_left.y = 350
#                     player_right.y = 350
#                     ball.x = 600
#                     ball.y = 450
#                     player_vs_c = False
#                     options = True
#         # keep playing until someone get three
#         if player_left_score < 3 and player_right_score < 3:

#             # ball movement
#             ball.x += ball_xdirection
#             ball.y += ball_ydirection
#             # player movement
#             player_left.y += player_left_direction
#             if ball.x >  300:
#                 if player_right.y < ball.y:
#                     player_right.y += 6
#                 if player_right.y > ball.y:
#                     player_right.y -= 6
#             # player left collision
#             if ball.x == player_left.x + 5 and (ball.y >= player_left.y -15 and ball.y <= player_left.y + 100):
#                 ball_xdirection = ball_xdirection * -1
#                 ball_ydirection = ball_ydirection * 1.1
#             # player right collision
#             if ball.x == player_right.x - 30 and (ball.y >= player_right.y -15 and ball.y <= player_right.y + 100):
#                 ball_xdirection = ball_xdirection * -1
#             # wall collision if ball goes off screen reset
#             if ball.x > 1290:
#                 ball_xdirection = 5
#                 ball_xdirection = ball_xdirection * -1
#                 ball.x = 585
#                 ball.y = 435
#                 player_left_score += 1
#             if ball.x < -90:
#                 ball_xdirection = 5
#                 ball_xdirection = ball_xdirection * -1
#                 ball.x = 585
#                 ball.y = 435
#                 player_right_score += 1
#             # change direction it reaches top or bottom of screen
#             if ball.y < 0 or ball.y > 870:
#                 ball_ydirection = ball_ydirection * -1

#             # color for court
#             screen.fill('black')
#             # draw the ball
#             pygame.draw.ellipse(screen,'hotpink', ball)
#             # draw players
#             pygame.draw.rect(screen, 'green', player_left)
#             pygame.draw.rect(screen, 'green', player_right)
#             # player left score
#             player_left_text = score_font.render(f'{player_left_score}', False, 'green')
#             screen.blit(player_left_text, (560, 10))
#             # player right score
#             player_right_text = score_font.render(f'{player_right_score}', False, 'green')
#             screen.blit(player_right_text, (610, 10))
#             # line in middle of screen
#             pygame.draw.aaline(screen, 'blue', (600,0),(600,900))
#         if player_left.y < -100 or player_left.y > 910:
#             player_left.y = 350
#         if player_right.y < -100 or player_right.y > 910:
#             player_right.y = 350
#         # display message to quit or continue
#         if player_left_score == 3 or player_right_score == 3:
#             player_left_text = score_font.render('Game Over', False, 'hotpink')
#             screen.blit(player_left_text, (440, 260))
#             player_left_text = score_font.render('press Y to continue or O to quit', False, 'hotpink')
#             screen.blit(player_left_text, (160, 360))
#             # set ball speed to begining
#             ball_xdirection = 5
#             ball_ydirection = 5
#         # update window
#         pygame.display.flip()
#         # this means 60 frames per sec
#         clock.tick(60)



#     while options:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_p:
#                 options = False
#                 play = True

#         if event.type == pygame.KEYUP:
#             if event.key == pygame.K_p:
#                 options = False
#                 play = True
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_c:
#                 options = False
#                 play = False
#                 player_vs_c = True

#         if event.type == pygame.KEYUP:
#             if event.key == pygame.K_c:
#                 options = False
#                 play = False
#                 player_vs_c = True
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_n:
#                 pygame.quit()
#                 sys.exit()
#         if event.type == pygame.KEYUP:
#             if event.key == pygame.K_n:
#                 pygame.quit()
#                 sys.exit()
#         mouse_pos = pygame.mouse.get_pos()
#         # if event.type == pygame.MOUSEBUTTONDOWN:
#         #     if button1.check_click(mouse_pos):
#         #         options = False
#         #         play = True
#         screen.fill('grey')
#         pygame.draw.rect(screen, 'black', bg)
#         # player_left_text = score_font.render('Options', False, white)
#         # screen.blit(player_left_text, (480, 260))
#         # player_left_text = score_font.render('press P for two player', False, white)
#         # screen.blit(player_left_text, (310, 400))
#         # player_left_text = score_font.render('press C for player vs computer', False, white)
#         # screen.blit(player_left_text, (180, 500))
#         # player_left_text = score_font.render('press n to quit', False, white)
#         # screen.blit(player_left_text, (400, 600))
#         # draw players
#         pygame.draw.rect(screen, 'green', player_left)
#         player_left.y = 350
#         # draw ball
#         pygame.draw.rect(screen, 'green', player_right)
#         #pygame.draw.ellipse(screen,white, ball)
#         ball.x = 760
#         ball.y = 200
#         player_right.y = 350
#             #player left score
#         player_left_text = score_font.render(f'{player_left_score}', False, 'green')
#         screen.blit(player_left_text, (560, 10))
#             # player right score
#         player_right_text = score_font.render(f'{player_right_score}', False, 'green')
#         screen.blit(player_right_text, (610, 10))
#         # center line
#         pygame.draw.aaline(screen, 'blue', (600,0),(600,290))
#         pygame.draw.aaline(screen, 'blue', (600,700),(600,900))
#         button3.draw()
#         button1.draw()
#         button2.draw()


#         # update window
#         pygame.display.flip()
#         # this means 60 frames per sec
#         clock.tick(60)










# import pygame, sys

# # set variables to control which game mode player is in
# options = True
# play = False
# player_vs_c = False
# # function to switch from options menu to player vs player
# def player_vs_player():
#     global options
#     global play
#     options = False
#     play = True
# # function to switch from options menu to player vs computer
# def player_vs_computer():
#     global options
#     global player_vs_c
#     options = False
#     player_vs_c = True
# # button class used for clickable text on options menu
# class Button:
#     def __init__(self,text,width,height,pos):
#         # surface for button
#         self.shape = pygame.Rect(pos,(width, height))
#         self.color = blue
#         self.text = score_font.render(text, True, white)
#         self.text_rect = self.text.get_rect(center = self.shape.center)
#         self.pressed = False
#     def draw(self):
#         pygame.draw.rect(screen, self.color , self.shape)
#         screen.blit(self.text, self.text_rect)
#         self.check_click()
#     # this button does not have function for click
#     def check_click(self):
#         mouse_pos = pygame.mouse.get_pos()
#         if self.shape.collidepoint(mouse_pos):
#             if pygame.mouse.get_pressed()[0]:
#                 self.pressed = True
#             else:
#                 if self.pressed == True:

#                     self.pressed = False
# # this button switches from options to player vs player
# class Button_player_vs_player:
#     def __init__(self,text,width,height,pos):
#         self.shape = pygame.Rect(pos,(width, height))
#         self.color = blue
#         self.text = score_font.render(text, True, white)
#         self.text_rect = self.text.get_rect(center = self.shape.center)
#         self.pressed = False
#     def draw(self):
#         pygame.draw.rect(screen, self.color , self.shape)
#         screen.blit(self.text, self.text_rect)
#         self.check_click()
#     # this button calls player_vs_player function when clicked
#     def check_click(self):
#         mouse_pos = pygame.mouse.get_pos()
#         if self.shape.collidepoint(mouse_pos):
#             if pygame.mouse.get_pressed()[0]:
#                 self.pressed = True
#             else:
#                 if self.pressed == True:

#                     player_vs_player()

#                     self.pressed = False

# # this button switches from options to player vs computer
# class Button_player_vs_computer:
#     def __init__(self,text,width,height,pos):
#         self.shape = pygame.Rect(pos,(width, height))
#         self.color = blue
#         self.text = score_font.render(text, True, white)
#         self.text_rect = self.text.get_rect(center = self.shape.center)
#         self.pressed = False
#     def draw(self):
#         pygame.draw.rect(screen, self.color , self.shape)
#         screen.blit(self.text, self.text_rect)
#         self.check_click()
#     # this button calls player_vs computer function when clicked
#     def check_click(self):
#         mouse_pos = pygame.mouse.get_pos()
#         if self.shape.collidepoint(mouse_pos):
#             if pygame.mouse.get_pressed()[0]:
#                 self.pressed = True
#             else:
#                 if self.pressed == True:

#                     player_vs_computer()
#                     self.pressed = False
# # add all pygame modules
# pygame.init()
# clock = pygame.time.Clock()
# # set up the screen
# screen_width = 1200
# screen_height = 900
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption('Pong')
# # make the ball
# ball = pygame.Rect(585,435,30,30)
# bg = pygame.Rect(0,0, 1200,900)
# #color white for player and ball
# white = (250,250,250)
# # color blue for board
# blue = (102, 191, 191)
# # set player scores to 0
# player_left_score = 0
# player_right_score = 0
# # font style for the score
# score_font = pygame.font.Font('freesansbold.ttf', 45)
# # buttons for options menu
# button1 = Button('PyPong',1000,150,(100, 150))
# button2 = Button_player_vs_player('Click here or press P for player vs player',1000,150,(100, 350))
# button3 = Button_player_vs_computer('Click here or press C for player vs computer', 1000, 150, (100, 550))
# # make player left and right
# player_left = pygame.Rect(40,350,5,100)
# player_right = pygame.Rect(1140,350,5,100)
# # this affects the player movement in the game loop
# player_left_direction = 0
# player_right_direction = 0
# # this affects ball movement in the game loop
# ball_xdirection = 5
# ball_ydirection = 5

# while True:
#     # this loop runs the player vs player logic
#     while play:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             # handle player left movement
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_s:
#                     player_left_direction += 7
#                 if event.key == pygame.K_w:
#                     player_left_direction -= 7
#             if event.type == pygame.KEYUP:
#                 if event.key == pygame.K_s:
#                     player_left_direction -= 7
#                 if event.key == pygame.K_w:
#                     player_left_direction += 7

#             # player right movement
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_DOWN:
#                     player_right_direction += 7
#                 if event.key == pygame.K_UP:
#                     player_right_direction -= 7
#             if event.type == pygame.KEYUP:
#                 if event.key == pygame.K_DOWN:
#                     player_right_direction -= 7
#                 if event.key == pygame.K_UP:
#                     player_right_direction += 7
#             # reset scores to zero move players to middle
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_y:
#                     player_left_score = 0
#                     player_right_score = 0
#                     player_left.y = 350
#                     player_right.y = 350
#             if event.type == pygame.KEYUP:
#                 if event.key == pygame.K_y:
#                     player_left_score = 0
#                     player_right_score = 0
#                     player_left.y = 350
#                     player_right.y = 350
#             # quit game go back to options menu
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_o:
#                     player_left_score = 0
#                     player_right_score = 0
#                     player_left.y = 350
#                     player_right.y = 350
#                     ball.x = 600
#                     ball.y = 450
#                     play = False
#                     options = True
#             if event.type == pygame.KEYUP:
#                 if event.key == pygame.K_o:
#                     player_left_score = 0
#                     player_right_score = 0
#                     player_left.y = 350
#                     player_right.y = 350
#                     ball.x = 600
#                     ball.y = 450
#                     play = False
#                     options = True
#         # keep playing until someone get three
#         if player_left_score < 3 and player_right_score < 3:
#             # ball movement
#             ball.x += ball_xdirection
#             ball.y += ball_ydirection
#             # player movement
#             player_left.y += player_left_direction
#             player_right.y += player_right_direction
#             # player left collision
#             if ball.x == player_left.x + 5 and (ball.y >= player_left.y -15 and ball.y <= player_left.y + 100):
#                 ball_xdirection = ball_xdirection * -1
#             # player right collision
#             if ball.x == player_right.x - 30 and (ball.y >= player_right.y -15 and ball.y <= player_right.y + 100):
#                 ball_xdirection = ball_xdirection * -1
#             # wall collision if ball goes off screen reset
#             if ball.x > 1290:
#                 ball_xdirection = ball_xdirection * -1
#                 ball.x = 585
#                 ball.y = 435
#                 player_left_score += 1
#             if ball.x < -90:
#                 ball_xdirection = ball_xdirection * -1
#                 ball.x = 585
#                 ball.y = 435
#                 player_right_score += 1
#             # change direction it reaches top or bottom of screen
#             if ball.y < 0 or ball.y > 870:
#                 ball_ydirection = ball_ydirection * -1

#             # color for court
#             screen.fill(blue)
#             # draw the ball
#             pygame.draw.ellipse(screen,white, ball)
#             # draw players
#             pygame.draw.rect(screen, white, player_left)
#             pygame.draw.rect(screen, white, player_right)
#             # player left score
#             player_left_text = score_font.render(f'{player_left_score}', False, white)
#             screen.blit(player_left_text, (565, 10))
#             # player right score
#             player_right_text = score_font.render(f'{player_right_score}', False, white)
#             screen.blit(player_right_text, (610, 10))
#             # line in middle of screen
#             pygame.draw.aaline(screen, white, (600,0),(600,900))
#         # move player to center if they go off screen
#         if player_left.y < -100 or player_left.y > 910:
#             player_left.y = 350
#         if player_right.y < -100 or player_right.y > 910:
#             player_right.y = 350
#         # display message to quit or continue
#         if player_left_score == 3 or player_right_score == 3:
#             player_left_text = score_font.render('Game Over', False, white)
#             screen.blit(player_left_text, (500, 260))
#             player_left_text = score_font.render('press Y to continue or O to quit', False, white)
#             screen.blit(player_left_text, (255, 360))
#         # update window
#         pygame.display.flip()
#         # this means 60 frames per sec
#         clock.tick(60)
#     # game loop for player vs computer logic
#     while player_vs_c:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             # handle player left movement
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_s:
#                     player_left_direction += 7
#                 if event.key == pygame.K_w:
#                     player_left_direction -= 7
#             if event.type == pygame.KEYUP:
#                 if event.key == pygame.K_s:
#                     player_left_direction -= 7
#                 if event.key == pygame.K_w:
#                     player_left_direction += 7

#             # player right movement
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_DOWN:
#                     player_right_direction += 7
#                 if event.key == pygame.K_UP:
#                     player_right_direction -= 7
#             if event.type == pygame.KEYUP:
#                 if event.key == pygame.K_DOWN:
#                     player_right_direction -= 7
#                 if event.key == pygame.K_UP:
#                     player_right_direction += 7
#             # reset scores to zero
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_y:
#                     player_left.y = 350
#                     player_left_score = 0
#                     player_right_score = 0
#             if event.type == pygame.KEYUP:
#                 if event.key == pygame.K_y:
#                     player_left.y = 350
#                     player_left_score = 0
#                     player_right_score = 0

#             # quit game return to options menu
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_o:
#                     player_left_score = 0
#                     player_right_score = 0
#                     player_left.y = 350
#                     player_right.y = 350
#                     ball.x = 600
#                     ball.y = 450
#                     player_vs_c = False
#                     options = True
#             if event.type == pygame.KEYUP:
#                 if event.key == pygame.K_o:
#                     player_left_score = 0
#                     player_right_score = 0
#                     player_left.y = 350
#                     player_right.y = 350
#                     ball.x = 600
#                     ball.y = 450
#                     player_vs_c = False
#                     options = True
#         # keep playing until someone get three
#         if player_left_score < 3 and player_right_score < 3:

#             # ball movement
#             ball.x += ball_xdirection
#             ball.y += ball_ydirection
#             # player left movement
#             player_left.y += player_left_direction
#             # computer movement
#             if ball.x >  300:
#                 if player_right.y < ball.y:
#                     player_right.y += 6
#                 if player_right.y > ball.y:
#                     player_right.y -= 6
#             # player left collision
#             if ball.x == player_left.x + 5 and (ball.y >= player_left.y -15 and ball.y <= player_left.y + 100):
#                 ball_xdirection = ball_xdirection * -1
#                 ball_ydirection = ball_ydirection * 1.1
#             # player right collision
#             if ball.x == player_right.x - 30 and (ball.y >= player_right.y -15 and ball.y <= player_right.y + 100):
#                 ball_xdirection = ball_xdirection * -1
#             # wall collision if ball goes off screen reset
#             if ball.x > 1290:
#                 ball_xdirection = 5
#                 ball_xdirection = ball_xdirection * -1
#                 ball.x = 585
#                 ball.y = 435
#                 player_left_score += 1
#             if ball.x < -90:
#                 ball_xdirection = 5
#                 ball_xdirection = ball_xdirection * -1
#                 ball.x = 585
#                 ball.y = 435
#                 player_right_score += 1
#             # change direction it reaches top or bottom of screen
#             if ball.y < 0 or ball.y > 870:
#                 ball_ydirection = ball_ydirection * -1

#             # color for court
#             screen.fill(blue)
#             # draw the ball
#             pygame.draw.ellipse(screen,white, ball)
#             # draw players
#             pygame.draw.rect(screen, white, player_left)
#             pygame.draw.rect(screen, white, player_right)
#             # player left score
#             player_left_text = score_font.render(f'{player_left_score}', False, white)
#             screen.blit(player_left_text, (565, 10))
#             # player right score
#             player_right_text = score_font.render(f'{player_right_score}', False, white)
#             screen.blit(player_right_text, (610, 10))
#             # line in middle of screen
#             pygame.draw.aaline(screen, white, (600,0),(600,900))
#             # if player goes off screen set back to middle
#         if player_left.y < -100 or player_left.y > 910:
#             player_left.y = 350
#         if player_right.y < -100 or player_right.y > 910:
#             player_right.y = 350
#         # display message to quit or continue
#         if player_left_score == 3 or player_right_score == 3:
#             player_left_text = score_font.render('Game Over', False, white)
#             screen.blit(player_left_text, (500, 260))
#             player_left_text = score_font.render('press Y to continue or O to quit', False, white)
#             screen.blit(player_left_text, (255, 360))
#             # set ball speed to begining
#             ball_xdirection = 5
#             ball_ydirection = 5
#         # update window
#         pygame.display.flip()
#         # this means 60 frames per sec
#         clock.tick(60)


#     # this loop runs logic for options menu
#     while options:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#         # switch to player vs player
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_p:
#                 options = False
#                 play = True
#         if event.type == pygame.KEYUP:
#             if event.key == pygame.K_p:
#                 options = False
#                 play = True
#         # switch to player vs computer
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_c:
#                 options = False
#                 play = False
#                 player_vs_c = True
#         if event.type == pygame.KEYUP:
#             if event.key == pygame.K_c:
#                 options = False
#                 play = False
#                 player_vs_c = True
#         # quit
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_n:
#                 pygame.quit()
#                 sys.exit()
#         if event.type == pygame.KEYUP:
#             if event.key == pygame.K_n:
#                 pygame.quit()
#                 sys.exit()
#         # color screen blue
#         screen.fill(blue)
#         pygame.draw.rect(screen, blue, bg)

#         # draw players
#         pygame.draw.rect(screen, white, player_left)
#         player_left.y = 350
#         pygame.draw.rect(screen, white, player_right)
#         player_right.y = 350
#         #player left score
#         player_left_text = score_font.render(f'{player_left_score}', False, white)
#         screen.blit(player_left_text, (565, 10))
#         # player right score
#         player_right_text = score_font.render(f'{player_right_score}', False, white)
#         screen.blit(player_right_text, (610, 10))
#         # center line
#         pygame.draw.aaline(screen, white, (600,0),(600,290))
#         pygame.draw.aaline(screen, white, (600,700),(600,900))

#         button1.draw()
#         button2.draw()
#         button3.draw()

#         # update window
#         pygame.display.flip()
#         # this means 60 frames per sec
#         clock.tick(60)
