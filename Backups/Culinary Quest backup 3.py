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
login_darkPurple1 = pygame.Color(70,73,132)
login_grey1 = pygame.Color(242, 234, 239)
login_red1 = pygame.Color(214, 135, 140)


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
    def __init__(self, x, y, text, colour, size):
        self.x = x
        self.y = y
        self.text = text
        self.colour = colour
        self.size = size

    def drawText(self):
        drawnText = pygame.font.Font(os.path.join('Culinary Quest ASSETS', 'Grotesque.ttf'), self.size).render(self.text, True, self.colour)
        WIN.blit(drawnText, (self.x,self.y))
        

class Box:
    def __init__(self, x, y, height, length, colour, transparent):
        self.x = x
        self.y = y
        self.height = height
        self.length = length
        self.colour = colour
        self.transparent = transparent
        
    def drawBox(self):
        if self.transparent != True:
            pygame.draw.rect(WIN, self.colour, pygame.Rect(self.x, self.y, self.length, self.height) ,0, 3)
        else:
            boxSurface = pygame.Surface((self.length, self.height),pygame.SRCALPHA)
            boxSurface.set_alpha(200)
            drawnBox = pygame.draw.rect(boxSurface, self.colour, boxSurface.get_rect(), 0, 3)
            WIN.blit(boxSurface, (self.x, self.y))
    

class Button(Box):
    def __init__(self, x, y, height, length, colour, transparent, pressed):
        super().__init__(x, y, height, length, colour, transparent)
        self.pressed = pressed

    def checkPressed(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            mousePosition = pygame.mouse.get_pos()
            if pygame.Rect(self.x, self.y, self.length, self.height).collidepoint(mousePosition):
                self.pressed = True
        return self.pressed



pygame.init()

pygame.display.set_caption('Culinary Quest')
WIN = pygame.display.set_mode((window_x, window_y))

def main():
    clock = pygame.time.Clock()
    loginLoop = True
    createLoop = False
    mainLoop = False
    settingsLoop = False
    shopLoop = False
    recipeLoop = False
    burgerLoop = False
    cakeLoop = False
    sushiLoop = False

    while loginLoop == True:
        clock.tick(FPS)

        WIN.blit(loginBg_image, bgPosition)
        WIN.blit(gameLogo_image, (410,20))
        loginBg_box = Box(280, 260, 200, 500, login_darkPurple1, True)
        loginBg_box.drawBox()
        doneBg1_box = Box(130, 490, 80, 370, login_darkPurple1, True)
        doneBg1_box.drawBox()
        createBg1_box = Box(525, 490, 80, 370, login_darkPurple1, True)
        createBg1_box.drawBox()
        loginLabel_box = Box(370, 270, 37, 300, login_lightPurple1, False)
        loginLabel_box.drawBox()
        usernameLabel_box = Box(300, 330, 37, 150, login_lightPurple1, False)
        usernameLabel_box.drawBox()
        passwordLabel_box = Box(300, 400, 37, 150, login_lightPurple1, False)
        passwordLabel_box.drawBox()
        done1_button = Button(130, 490, 37, 150, login_lightPurple1, False, False)
        done1_button.drawBox()
        create_button = Button(525, 490, 37, 150, login_lightPurple1, False, False)
        create_button.drawBox()
        loginLabel_text = Text(495, 275, "Login", white, 20)
        loginLabel_text.drawText()
        usernameLabel_text = Text(327, 335, "Username", white, 20)
        usernameLabel_text.drawText()
        passwordLabel_text = Text(327, 405, "Password", white, 20)
        passwordLabel_text.drawText()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif create_button.checkPressed(event):
                loginLoop = False
                createLoop = True

    while createLoop == True:
        clock.tick(FPS)
        WIN.blit(loginBg_image, bgPosition)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()




main()
        
