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
specialCharacters = "!£$%^&*()_+-={['#~.,<>/?|\¬`;:}]"

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
            pygame.draw.rect(boxSurface, self.colour, boxSurface.get_rect(), 0, 3)
            WIN.blit(boxSurface, (self.x, self.y))
    
class Button(Box):
    def __init__(self, x, y, height, length, colour, transparent):
        super().__init__(x, y, height, length, colour, transparent)
        self.pressed = False

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
    def __init__(self, x, y, height, length, colourText, size, censored):
        self.x = x
        self.y = y
        self.height = height
        self.length = length
        self.colourText = colourText
        self.size = size
        self.colourBox = login_grey1
        self.input = ''
        self.selected = False
        self.rect = pygame.Rect(x, y, length, height)
        self.censored = censored
        self.text_surface = pygame.font.Font(os.path.join('Culinary Quest ASSETS', 'Grotesque.ttf'), self.size).render(self.input, True, self.colourText)
    
    def handleEvent(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.selected = True
            else:
                self.selected = False
        if event.type == pygame.KEYDOWN and self.selected:
            if event.key == pygame.K_RETURN:
                print(self.input)
                self.input = ''
            if event.key == pygame.K_BACKSPACE:
                self.input = self.input[:-1] #will remove the previous character if backspace
            else:
                self.input += event.unicode #will display the corresponding characters

            if self.censored:
                self.text_surface = pygame.font.Font(os.path.join('Culinary Quest ASSETS', 'Grotesque.ttf'), self.size).render(('*' * len(self.input)), True, self.colourText)
            else:
                self.text_surface = pygame.font.Font(os.path.join('Culinary Quest ASSETS', 'Grotesque.ttf'), self.size).render(self.input, True, self.colourText)
    
    def draw(self):
        
        pygame.draw.rect(WIN, self.colourBox, self.rect, 0, 3)
        WIN.blit(self.text_surface, (self.rect.x+5, self.rect.y+5))

class PassInput(Input):
    def __init__(self, x, y, height, length, colourText, size, censored):
        super().__init__(x, y, height, length, colourText, size, censored)
        self.colourBox = login_grey1
        self.input = ''
        self.selected = False
        self.rect = pygame.Rect(x, y, length, height)
        self.censored = censored
        self.text_surface = pygame.font.Font(os.path.join('Culinary Quest ASSETS', 'Grotesque.ttf'), self.size).render(self.input, True, self.colourText)
        self.validated = False

    def passValidate(self):
        passwordInput = self.input
        if len(passwordInput) >= 8:
            for character in passwordInput:
                if character.islower():
                    if character.isupper():
                        if character in specialCharacters:
                            self.validated = True
        else:
            self.validated = False
        return self.validated


class UserInput(Input):
    def __init__(self, x, y, height, length, colourText, size, censored):
        super().__init__(x, y, height, length, colourText, size, censored)
        self.colourBox = login_grey1
        self.input = ''
        self.selected = False
        self.rect = pygame.Rect(x, y, length, height)
        self.censored = censored
        self.text_surface = pygame.font.Font(os.path.join('Culinary Quest ASSETS', 'Grotesque.ttf'), self.size).render(self.input, True, self.colourText)

#SCREENS 

def loginScreen(usernameInput1_input, passwordInput1_input):

    WIN.blit(loginBg_image, bgPosition)
    WIN.blit(gameLogo_image, (410,20))
    loginBg_box = Box(280, 260, 200, 500, login_darkPurple1, True)
    doneBg1_box = Box(150, 490, 80, 330, login_darkPurple1, True)
    createBg1_box = Box(545, 490, 80, 330, login_darkPurple1, True)
    loginLabel_box = Box(370, 270, 37, 300, login_lightPurple1, False)
    usernameLabel_box = Box(300, 330, 37, 150, login_lightPurple1, False)
    passwordLabel_box = Box(300, 400, 37, 150, login_lightPurple1, False)
    done1_button = Button(165, 500, 60, 300, login_lightPurple1, False)
    create_button = Button(560, 500, 60, 300, login_lightPurple1, False)
    loginLabel_text = Text(495, 275, "Login", white, 20)
    done1_text = Text(285, 510, "Done", white, 25)
    create_text = Text(615, 510, "Create Account", white, 25)
    usernameLabel_text = Text(327, 335, "Username", white, 20)
    passwordLabel_text = Text(327, 405, "Password", white, 20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            createPressed = create_button.checkPressed(pygame.mouse.get_pos())
            if createPressed:
                return createPressed
        usernameInput1_input.handleEvent(event)
        passwordInput1_input.handleEvent(event)

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
    usernameInput1_input.draw()
    passwordInput1_input.draw()
    
    pygame.display.update()

def createScreen(usernameInput2_input, passwordInput2_input):

    WIN.blit(loginBg_image, bgPosition)
    scaled_gameLogo = pygame.transform.scale(gameLogo_image, (125, 125))
    WIN.blit(scaled_gameLogo, (470,10))
    createBg_box = Box(280, 150, 200, 500, login_darkPurple1, True)
    doneBg2_box = Box(415, 360, 60, 230, login_darkPurple1, True)
    createLabel_box = Box(370, 160, 37, 300, login_lightPurple1, False)
    usernameLabel2_box = Box(300, 230, 37, 150, login_lightPurple1, False)
    passwordLabel2_box = Box(300, 290, 37, 150, login_lightPurple1, False)
    createLabel_text = Text(450, 165, "Create Account", white, 20)
    usernameLabel2_text = Text(327, 235, "Username", white, 20)
    passwordLabel2_text = Text(327, 295, "Password", white, 20)
    done2_text = Text(505, 375, "Done", white, 20)
    done2_button = Button(430, 370, 40, 200, login_lightPurple1, False)
    back_button = Button(40, 70, 70, 100, login_darkPurple1, True)
    back_text = Text(50, 75, "<--", white, 40)
    passError_box = Box(500, 360, 60, 230, login_red1, False)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            backPressed = back_button.checkPressed(pygame.mouse.get_pos())
            if backPressed:
                return backPressed
            done2Pressed = done2_button.checkPressed(pygame.mouse.get_pos())
            if done2Pressed:
                passValidated = passwordInput2_input.passValidate()
                if passValidated != True:
                    passError_box.drawBox()
        usernameInput2_input.handleEvent(event)
        passwordInput2_input.handleEvent(event)

    createBg_box.drawBox()
    doneBg2_box.drawBox()
    createLabel_box.drawBox()
    usernameLabel2_box.drawBox()
    passwordLabel2_box.drawBox()
    createLabel_text.drawText()
    usernameLabel2_text.drawText()
    passwordLabel2_text.drawText()
    done2_button.drawBox()
    done2_text.drawText()
    back_button.drawBox()
    back_text.drawText()
    usernameInput2_input.draw()
    passwordInput2_input.draw()

    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    clock.tick(FPS)
    run = True
    #loops
    loginLoop = True
    createLoop = False
    mainLoop = False
    settingsLoop = False
    shopLoop = False
    recipeLoop = False
    burgerLoop = False
    cakeLoop = False
    sushiLoop = False
    #input boxes
    usernameInput1_input = Input(480, 330, 37, 280, black, 20, False)
    passwordInput1_input = Input(480, 400, 37, 280, black, 20, True)
    usernameInput2_input = UserInput(480, 230, 37, 280, black, 20, False)
    passwordInput2_input = PassInput(480, 290, 37, 280, black, 20, True)

    while run:
        while loginLoop == True:
            createPressed = loginScreen(usernameInput1_input, passwordInput1_input)
            if createPressed:
                loginLoop = False
                createLoop = True

        while createLoop == True:
            backPressed = createScreen(usernameInput2_input, passwordInput2_input)
            if backPressed:
                createLoop = False
                loginLoop = True




main()
        
