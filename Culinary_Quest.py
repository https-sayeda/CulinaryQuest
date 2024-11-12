import os
import pygame
import time
import database

pygame.init()

pygame.display.set_caption('Culinary Quest')
window_x = 1000
window_y = 600
WIN = pygame.display.set_mode((window_x, window_y))

FPS = 60

#Commonly Used Variables
bgPosition = (0,0)
specialCharacters = "!£$%^&*()_+-={['#~.,<>/?|\¬`;:}]@"

#COLOURS
white = (255, 255, 255)
black = pygame.Color(0, 0, 0)

#log in + create account colours
login_lightPurple1 = pygame.Color(179, 137, 164)
login_darkPurple1 = pygame.Color(70,73,132)
login_grey1 = pygame.Color(242, 234, 239)
login_red1 = pygame.Color(214, 135, 140)

#main menu screens 
main_lightPurple1 = pygame.Color(190, 171, 214)
main_lightPurple2 = pygame.Color(192, 153, 218)
main_darkPurple1 = pygame.Color(168, 120, 169)
main_darkPurple2 = pygame.Color(130, 103, 158)
main_darkPurple3 = pygame.Color(110, 54, 98)
main_beige = pygame.Color(232, 220, 211)

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
        drawnText = pygame.font.Font(os.path.join('Culinary Quest ASSETS', 'Aptos.ttf'), self.size).render(self.text, True, self.colour)
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
        self.active = False
        
    def drawBox(self):
        if self.transparent != True:
            pygame.draw.rect(WIN, self.colour, pygame.Rect(self.x, self.y, self.length, self.height) ,0, 3)
        else:
            boxSurface = pygame.Surface((self.length, self.height),pygame.SRCALPHA)
            boxSurface.set_alpha(200)
            pygame.draw.rect(boxSurface, self.colour, boxSurface.get_rect(), 0, 3)
            WIN.blit(boxSurface, (self.x, self.y))

    def getActive(self): return self.active

    def setActive(self): self.active = True

    def setUnactive(self): self.active = False
    
class Button(Box):
    def __init__(self, x, y, height, length, colour, transparent):
        super().__init__(x, y, height, length, colour, transparent)
        self.pressed = False
        self.active = False

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

class ImageButton():
    def __init__(self, x, y, image, size):
        width = image.get_width()
        height = image.get_width
        self.image = pygame.transform.scale(image, (int(width * size), int(height * size)))
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.pressed = False

    def draw(self):
        active = False
        #get mouse position and checks if the button has been clicked
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouseget_pressed()[0] == 1 and self.pressed == False:
                self.pressed = True
                active = True
        
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        #draws image button screen
        WIN.blit(self.image, (self.rect.x, self.rect.y))

        return active #returns whether its been clicked or not




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
        self.text_surface = pygame.font.Font(os.path.join('Culinary Quest ASSETS', 'Aptos.ttf'), self.size).render(self.input, True, self.colourText)
        self.passValidated = False

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
                if self.text_surface.get_width() > self.rect.w - 20:
                    self.input = self.input[:-1]

            if self.censored:
                self.text_surface = pygame.font.Font(os.path.join('Culinary Quest ASSETS', 'Aptos.ttf'), self.size).render(('*' * len(self.input)), True, self.colourText)
            else:
                self.text_surface = pygame.font.Font(os.path.join('Culinary Quest ASSETS', 'Aptos.ttf'), self.size).render(self.input, True, self.colourText)
    
    def draw(self):
        pygame.draw.rect(WIN, self.colourBox, self.rect, 0, 3)
        WIN.blit(self.text_surface, (self.rect.x+5, self.rect.y+5))

    def passValidate(self):
        passwordInput = self.input
        lower = False
        upper = False
        special = False
        if len(passwordInput) >= 8: #makes sure pass is above 8 chars
            for character in passwordInput: #checks all the characters in the password
                if character.islower(): #checks if there's lowercase
                    lower = True
                if character.isupper(): #checks for uppercase
                    upper = True
                if character in specialCharacters: #checks through the string of special chars
                    special = True
            if lower and upper and special:
                self.passValidated = True #if all is met, then it is validated
            else:
                self.passValidated = False #if not, then it is not validated
        else:
            self.passValidated = False
        print(self.passValidated)
        return self.passValidated #returns it to create account loop
    
    def getInput(self): return self.input #getter method for inputs

