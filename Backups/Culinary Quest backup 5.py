import os
import pygame
import time

pygame.init()

pygame.display.set_caption('Culinary Quest')
window_x = 1000
window_y = 600
WIN = pygame.display.set_mode((window_x, window_y))

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
cursor_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','cursor_icon.png'))

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
        self.rect = pygame.Rect(self.x, self.y, self.length, self.height)
        
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

    def checkPressed(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.mouseHovering = True
        else:
            self.mouseHovering = False
        if self.mouseHovering:
            self.pressed = True
        else:
            self.pressed = False
        return self.pressed

    
class Input:
    def __init__(self, x, y, height, length, colourBox, colourText, size):
        self.x = x
        self.y = y
        self.height = height
        self.length = length
        self.colourBox = colourBox
        self.colourText = colourText
        self.size = size
        self.input = ''
        self.selected = False
        self.inputBox = pygame.Rect(x, y, length, height)
    
    def draw(self):
        pygame.draw.rect(WIN, self.colourBox, self.inputBox, 0, 3)
        text_surface = pygame.font.Font(os.path.join('Culinary Quest ASSETS', 'Grotesque.ttf'), self.size).render(self.input, True, self.colourText)
        WIN.blit(text_surface, (self.x+5, self.y+5))

    def inputText(self, event):
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_BACKSPACE:
                self.input = self.input[:-1] #will remove the previous character if backspace
            else:
                self.input += event.unicode #will display the corresponding characters
        WIN.blit((pygame.font.Font(os.path.join('Culinary Quest ASSETS', 'Grotesque.ttf'), self.size).render(self.input, True, self.colourText)), (self.x+5, self.y+5))

    def enter(self):
        print(self.input) #displays correct text on screen
        self.input = ''
    
    def checkSelected(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN: #makes sure the box has been pressed for it to have an input
            if self.inputBox.collidepoint(pygame.mouse.get_pos()):
                self.selected = True
            else:
                self.selected = False
        if self.selected == True: #can only input if the box has been clicked
            self.inputText(event)

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

        #creating objects
        WIN.blit(loginBg_image, bgPosition)
        WIN.blit(gameLogo_image, (410,20))
        loginBg_box = Box(280, 260, 200, 500, login_darkPurple1, True)
        doneBg1_box = Box(130, 490, 80, 370, login_darkPurple1, True)
        createBg1_box = Box(525, 490, 80, 370, login_darkPurple1, True)
        loginLabel_box = Box(370, 270, 37, 300, login_lightPurple1, False)
        usernameLabel_box = Box(300, 330, 37, 150, login_lightPurple1, False)
        passwordLabel_box = Box(300, 400, 37, 150, login_lightPurple1, False)
        done1_button = Button(145, 500, 60, 340, login_lightPurple1, False, False)
        create_button = Button(540, 500, 60, 340, login_lightPurple1, False, False)
        loginLabel_text = Text(495, 275, "Login", white, 20)
        done1_text = Text(265, 505, "Done", white, 35)
        create_text = Text(580, 505, "Create Account", white, 35)
        usernameLabel_text = Text(327, 335, "Username", white, 20)
        passwordLabel_text = Text(327, 405, "Password", white, 20)
        usernameInput_input = Input(600, 330, 37, 150, login_grey1, black, 20)

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pressed = create_button.checkPressed(pygame.mouse.get_pos())
                if pressed:
                    loginLoop = False
                    createLoop = True
            usernameInput_input.checkSelected(event)
        #drawing to screen
        loginBg_box.drawBox()
        doneBg1_box.drawBox()
        createBg1_box.drawBox()
        loginLabel_box.drawBox()
        usernameLabel_box.drawBox()
        passwordLabel_box.drawBox()
        done1_button.drawBox()
        create_button.drawBox()
        loginLabel_text.drawText()
        usernameLabel_text.drawText()
        passwordLabel_text.drawText()
        done1_text.drawText()
        create_text.drawText()
        usernameInput_input.draw()
        
        pygame.display.update()
        clock.tick(FPS)


    while createLoop == True:
        clock.tick(FPS)
        WIN.blit(loginBg_image, bgPosition)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()




main()
        
