import pygame, sys

pygame.init()
screen_width = 1200
screen_height = 900
screen = pygame.display.set_mode((screen_width, screen_height))
# play = False
# options = True
score_font = pygame.font.Font('freesansbold.ttf', 60)
class Button:
    def __init__(self,text,width,height,pos):
        self.shape = pygame.Rect(pos,(width, height))
        self.color = 'black'
        self.text = score_font.render(text, True, 'pink')
        self.text_rect = self.text.get_rect(center = self.shape.center)
        self.pressed = False
    def draw(self):
        pygame.draw.rect(screen, self.color , self.shape)
        screen.blit(self.text, self.text_rect)
        self.check_click()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.shape.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.pressed = True
            else:
                if self.pressed == True:
                    # options = False
                    # play = True
                    print('y')
                    self.pressed = False