#SCREENS 

def loginScreen(usernameInput1_input, passwordInput1_input):

    #boxes
    loginBg_box = Box(280, 260, 200, 500, login_darkPurple1, True)
    doneBg1_box = Box(150, 490, 80, 330, login_darkPurple1, True)
    createBg1_box = Box(545, 490, 80, 330, login_darkPurple1, True)
    loginLabel_box = Box(370, 270, 37, 300, login_lightPurple1, False)
    usernameLabel_box = Box(300, 330, 37, 150, login_lightPurple1, False)
    passwordLabel_box = Box(300, 400, 37, 150, login_lightPurple1, False)
    accountError_box = Box(300, 371, 25, 460, login_red1, False)
    #buttons
    done1_button = Button(165, 500, 60, 300, login_lightPurple1, False)
    create_button = Button(560, 500, 60, 300, login_lightPurple1, False)
    #text
    loginLabel_text = Text(495, 275, "Login", white, 22)
    done1_text = Text(285, 510, "Done", white, 27)
    create_text = Text(615, 510, "Create Account", white, 27)
    usernameLabel_text = Text(327, 335, "Username", white, 22)
    passwordLabel_text = Text(327, 405, "Password", white, 22)
    accountError_text = Text(323, 371, "Please enter the correct username / password", white, 21)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
        if event.type == pygame.MOUSEBUTTONDOWN:
            createPressed = create_button.checkPressed(pygame.mouse.get_pos())
            if createPressed:
                create_button.setActive()
            done1Pressed = done1_button.checkPressed(pygame.mouse.get_pos())
            if done1Pressed:
                done1_button.setActive()
        usernameInput1_input.handleEvent(event)
        passwordInput1_input.handleEvent(event)

    #drawing to screen
    WIN.blit(loginBg_image, bgPosition)
    WIN.blit(gameLogo_image, (410,20))

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

    #login system
    create_activate = create_button.getActive() #checks if create account button pressed
    done1_activate = done1_button.getActive() #checks if done button pressed
    accountVerified = False

    if done1_activate == True: #if done button pressed
        userInput = usernameInput1_input.getInput()
        passInput = passwordInput1_input.getInput() #gets the inputs from the box
        accountVerified = database.verifyAccount_main(userInput, passInput) #sends to database file
    if accountVerified == False: #if not verified, then error box
        accountError_box.drawBox()
        accountError_text.drawText()
    elif accountVerified == True: #if verified
        loginBg_box.setActive() #sets box to active
    account_activate = loginBg_box.getActive() #gets the value

    pygame.display.update()

    return create_activate, account_activate #returns to main() to switch / not switch screens

