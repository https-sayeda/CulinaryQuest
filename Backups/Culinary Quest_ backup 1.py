import os
import pygame
import time

window_x = 1000
window_y = 600
FPS = 60

#Commonly Used Variables
bgPosition = (0,0)

#COLOURS
white = (255, 255, 255)
black = pygame.Color(0, 0, 0)

login_lightPurple1 = pygame.Color(179, 137, 164)
login_lightPurple2 = pygame.Color(155, 109, 127)
login_darkPurple1 = pygame.Color(70,73,132)
login_darkPurple2 = pygame.Color(58, 60, 110)
login_grey1 = pygame.Color(242, 234, 239)
login_grey2 = pygame.Color(253, 253, 253)
login_red1 = pygame.Color(214, 135, 140)
login_red2 = pygame.Color(201, 99, 106)

#IMAGES
loginBg_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','login1_background.png'))
mainBg_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','main1_background.png'))
gameBg_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','game1_background.png'))
gameLogo_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','logo.png'))

burgerIcon_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','burger_icon.png'))
cakeIcon_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','cake_icon.png'))
sushiIcon_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','sushi_icon.png'))
halalIcon_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','halal_icon.png'))
vegetarianIcon_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','vegetarian_icon.png'))
veganIcon_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','vegan_icon.png'))

#CLASSES

class Text:
    def __init__(self, x, y, text, colour, font):
        self.x = x
        self.y = y
        self.text = text
        self.colour = colour
        self.font = font

    def drawText(self):
        drawnText = self.font.render(self.text, True, self.colour)
        WIN.blit(drawnText, (self.x,self.y))

class Box:
    def __init__(self, x, y, height, length, colour):
        self.x = x
        self.y = y
        self.height = height
        self.length = length
        self.colour = colour
        
    def drawBox(self):
     pygame.draw.rect(WIN, self.colour, pygame.Rect(self.x, self.y, self.length, self.height) ,0, 3)
     pygame.display.flip()

pygame.init()

pygame.display.set_caption('Culinary Quest')
WIN = pygame.display.set_mode((window_x, window_y))

def draw_window():
    WIN.fill(white)
    WIN.blit(loginBg_image, bgPosition)
    loginLabel_box = Box(window_x/2, window_y/2, 40, 30, login_lightPurple1)
    loginLabel_box.drawBox()
    loginLabel_text = Text(window_x/2, window_y/2, "Login", white, (pygame.font.SysFont("Grotesque", 11)))
    loginLabel_text.drawText()
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()
    
    pygame.quit()

main()
        