def createScreen(usernameInput2_input, passwordInput2_input, done2_activate):

    #images
    WIN.blit(loginBg_image, bgPosition)
    scaled_gameLogo = pygame.transform.scale(gameLogo_image, (125, 125))
    WIN.blit(scaled_gameLogo, (470,10))
    #boxes
    createBg_box = Box(280, 150, 200, 500, login_darkPurple1, True)
    doneBg2_box = Box(405, 360, 60, 230, login_darkPurple1, True)
    createLabel_box = Box(370, 160, 37, 300, login_lightPurple1, False)
    usernameLabel2_box = Box(300, 230, 37, 150, login_lightPurple1, False)
    passwordLabel2_box = Box(300, 290, 37, 150, login_lightPurple1, False)
    userError_box = Box(340, 430, 37, 350, login_red1, False)
    passError_box = Box(340, 475, 115, 350, login_red1, False)
    #buttons
    done2_button = Button(420, 370, 40, 200, login_lightPurple1, False)
    back_button = Button(40, 70, 70, 100, login_darkPurple1, True)
    #text
    createLabel_text = Text(450, 165, "Create Account", white, 22)
    usernameLabel2_text = Text(327, 235, "Username", white, 22)
    passwordLabel2_text = Text(327, 295, "Password", white, 22)
    done2_text = Text(500, 375, "Done", white, 22)
    back_text = Text(50, 75, "<--", white, 50)
    userError_text = Text(365, 435, "Please enter a unique username", white, 22)
    passError1_text = Text(355, 475, "Passwords must include at least:", white, 22)
    passError2_text = Text(355, 500, "- 8 characters", white, 22)
    passError3_text = Text(355, 520, "- 1 lowercase character", white, 22)
    passError4_text = Text(355, 540, "- 1 uppercase character", white, 22)
    passError5_text = Text(355, 560, "- 1 special symbol", white, 22)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
        if event.type == pygame.MOUSEBUTTONDOWN:
            backPressed = back_button.checkPressed(pygame.mouse.get_pos())
            if backPressed:
                back_button.setActive()
            done2Pressed = done2_button.checkPressed(pygame.mouse.get_pos())
            if done2Pressed: #if the done button is pressed..
                passValidated = passwordInput2_input.passValidate() #makes sure pass matches requirements
                if passValidated:
                    passInput = passwordInput2_input.getInput() #if validated, stored into variable
                userInput = usernameInput2_input.getInput() #username stored
                userValidated = database.validateUser_main(userInput) #sent to database to check if exists
                if userValidated == True and passValidated == True: #if both valid
                    database.addAccount_main(userInput, passInput) #new account created
                    done2_button.setActive() #will only switch screens if account is validated
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
    passError_box.drawBox()
    userError_box.drawBox()
    userError_text.drawText()
    passError1_text.drawText()
    passError2_text.drawText()
    passError3_text.drawText()
    passError4_text.drawText()
    passError5_text.drawText()

    #activating methods to switch screens
    done2_activate = done2_button.getActive()    
    back_activate = back_button.getActive()

    pygame.display.update()

    return done2_activate, back_activate

def mainScreen(search_input):
    WIN.blit(mainBg_image, bgPosition)
    #drawing logo on screen
    scaled_gameLogo = pygame.transform.scale(gameLogo_image, (75, 75))
    #box object creation
    recipeBg_box = Box(120, 170, 425, 750, main_lightPurple1, True)
    overhead_box = Box(0, 0, 75, 1000, main_darkPurple1, True)
    levelNeeded_box = Box(240, 15, 40, 270, main_darkPurple3, False)
    currentLevel_box = Box(160, 15, 40, 120, main_darkPurple2, False)
    searchLabel_box = Box(120, 100, 37, 120, main_lightPurple2, False)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
        search_input.handleEvent(event)

    #drawing onto screen
    recipeBg_box.drawBox()
    overhead_box.drawBox()
    levelNeeded_box.drawBox()
    currentLevel_box.drawBox()
    WIN.blit(scaled_gameLogo, (30,0))
    searchLabel_box.drawBox()
    search_input.draw()

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
    usernameInput2_input = Input(480, 230, 37, 280, black, 20, False)
    passwordInput2_input = Input(480, 290, 37, 280, black, 20, True)
    search_input = Input(240, 100, 37, 570, black, 20, False)
    
    while run:
        while loginLoop == True:
            createPressed, accountActivated = loginScreen(usernameInput1_input, passwordInput1_input)
            if createPressed == True:
                loginLoop = False
                createLoop = True
            if accountActivated == True:
                loginLoop = False
                mainLoop = True

        while createLoop == True:
            done2_activate = False
            accountVerified, backPressed = createScreen(usernameInput2_input, passwordInput2_input, done2_activate)
            if backPressed:
                createLoop = False
                loginLoop = True
                done2_activate = False

            if accountVerified:
                createLoop = False
                loginLoop = True
                done2_activate = False

        while mainLoop == True:
            mainScreen(search_input)

main()
        
