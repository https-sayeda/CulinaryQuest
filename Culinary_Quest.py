import os
import pygame
import time
import database
import sys

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
main_brightPurple = pygame.Color(112, 48, 160)
main_beige = pygame.Color(232, 220, 211)
main_green = pygame.Color(68, 166, 84)

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
shopIcon_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','shop_icon.png'))
settingsIcon_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','settings_icon.png'))
filterIcon_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','filter_icon.png'))
checkmarkIcon_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','checkmark_icon.png'))
cheeseFondueIcon_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','cheeseFondue_icon.png'))
croissantIcon_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','croissant_icon.png'))
tofuIcon_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','tofu_icon.png'))


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
        self.image = image
        width = image.get_width()
        height = image.get_width()
        self.image = pygame.transform.scale(image, (int(width * size), int(height * size)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.pressed = False
        self.active = False

    def draw(self):
        #draws image button screen
        WIN.blit(self.image, (self.rect.x, self.rect.y))
    
    def changePosition(self, newX, newY):
        #changes position of the button if needed
        WIN.blit(self.image, (newX, newY))
        self.rect.topleft = (newX, newY)

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

    def getActive(self): return self.active
    def setActive(self): self.active = True
    def setUnactive(self): self.active = False

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
                self.selected = False
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

def loginScreen(usernameInput1_input, passwordInput1_input, loginLoop, createLoop, mainLoop):

    userInput = "None"
    #creating objects to display
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

    while loginLoop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                createPressed = create_button.checkPressed(pygame.mouse.get_pos())
                if createPressed: #if create account button pressed..
                    loginLoop = False
                    createLoop = True #set to true while loginLoop is false so it can switch screens
            if event.type == pygame.MOUSEBUTTONDOWN:
                done1Pressed = done1_button.checkPressed(pygame.mouse.get_pos())
                if done1Pressed:
                    userInput = usernameInput1_input.getInput()
                    passInput = passwordInput1_input.getInput() #gets the inputs from the box
                    accountVerified = database.verifyAccount_main(userInput, passInput) #sends to database file
                    if accountVerified == False: #if account is not verified
                        accountError_box.setActive() #sets box to active so it can be drawn
                    elif accountVerified == True: #if it is verified
                        loginLoop = False #sets loop to false so it can switch screens
                        mainLoop = True #sets loop to true so it can switch to the main screen
            
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

        accountError_active = accountError_box.getActive() 
        if accountError_active: #if error box active
            accountError_box.drawBox() #drawn onto screen
            accountError_text.drawText()

        pygame.display.update()

    return loginLoop, createLoop, mainLoop, userInput #returns to main() to switch / not switch screens

def createScreen(usernameInput2_input, passwordInput2_input, createLoop, loginLoop):

    #creating objects to display
    #images
    scaled_gameLogo = pygame.transform.scale(gameLogo_image, (125, 125))
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

    while createLoop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                backPressed = back_button.checkPressed(pygame.mouse.get_pos())
                if backPressed:
                    createLoop = False
                    loginLoop = True #if back pressed, will return to login screen
                done2Pressed = done2_button.checkPressed(pygame.mouse.get_pos())
                if done2Pressed: #if the done button is pressed..
                    passValidated = passwordInput2_input.passValidate() #makes sure pass matches requirements
                    if passValidated:
                        passInput = passwordInput2_input.getInput() #if validated, stored into variable
                    else:
                        passError_box.setActive() #if not validated, error box is activated
                    userInput = usernameInput2_input.getInput() #username stored
                    userValidated = database.validateUser_main(userInput) #sent to database to check if exists
                    if userValidated == True and passValidated == True: #if both valid
                        database.addAccount_main(userInput, passInput) #new account created
                        createLoop = False  #will only switch screens if account is validated
                        loginLoop = True
                    elif userValidated != True: #if username not validated..
                        userError_box.setActive() #error box is activated
            usernameInput2_input.handleEvent(event)
            passwordInput2_input.handleEvent(event)

        #drawing the objects
        WIN.blit(loginBg_image, bgPosition)
        WIN.blit(scaled_gameLogo, (470,10))
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

        passError_active = passError_box.getActive()
        userError_active = userError_box.getActive()
        if passError_active: #if password error box is active, it is drawn onto screen
            passError_box.drawBox()
            passError1_text.drawText()
            passError2_text.drawText()
            passError3_text.drawText()
            passError4_text.drawText()
            passError5_text.drawText()
        if userError_active: #if username error box is active, it is drawn onto screen
            userError_box.drawBox()
            userError_text.drawText()

        pygame.display.update()

    return createLoop, loginLoop

def mainScreen(search_input, mainLoop, shopLoop, settingsLoop, recipeLoop, recipeChosen, username):

    #retrieving from database
    current_level = str(database.getData_main(username, "current_level"))
    current_points = str(100-(database.getData_main(username, "current_points")))

    #scaling the game logo
    scaled_gameLogo = pygame.transform.scale(gameLogo_image, (75, 75))
    scaled_checkmarkIcon = pygame.transform.scale(checkmarkIcon_image, (30, 30))
    #box object creation
    recipeBg_box = Box(120, 170, 425, 750, main_lightPurple1, True)
    overhead_box = Box(0, 0, 75, 1000, main_darkPurple1, True)
    pointsNeeded_box = Box(240, 15, 40, 300, main_darkPurple3, False)
    currentLevel_box = Box(160, 15, 40, 90, main_darkPurple2, False)
    recipeBg1_box = Box(130, 180, 180, 200, main_lightPurple2, False)
    recipeBg2_box = Box(340, 180, 180, 200, main_lightPurple2, False)
    recipeBg3_box = Box(550, 180, 180, 200, main_lightPurple2, False)
    recipeBg4_box = Box(130, 380, 180, 200, main_lightPurple2, False)
    recipeBg5_box = Box(340, 380, 180, 200, main_lightPurple2, False)
    recipeBg6_box = Box(550, 380, 180, 200, main_lightPurple2, False)
    filterBg_box = Box(820, 100, 37, 50, login_grey1, False)
    filtertoolBg_box = Box(670, 150, 380, 300, login_grey1, False)
    dietaryBg_box = Box(690, 160, 33, 265, main_darkPurple2, False)
    halalBg_box = Box(690, 200, 33, 130, main_lightPurple1, False)
    vegeterianBg_box = Box(690, 238, 33, 130, main_lightPurple1, False)
    veganBg_box = Box(690, 276, 33, 130, main_lightPurple1, False)
    difficultyBg_box = Box(690, 316, 33, 265, main_darkPurple2, False)
    easyBg_box = Box(690, 356, 33, 130, main_lightPurple1, False)
    mediumBg_box = Box(690, 394, 33, 130, main_lightPurple1, False)
    hardBg_box = Box(690, 432, 33, 130, main_lightPurple1, False)
    errorBg_box = Box(350, 230, 50, 300, login_red1, False)

    #text object creation
    searchLabel_text = Text(150, 105, "Search", white, 22)
    error_text = Text(405, 240, "Recipe not found", white, 25)
    dietary_text = Text(720, 165, "Dietary Requirements", white, 22)
    halal_text = Text(727, 205, "Halal", white, 22)
    vegetarian_text = Text(703, 243, "Vegetarian", white, 22)
    vegan_text = Text(725, 281, "Vegan", white, 22)
    difficulty_text = Text(775, 321, "Difficulty", white, 22)
    easy_text = Text(732, 361, "Easy", white, 22)
    medium_text = Text(715, 399, "Medium", white, 22)
    hard_text = Text(732, 437, "Hard", white, 22)
    filterText_text = Text(800, 477, "Filter", white, 22)
    level_text = Text(170, 20, "Level " + current_level, white, 22)
    pointsNeeded_text = Text(263, 20, current_points + " points for the next level", white, 22)

    #button creation
    search_button = Button(120, 100, 37, 120, main_lightPurple2, False)
    halal_button = Button(840, 200, 33, 33, white, False)
    vegetarian_button = Button(840, 238, 33, 33, white, False)
    vegan_button = Button(840, 276, 33, 33, white, False)
    easy_button = Button(840, 356, 33, 33, white, False)
    medium_button = Button(840, 394, 33, 33, white, False)
    hard_button = Button(840, 432, 33, 33, white, False)
    filterText_button = Button(690, 472, 33, 265, main_brightPurple, False)

    #image button creation
    shop_button = ImageButton(600, 10, shopIcon_image, 1)
    settings_button = ImageButton(850, 15, settingsIcon_image, 1)
    burger_button = ImageButton(110, 155, burgerIcon_image, 0.45)
    cake_button = ImageButton(355, 190, cakeIcon_image, 0.3)
    sushi_button = ImageButton(570, 180, sushiIcon_image, 0.3)
    filter_button = ImageButton(830, 102, filterIcon_image, 0.7)
    cheeseFondue_button = ImageButton(145, 390, cheeseFondueIcon_image, 0.3)
    croissant_button = ImageButton(355, 390, croissantIcon_image, 0.3)
    tofu_button = ImageButton(570, 390, tofuIcon_image, 0.3)


    #this will hold the dietary requirements that have been selected via the filter tool, the values 
    #will change depending on what the user will select
    dietaryOption = [0, 0, 0]
    difficultyOption = "None"
    activeRecipes = [] #will hold the number of recipes that are active
    recipeBoxes = [recipeBg1_box, recipeBg2_box, recipeBg3_box, recipeBg4_box, recipeBg5_box, recipeBg6_box] #stores all the recipe background boxes
    recipeCoordinates_x = [145, 355, 570, 145, 355]
    recipeCoordinates_y = [180, 190, 180, 390, 390]


    while mainLoop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                shopPressed = shop_button.checkPressed(pygame.mouse.get_pos()) #checks if its been pressed
                if shopPressed:
                    mainLoop = False
                    shopLoop = True
                settingsPressed = settings_button.checkPressed(pygame.mouse.get_pos())
                if settingsPressed:
                    mainLoop = False
                    settingsLoop = True
                burgerPressed = burger_button.checkPressed(pygame.mouse.get_pos())
                if burgerPressed:
                    mainLoop = False
                    recipeLoop = True
                    recipeChosen = "burger"
                cakePressed = cake_button.checkPressed(pygame.mouse.get_pos())
                if cakePressed:
                    mainLoop = False
                    recipeLoop = True
                    recipeChosen = "cake"
                sushiPressed = sushi_button.checkPressed(pygame.mouse.get_pos())
                if sushiPressed:
                    mainLoop = False
                    recipeLoop = True
                    recipeChosen = "sushi"
                cheeseFonduePressed = cheeseFondue_button.checkPressed(pygame.mouse.get_pos())
                if cheeseFonduePressed:
                    mainLoop = False
                    recipeLoop = True
                    recipeChosen = "cheese fondue"
                croissantPressed = croissant_button.checkPressed(pygame.mouse.get_pos())
                if croissantPressed:
                    mainLoop = False
                    recipeLoop = True
                    recipeChosen = "croissant"
                tofuPressed = tofu_button.checkPressed(pygame.mouse.get_pos())
                if tofuPressed:
                    mainLoop = False
                    recipeLoop = True
                    recipeChosen = "tofu"
                filterPressed = filter_button.checkPressed(pygame.mouse.get_pos()) #checks if it's been pressed
                if filterPressed: #if it has..
                    filterActive = filter_button.getActive() #checks if the button has been pressed before
                    if filterActive != True: #if it hasn't (the pop up is not on the screen)
                        filter_button.setActive() #the button is active
                    else: #if it is (the pop up is on the screen)
                        filter_button.setUnactive() #sets to unactive so the pop up disappears
                #when one of the filtering options are pressed
                halalPressed = halal_button.checkPressed(pygame.mouse.get_pos()) #checks if pressed..
                if halalPressed:
                    halalActive = halal_button.getActive() #if it is, gets value of if its active or not
                    if halalActive != True: #if it isnt already active
                        halal_button.setActive()
                        #sets to active so the filter can be applied and checkmark can appear
                        dietaryOption[0] = 1 #stores whether halal has been selected
                    else: #if its already active
                        halal_button.setUnactive() 
                        #sets to unactive (check mark disappears and filter not applied 
                        # if user changes their mind)
                        dietaryOption[0] = 0
                vegetarianPressed = vegetarian_button.checkPressed(pygame.mouse.get_pos())
                if vegetarianPressed:
                    vegetarianActive = vegetarian_button.getActive()
                    if vegetarianActive != True:
                        vegetarian_button.setActive()
                        dietaryOption[1] = 1
                    else:
                        vegetarian_button.setUnactive()
                        dietaryOption[1] = 0
                veganPressed = vegan_button.checkPressed(pygame.mouse.get_pos())
                if veganPressed:
                    veganActive = vegan_button.getActive()
                    if veganActive != True:
                        vegan_button.setActive()
                        dietaryOption[2] = 1
                    else:
                        vegan_button.setUnactive()
                        dietaryOption[2] = 0
                easyPressed = easy_button.checkPressed(pygame.mouse.get_pos())
                if easyPressed:
                    easyActive = easy_button.getActive()
                    if easyActive != True:
                        easy_button.setActive()
                        difficultyOption = "Easy" #sets the difficulty chosen to easy
                        medium_button.setUnactive()
                        hard_button.setUnactive()
                    else:
                        easy_button.setUnactive()
                        difficultyOption = "None" #if unselected, it will go back to None
                mediumPressed = medium_button.checkPressed(pygame.mouse.get_pos())
                if mediumPressed:
                    mediumActive = medium_button.getActive()
                    if mediumActive != True:
                        medium_button.setActive()
                        difficultyOption = "Medium"
                        easy_button.setUnactive()
                        hard_button.setUnactive()
                    else:
                        medium_button.setUnactive()
                        difficultyOption = "None"
                hardPressed = hard_button.checkPressed(pygame.mouse.get_pos())
                if hardPressed:
                    hardActive = hard_button.getActive()
                    if hardActive != True:
                        hard_button.setActive()
                        difficultyOption = "Hard"
                        easy_button.setUnactive()
                        medium_button.setUnactive()
                    else:
                        hard_button.setUnactive()
                        difficultyOption = "None"
                filterTextpressed = filterText_button.checkPressed(pygame.mouse.get_pos())
                if filterTextpressed:
                    burger_button.setUnactive()
                    cake_button.setUnactive()
                    sushi_button.setUnactive()
                    cheeseFondue_button.setUnactive()
                    croissant_button.setUnactive()
                    tofu_button.setUnactive()
                    errorBg_box.setUnactive()
                    activeRecipes = []
                    dietaryInput = False
                    for i in range(len(dietaryOption)): #checks if any of the items have been set to true
                        if dietaryOption[i] == 1:
                            dietaryInput = True #if it has, then a dietary option has been selected
                    if dietaryInput == True or difficultyOption != "None": #ensures at least one option selected
                        filter_button.setUnactive() #removes the pop up menu
                        halal_button.setUnactive()
                        vegetarian_button.setUnactive()
                        vegan_button.setUnactive()
                        easy_button.setUnactive()
                        medium_button.setUnactive()
                        hard_button.setUnactive()
                        recipeFound, recipeName = database.filterRecipe_main(dietaryOption, difficultyOption, dietaryInput)
                        #the values from the database are returned
                        dietaryOption = [0, 0, 0]
                        difficultyOption = "None"
                        if recipeFound: #if a recipe has been found
                            for i in range (len(recipeName)): #goes through the list of recipe names
                                if recipeName[i] == "burger": #checks if it is a recipe
                                    burger_button.setActive() #sets that recipe button to active
                                    activeRecipes.append(burger_button)
                                elif recipeName[i] == "cake":
                                    cake_button.setActive()
                                    activeRecipes.append(cake_button)
                                elif recipeName[i] == "sushi":
                                    sushi_button.setActive()
                                    activeRecipes.append(sushi_button)
                                elif recipeName[i] == "cheese fondue":
                                    cheeseFondue_button.setActive()
                                    activeRecipes.append(cheeseFondue_button)
                                elif recipeName[i] == "croissant":
                                    croissant_button.setActive()
                                    activeRecipes.append(croissant_button)
                                elif recipeName[i] == "tofu":
                                    tofu_button.setActive()
                                    activeRecipes.append(tofu_button)
                                
                        else: #if no recipes have been found
                            errorBg_box.setActive() #error button is set to active so it can be displayed

                searchPressed = search_button.checkPressed(pygame.mouse.get_pos())
                if searchPressed: #if search button is pressed
                    burger_button.setUnactive()
                    cake_button.setUnactive()
                    sushi_button.setUnactive()
                    cheeseFondue_button.setUnactive()
                    croissant_button.setUnactive()
                    tofu_button.setUnactive()
                    errorBg_box.setUnactive()
                    activeRecipes = []
                    searchRecipe = search_input.getInput() #retrieves search input
                    recipeFound, recipeName = database.searchRecipe_main(searchRecipe) #sends to database functions
                    if recipeFound: #if the recipe is found
                        if recipeName == "burger": #checks which recipe it is
                            burger_button.setActive() #actives the correct button so that it will appear
                            activeRecipes.append(burger_button)
                        elif recipeName == "cake":
                            cake_button.setActive()
                            activeRecipes.append(cake_button)
                        elif recipeName == "sushi":
                            sushi_button.setActive()
                            activeRecipes.append(sushi_button)
                        elif recipeName == "cheese fondue":
                            cheeseFondue_button.setActive()
                            activeRecipes.append(cheeseFondue_button)
                        elif recipeName == "croissant":
                            croissant_button.setActive()
                            activeRecipes.append(croissant_button)
                        elif recipeName == "tofu":
                            tofu_button.setActive()
                            activeRecipes.append(tofu_button)
                    else: #if there recipe isnt found
                        errorBg_box.setActive() #the error box is set to active so it appears
                
            search_input.handleEvent(event)

        #drawing onto screen
        WIN.blit(mainBg_image, bgPosition)
        recipeBg_box.drawBox()
        overhead_box.drawBox()
        pointsNeeded_box.drawBox()
        currentLevel_box.drawBox()
        WIN.blit(scaled_gameLogo, (30,0))
        search_button.drawBox()
        search_input.draw()
        searchLabel_text.drawText()
        shop_button.draw()
        settings_button.draw()
        filterBg_box.drawBox()
        filter_button.draw()
        level_text.drawText()
        pointsNeeded_text.drawText()
        
        errorActive = errorBg_box.getActive() #gets the value of the button / box being active
        if len(activeRecipes) == 0 and errorActive == False :
        #if they are all unactive (there hasn't been a search or filter query)
            for x in range(len(recipeBoxes)):
                recipeBoxes[x].drawBox()
            burger_button.draw()
            cake_button.draw()
            sushi_button.draw() #they are all drawn to the screen except the error box
            cheeseFondue_button.draw()
            croissant_button.draw()
            tofu_button.draw()
        if len(activeRecipes) != 0 and errorActive == False: 
            #if they aren't all unactive
            for x in range(len(activeRecipes)): #draw the boxes based on the number of active recipes
                recipeBoxes[x].drawBox()
            for i in range(len(activeRecipes)): 
                if len(activeRecipes) == 1: #if there is only one active
                    if activeRecipes[i] == burger_button: #if the first one is burger
                        burger_button.draw() #draw burger 
                        #(the burger image doesn't work with the position below)
                    else:
                        activeRecipes[i].changePosition(145,180) #if it isn't burger, draw
                if len(activeRecipes) > 1: #if there are more than one active recipes
                    if activeRecipes[i] == burger_button and i == 0: #if it recipe is burger and it's 1st
                        burger_button.draw() #draw it
                    else:
                        activeRecipes[i].changePosition(recipeCoordinates_x[i], recipeCoordinates_y[i])
        if errorActive: #if only the error box is active
                errorBg_box.drawBox() #it gets drawn
                error_text.drawText()

        filterActive = filter_button.getActive() # gets the value of whether its active
        if filterActive: #if it is..
            filtertoolBg_box.drawBox() #draws the box
            dietaryBg_box.drawBox()
            dietary_text.drawText()
            halalBg_box.drawBox()
            halal_text.drawText()
            halal_button.drawBox()
            vegeterianBg_box.drawBox()
            vegetarian_text.drawText()
            vegetarian_button.drawBox()
            veganBg_box.drawBox()
            vegan_text.drawText()
            vegan_button.drawBox()
            difficultyBg_box.drawBox()
            difficulty_text.drawText()
            easyBg_box.drawBox()
            easy_text.drawText()
            easy_button.drawBox()
            mediumBg_box.drawBox()
            medium_text.drawText()
            medium_button.drawBox()
            hardBg_box.drawBox()
            hard_text.drawText()
            hard_button.drawBox()
            filterText_button.drawBox()
            filterText_text.drawText()

        #checks if filter option buttons have been pressed
        halalActive = halal_button.getActive()
        vegetarianActive = vegetarian_button.getActive()
        veganActive = vegan_button.getActive()
        easyActive = easy_button.getActive()
        mediumActive = medium_button.getActive()
        hardActive = hard_button.getActive()
        if halalActive: #if the button is active
            WIN.blit(scaled_checkmarkIcon, (845,198)) #the checkmark is displayed
        if vegetarianActive:
            WIN.blit(scaled_checkmarkIcon, (845,236))
        if veganActive:
            WIN.blit(scaled_checkmarkIcon, (845,275))
        if easyActive: #if the button is active
            WIN.blit(scaled_checkmarkIcon, (845,354)) #the checkmark is displayed
        if mediumActive:
            WIN.blit(scaled_checkmarkIcon, (845,392))
        if hardActive:
            WIN.blit(scaled_checkmarkIcon, (845,430))

        pygame.display.update()

    return mainLoop, shopLoop, settingsLoop, recipeLoop, recipeChosen

def shopScreen(mainLoop, shopLoop):
    scaled_gameLogo = pygame.transform.scale(gameLogo_image, (125, 125))

    #box object creation
    shopBg_box = Box(120, 150, 425, 750, main_lightPurple1, True)
    shopLabel_box = Box(410, 160, 30, 200, main_darkPurple2, False)

    #text object creation
    back_text = Text(80, 55, "<--", white, 50)
    shopLabel_text = Text(485, 162, "Shop", white, 22)

    #button object creation
    back_button = Button(65, 50, 70, 100, main_darkPurple2, False)

    while shopLoop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                backPressed = back_button.checkPressed(pygame.mouse.get_pos()) #checks if its been pressed
                if backPressed:
                    shopLoop = False
                    mainLoop = True
            
        #drawing onto screen
        WIN.blit(mainBg_image, bgPosition)
        WIN.blit(scaled_gameLogo, (450,10))
        shopBg_box.drawBox()
        back_button.drawBox()
        back_text.drawText()
        shopLabel_box.drawBox()
        shopLabel_text.drawText()

        pygame.display.update()

    return mainLoop, shopLoop

def settingsScreen(mainLoop, settingsLoop, oldPassInput_input, newPassInput_input, username):
    scaled_gameLogo = pygame.transform.scale(gameLogo_image, (125, 125))
    scaled_checkmarkIcon = pygame.transform.scale(checkmarkIcon_image, (35, 35))

    #box object creation
    settingsBg_box = Box(120, 150, 425, 750, main_lightPurple1, True)
    settingsLabel_box = Box(405, 160, 30, 200, main_darkPurple2, False)
    changePassLabel_box = Box(140, 200, 30, 210, main_darkPurple2, False)
    volumeLabel_box = Box(140, 360, 30, 210, main_darkPurple2, False)
    measurementLabel_box = Box(140, 460, 30, 210, main_darkPurple2, False)
    oldPasswordLabel_box = Box(140, 250, 30, 210, main_darkPurple3, False)
    newPasswordLabel_box = Box(140, 310, 30, 210, main_darkPurple3, False)
    errorBg1_box = Box(655, 180, 30, 200, login_red1, False)
    errorBg2_box = Box(655, 230, 130, 200, login_red1, False)
    passwordChangedBg_box = Box(655, 180, 30, 200, main_green, False)
    metricLabel_box = Box(140, 520, 30, 200, main_darkPurple3, False)
    UScustomaryLabel_box = Box(440, 520, 30, 200, main_darkPurple3, False)

    #text object creation
    back_text = Text(80, 55, "<--", white, 50)
    settingsLabel_text = Text(470, 162, "Settings", white, 22)
    changePassLabel_text = Text(155, 202, "Change Password", white, 22)
    volumeLabel_text = Text(175, 362, "Music Volume", white, 22)
    measurementLabel_text = Text(155, 462, "Measurement Type", white, 22)
    oldPasswordLabel_text = Text(175, 252, "Old Password", white, 22)
    newPasswordLabel_text = Text(175, 312, "New Password", white, 22)
    save_text = Text(385, 202, "Save", white, 22)
    incorrectPassword_text = Text(660, 182, "Incorrect old password", white, 19)
    passwordRequirements1_text = Text(660, 232, "Passwords must have :", white, 19)
    passwordRequirements2_text = Text(660, 252, "- at least 8 characters", white, 18)
    passwordRequirements3_text = Text(660, 272, "- at least 1 uppercase", white, 18)
    passwordRequirements4_text = Text(660, 292, "- at least 1 lowercase", white, 18)
    passwordRequirements5_text = Text(660, 312, "- at least 1 special", white, 18)
    passwordRequirements6_text = Text(670, 332, "symbol", white, 18)
    passwordChanged_text = Text(670, 182, "Password changed.", white, 19)
    metricLabel_text = Text(165, 522, "Metric System", white, 22)
    UScustomaryLabel_text = Text(465, 522, "US Customary", white, 22)

    #button object creation
    back_button = Button(65, 50, 70, 100, main_darkPurple2, False)
    save_button = Button(370, 200, 30, 75, main_brightPurple, False)
    metric_button = Button(370, 518, 33, 33, white, False)
    UScustomary_button = Button(670, 518, 33, 33, white, False)

    while settingsLoop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                backPressed = back_button.checkPressed(pygame.mouse.get_pos()) #checks if its been pressed
                if backPressed:
                    settingsLoop = False
                    mainLoop = True
                savePressed = save_button.checkPressed(pygame.mouse.get_pos())
                if savePressed: #if save button pressed
                    errorBg1_box.setUnactive() #sets to unactive so they don't remain displayed
                    errorBg2_box.setUnactive()
                    passwordChangedBg_box.setUnactive()
                    oldPassInput = oldPassInput_input.getInput() #get input for old pass
                    newPassInput = newPassInput_input.getInput() #get input for new pass
                    passwordVerified = database.verifyPassword_main(oldPassInput, username)
                    #check that old pass matches the one in the database
                    passwordValidated = newPassInput_input.passValidate() 
                    #check that the new pass matches the password requirements
                    if passwordVerified != True: #if it isn't verified
                        errorBg1_box.setActive() #sets the first error box to active, will be displayed
                    if passwordValidated != True: #if it isn't validated
                        errorBg2_box.setActive() #error box is active
                    if passwordVerified and passwordValidated: #if both are true
                        database.changeData_main("password", newPassInput, username)
                        #change the password to that within the database
                        passwordChangedBg_box.setActive() #password changed so box is active
                        errorBg1_box.setUnactive()
                        errorBg2_box.setUnactive() #error box is not active
                metricPressed = metric_button.checkPressed(pygame.mouse.get_pos())
                if metricPressed:
                    database.changeData_main("measurement_type", True, username)
                UScustomaryPressed = UScustomary_button.checkPressed(pygame.mouse.get_pos())
                if UScustomaryPressed:
                    database.changeData_main("measurement_type", False, username)


            oldPassInput_input.handleEvent(event)
            newPassInput_input.handleEvent(event)
        
        #drawing onto screen
        WIN.blit(mainBg_image, bgPosition)
        WIN.blit(scaled_gameLogo, (450,10))
        settingsBg_box.drawBox()
        back_button.drawBox()
        back_text.drawText()
        settingsLabel_box.drawBox()
        settingsLabel_text.drawText()
        changePassLabel_box.drawBox()
        changePassLabel_text.drawText()
        volumeLabel_box.drawBox()
        volumeLabel_text.drawText()
        measurementLabel_box.drawBox()
        measurementLabel_text.drawText()
        oldPassInput_input.draw()
        newPassInput_input.draw()
        oldPasswordLabel_box.drawBox()
        oldPasswordLabel_text.drawText()
        newPasswordLabel_box.drawBox()
        newPasswordLabel_text.drawText()
        save_button.drawBox()
        save_text.drawText()
        metricLabel_box.drawBox()
        metricLabel_text.drawText()
        UScustomaryLabel_box.drawBox()
        UScustomaryLabel_text.drawText()
        metric_button.drawBox()
        UScustomary_button.drawBox()

        error1Active = errorBg1_box.getActive()
        error2Active = errorBg2_box.getActive()
        passwordChangedActive = passwordChangedBg_box.getActive() #checks if active
        if error1Active: #if active
            errorBg1_box.drawBox() #draw box and text
            incorrectPassword_text.drawText()
        if error2Active:
            errorBg2_box.drawBox()
            passwordRequirements1_text.drawText()
            passwordRequirements2_text.drawText()
            passwordRequirements3_text.drawText()
            passwordRequirements4_text.drawText()
            passwordRequirements5_text.drawText()
            passwordRequirements6_text.drawText()
        if passwordChangedActive:
            passwordChangedBg_box.drawBox()
            passwordChanged_text.drawText()

        measurement_type = database.getData_main(username, "measurement_type") #checks what value
        print(measurement_type)
        if measurement_type: #if its true
            WIN.blit(scaled_checkmarkIcon, (370, 511)) #blit chekcmark where metric system is
        else: #if false
            WIN.blit(scaled_checkmarkIcon, (670, 511)) #blit where us customary is

        pygame.display.update()
    return mainLoop, settingsLoop
    
def recipeScreen(mainLoop, recipeLoop, recipeChosen):

    #scaling images
    scaled_gameLogo = pygame.transform.scale(gameLogo_image, (125, 125))
    scaled_burger = pygame.transform.scale(burgerIcon_image, (250, 250))
    scaled_cake = pygame.transform.scale(cakeIcon_image, (170, 170))
    scaled_sushi = pygame.transform.scale(sushiIcon_image, (170, 170))
    scaled_cheeseFondue = pygame.transform.scale(cheeseFondueIcon_image, (170, 170))
    scaled_croissant = pygame.transform.scale(croissantIcon_image, (170, 170))
    scaled_tofu = pygame.transform.scale(tofuIcon_image, (170, 170))
    scaled_halal = pygame.transform.scale(halalIcon_image, (60, 60))
    scaled_vegetarian = pygame.transform.scale(vegetarianIcon_image, (60, 60))
    scaled_vegan = pygame.transform.scale(veganIcon_image, (60, 60))

    #box object creation
    recipeBg_box = Box(120, 150, 425, 750, main_lightPurple1, True)
    recipeLabel_box = Box(410, 160, 30, 200, main_darkPurple2, False)
    informationLabel_box = Box(170, 210, 30, 180, main_darkPurple2, False)
    attemptsLabel_box = Box(660, 210, 30, 180, main_darkPurple2, False)
    recipeIconBg_box = Box(390, 210, 195, 235, white, False)
    difficultyBg_box = Box(170, 330, 30, 180, main_darkPurple1, False)
    descriptionLabel_box = Box(170, 420, 30, 180, main_darkPurple2, False)
    leaderboardBg_box = Box(660, 247, 205, 180, main_darkPurple1, False)
    descriptionBg_box = Box(170, 465, 90, 670, main_darkPurple1, False)
    fullRecipeBg_box = Box(310, 100, 480, 410, main_darkPurple3, False)

    #text object creation
    back_text = Text(80, 55, "<--", white, 50)
    informationLabel_text = Text(200, 212, "Information", white, 22)
    attemptsLabel_text = Text(685, 212, "Past Attempts", white, 22)
    burgerLabel_text = Text(480, 162, "Burger", white, 22)
    cakeLabel_text = Text(485, 162, "Cake", white, 22)
    sushiLabel_text = Text(485, 162, "Sushi", white, 22)
    cheeseFondueLabel_text = Text(435, 162, "Cheese Fondue", white, 22)
    croissantLabel_text = Text(465, 162, "Croissant", white, 22)
    tofuLabel_text = Text(490, 162, "Tofu", white, 22)
    easy_text = Text(235, 332, "Easy", white, 22)
    medium_text = Text(222, 332, "Medium", white, 22)
    hard_text = Text(235, 332, "Hard", white, 22)
    fullRecipe_text = Text(205, 377, "Full Recipe", white, 22)
    description_text = Text(205, 422, "Description", white, 22)
    start_text = Text(485, 422, "Start", white, 22)
    exit_text = Text(717, 86, "X", white, 30)
    recipePageR_text = Text(695, 540, ">", white, 27)
    recipePageL_text = Text(320, 540, "<", white, 27)
    
    #description text
    burgerDescription1_text = Text(180, 467, "A burger consists of a ground meat patty enclosed in a bun. The", white, 22)
    burgerDescription2_text = Text(180, 487, "patty can be made from beef, chicken, turkey, or even plant-based", white, 22)
    burgerDescription3_text = Text(180, 507, "alternatives. The bun is typically soft, and holds the burger ingredients", white, 22)
    burgerDescription4_text = Text(180, 527, "together, which includes lettuce, cheese, tomatoes, and more.", white, 22)

    cakeDescription1_text = Text(180, 467, "Cake is a flour confection made from flour, sugar, and other ingredients", white, 22)
    cakeDescription2_text = Text(180, 487, "and is usually baked. In their oldest forms, cakes were modifications of", white, 22)
    cakeDescription3_text = Text(180, 507, "bread, but cakes now cover a wide range of preparations and share", white, 22)
    cakeDescription4_text = Text(180, 527, "features with desserts such as pastries, meringues, custards, and pies.", white, 22)

    sushiDescription1_text = Text(180, 467, "A staple rice dish of Japanese cuisine, consisting of cooked rice", white, 22)
    sushiDescription2_text = Text(180, 487, "flavored with vinegar and a variety of vegetable, egg, or raw seafood", white, 22)
    sushiDescription3_text = Text(180, 507, "garnishes and served cold. Restaurants specializing in sushi abound", white, 22)
    sushiDescription4_text = Text(180, 527, "in Japan, and the dish has gained popularity in the USA and elsewhere.", white, 22)

    cheeseFondueDescription1_text = Text(180, 467, "A Swiss national dish of melted cheese and wine served in a", white, 22)
    cheeseFondueDescription2_text = Text(180, 487, "communal pot over a portable stove and eaten by dipping bread,", white, 22)
    cheeseFondueDescription3_text = Text(180, 507, "vegetables or other foods into the cheese using long-stemmed forks.", white, 22)
    cheeseFondueDescription4_text = Text(180, 527, "This meal was supposedly to use up stale bread and cheese.", white, 22)

    croissantDescription1_text = Text(180, 467, "It is a buttery, flaky, viennoiserie pastry inspired by the shape of the", white, 22)
    croissantDescription2_text = Text(180, 487, "Austrian kipferl, but using the French yeast-leavened laminated dough.", white, 22)
    croissantDescription3_text = Text(180, 507, "Croissants are named for their historical crescent shape and are a", white, 22)
    croissantDescription4_text = Text(180, 527, "common part of a continental breakfast in many European countries.", white, 22)

    tofuDescription1_text = Text(180, 467, "Tofu, which originates from China, is a vegan cheese alternative and is", white, 22)
    tofuDescription2_text = Text(180, 487, "condensed soy milk that people press into blocks of different firmness.", white, 22)
    tofuDescription3_text = Text(180, 507, "It is a nutrient-dense food that is high in protein and contains all the", white, 22)
    tofuDescription4_text = Text(180, 527, "essential amino acids your body needs.", white, 22)
    
    #full recipe text objects
    
    burgerRecipe1_text = Text(315, 105, "1. Heat the olive oil in a frying pan, add", white, 22)
    burgerRecipe2_text = Text(337, 125, "the onion and cook for 5 minutes until", white, 22)
    burgerRecipe3_text = Text(337, 145, "softened and starting to turn golden.", white, 22)
    burgerRecipe4_text = Text(337, 165, "Set aside", white, 22)
    burgerRecipe5_text = Text(315, 205, "2. In a bowl, combine the beef mince with ", white, 22)
    burgerRecipe6_text = Text(337, 225, "the herbs and the egg. Seaston, add the", white, 22)
    burgerRecipe7_text = Text(337, 245, "onions and mix well. Shape into 4 patties", white, 22)
    burgerRecipe8_text = Text(337, 265, "(or use store bought patties instead)", white, 22)
    burgerRecipe9_text = Text(315, 305, "3. Cook the burgers on a preheated pan ", white, 22)
    burgerRecipe10_text = Text(337, 325, "for 5-6 minutes on each side, while the", white, 22)
    burgerRecipe11_text = Text(337, 345, "second side is cooking, lay a slice of", white, 22)
    burgerRecipe12_text = Text(337, 365, "cheese on top to melt slightly (if using)", white, 22)
    burgerRecipe13_text = Text(315, 405, "4. Meanwhile, lightly toast the cut sides", white, 22)
    burgerRecipe14_text = Text(337, 425, "on the pan. Fill with the lettuce, burgers", white, 22)
    burgerRecipe15_text = Text(337, 445, "and tomato slices (and other toppings)", white, 22)
    burgerRecipe16_text = Text(337, 485, "This can easily fit dietary requirements", white, 22)
    burgerRecipe17_text = Text(337, 505, "by replacing certain ingredients. Enjoy!!", white, 22)

    cakeRecipe1_text = Text(315, 105, "1. Place the cake flour, all-purpose flour,", white, 22)
    cakeRecipe2_text = Text(337, 125, "sugar, baking powder, baking soda, in the", white, 22)
    cakeRecipe3_text = Text(337, 145, "bowl of an electric mixer, and stir on low", white, 22)
    cakeRecipe4_text = Text(337, 165, "speed to combine.", white, 22)
    cakeRecipe5_text = Text(315, 205, "2. Add the butter, mixing on medium-low", white, 22)
    cakeRecipe6_text = Text(337, 225, "speed until the mixture resembles damp", white, 22)
    cakeRecipe7_text = Text(337, 245, "sand, for about one minute.", white, 22)
    cakeRecipe8_text = Text(315, 285, "3. Add the eggs, one at a time, scraping the", white, 22)
    cakeRecipe9_text = Text(337, 305, "bottom and sides of the bowl to be sure", white, 22)
    cakeRecipe10_text = Text(337, 325, "all the ingredients are fully incorporated", white, 22)
    cakeRecipe11_text = Text(315, 365, "4. Add the milk and vanilla. Mix on medium", white, 22)
    cakeRecipe12_text = Text(337, 385, "speed for 2 to 3 minutes, to aerate the", white, 22)
    cakeRecipe13_text = Text(337, 405, "batter and build the cake’s structure.", white, 22)
    cakeRecipe14_text = Text(315, 445, "5. Divide the batter equally between the", white, 22)
    cakeRecipe15_text = Text(337, 465, "prepared pans, and bake for 30 to 40", white, 22)
    cakeRecipe16_text = Text(337, 485, "minutes, or until a toothpick inserted in", white, 22)
    cakeRecipe17_text = Text(337, 505, "the thickest part of the cake comes out", white, 22)
    cakeRecipe18_text = Text(337, 525, "clean or with a few moist crumbs.", white, 22)
    cakeRecipe19_text = Text(315, 105, "6. Cool completely before frosting", white, 22)
    cakeRecipe20_text = Text(315, 145, "7. Beat butter with paddle attachment in", white, 22)
    cakeRecipe21_text = Text(337, 165, "stand mixer for 3 minutes on high until it", white, 22)
    cakeRecipe22_text = Text(337, 185, " changes from yellow to almost white,", white, 22)
    cakeRecipe23_text = Text(337, 205, "and it becomes fluffy and creamy.", white, 22)
    cakeRecipe24_text = Text(315, 245, "8. Add icing sugar / powdered sugar", white, 22)
    cakeRecipe25_text = Text(337, 265, "gradually in 3 lots, beating slowly then", white, 22)
    cakeRecipe26_text = Text(337, 285, "once mostly incorporated, beat on high", white, 22)
    cakeRecipe27_text = Text(337, 305, "for a full 3 minutes until fluffy.", white, 22)
    cakeRecipe28_text = Text(315, 345, "9. Add vanilla and milk, then beat for a", white, 22)
    cakeRecipe29_text = Text(337, 365, " further 30 seconds. Use milk only if", white, 22)
    cakeRecipe30_text = Text(337, 385, "needed to make it lovely and soft but", white, 22)
    cakeRecipe31_text = Text(337, 405, "still holds its form (e.g. for piping).", white, 22)
    cakeRecipe32_text = Text(337, 425, "Use immediately.", white, 22)

    sushiRecipe1_text = Text(315, 105, "1. Take your rice, rinse well in cold water.", white, 22)
    sushiRecipe2_text = Text(315, 145, "2. Place the rice in a pot and add water, add", white, 22)
    sushiRecipe3_text = Text(337, 165, "the lid and bring to the boil", white, 22)
    sushiRecipe4_text = Text(315, 205, "3. Once its boiling reduce to simmer for", white, 22)
    sushiRecipe5_text = Text(337, 225, "about 8-10 minutes (but keep an eye on it,", white, 22)
    sushiRecipe6_text = Text(337, 245, "you want the rice to absorb all the water", white, 22)
    sushiRecipe7_text = Text(337, 265, "but not burn or stick to the bottom on", white, 22)
    sushiRecipe8_text = Text(337, 285, "the pot)", white, 22)
    sushiRecipe9_text = Text(315, 325, "4. Cool it quickly by spreading it out on a", white, 22)
    sushiRecipe10_text = Text(337, 345, "tray, add 2 to 3 tablespoons of the sushi", white, 22)
    sushiRecipe11_text = Text(337, 365, "seasoning and mix well", white, 22)
    sushiRecipe12_text = Text(315, 405, "5. Place your nori sheet longest edge at", white, 22)
    sushiRecipe13_text = Text(337, 425, "the bottom, shiny side facing down, on", white, 22)
    sushiRecipe14_text = Text(337, 445, "the sushi mat to help you roll it.", white, 22)
    sushiRecipe15_text = Text(315, 485, "6. Leaving about an inch gap at the top.", white, 22)
    sushiRecipe16_text = Text(337, 505, "place a thin layer of rice across the sheet.", white, 22)
    sushiRecipe17_text = Text(337, 525, "(Wet hands to prevent rice from sticking)", white, 22)
    sushiRecipe18_text = Text(337, 105, "Add salmon, cucumber, avocado, that", white, 22)
    sushiRecipe19_text = Text(337, 125, "are thinly sliced and a similar length,", white, 22)
    sushiRecipe20_text = Text(337, 145, "place your filling half way up the rice", white, 22)
    sushiRecipe21_text = Text(337, 165, "and let it hang over the sides.", white, 22)
    sushiRecipe22_text = Text(315, 205, "7. Take the bottom of the sheet and roll it", white, 22)
    sushiRecipe23_text = Text(337, 225, "up so that the bottom meets the top line", white, 22)
    sushiRecipe24_text = Text(337, 245, "of the rice.", white, 22)
    sushiRecipe25_text = Text(315, 285, "8. Try to make one full roll of the rice", white, 22)
    sushiRecipe26_text = Text(337, 305, "keeping it tight, hold the roll in place.", white, 22)
    sushiRecipe27_text = Text(337, 325, "Then wet your fingers with the water and", white, 22)
    sushiRecipe28_text = Text(337, 345, "slightly dampen the remaining edge of", white, 22)
    sushiRecipe29_text = Text(337, 365, "the nori sheet then continue to roll,", white, 22)
    sushiRecipe30_text = Text(337, 385, "sealing it.", white, 22)
    sushiRecipe31_text = Text(315, 425, "9. Roll the mat around the sushi giving it a", white, 22)
    sushiRecipe32_text = Text(337, 445, "gentle yet firm squeeze (you want to", white, 22)
    sushiRecipe33_text = Text(337, 465, "compact the roll keeping it round but not", white, 22)
    sushiRecipe34_text = Text(337, 485, "squash it)", white, 22)
    sushiRecipe35_text = Text(315, 525, "10. Once you have made up all your rolls,", white, 22)
    sushiRecipe36_text = Text(337, 105, "make sure your knife is sharp and run", white, 22)
    sushiRecipe37_text = Text(337, 125, "the edge of the knife under a running tap", white, 22)
    sushiRecipe38_text = Text(337, 145, "to prevent the rice from sticking to it.", white, 22)
    sushiRecipe39_text = Text(337, 165, "Cut the roll in half then keep cutting", white, 22)
    sushiRecipe40_text = Text(337, 185, "the pieces in half again until you have", white, 22)
    sushiRecipe41_text = Text(337, 205, "8 pieces", white, 22)

    #arrays with the text objects for each recipe
    burgerRecipe = [burgerRecipe1_text, burgerRecipe2_text, burgerRecipe3_text, burgerRecipe4_text, burgerRecipe5_text, 
    burgerRecipe6_text, burgerRecipe7_text, burgerRecipe8_text, burgerRecipe9_text, burgerRecipe10_text, burgerRecipe11_text, 
    burgerRecipe12_text, burgerRecipe13_text, burgerRecipe14_text, burgerRecipe15_text, burgerRecipe16_text, burgerRecipe17_text]

    cakeRecipe = [cakeRecipe1_text, cakeRecipe2_text, cakeRecipe3_text, cakeRecipe4_text, cakeRecipe5_text, cakeRecipe6_text, cakeRecipe7_text, 
    cakeRecipe8_text, cakeRecipe9_text, cakeRecipe10_text, cakeRecipe11_text, cakeRecipe12_text, cakeRecipe13_text, cakeRecipe14_text, cakeRecipe15_text, 
    cakeRecipe16_text, cakeRecipe17_text, cakeRecipe18_text, cakeRecipe19_text, cakeRecipe20_text, cakeRecipe21_text, cakeRecipe22_text, cakeRecipe23_text, 
    cakeRecipe24_text, cakeRecipe25_text, cakeRecipe26_text, cakeRecipe27_text, cakeRecipe28_text, cakeRecipe29_text, cakeRecipe30_text, cakeRecipe31_text, 
    cakeRecipe32_text]

    sushiRecipe = [sushiRecipe1_text, sushiRecipe2_text, sushiRecipe3_text, sushiRecipe4_text, sushiRecipe5_text, sushiRecipe6_text, sushiRecipe7_text, 
    sushiRecipe8_text, sushiRecipe9_text, sushiRecipe10_text, sushiRecipe11_text, sushiRecipe12_text, sushiRecipe13_text, sushiRecipe14_text, 
    sushiRecipe15_text, sushiRecipe16_text, sushiRecipe17_text, sushiRecipe18_text, sushiRecipe19_text, sushiRecipe20_text, sushiRecipe21_text, 
    sushiRecipe22_text, sushiRecipe23_text, sushiRecipe24_text, sushiRecipe25_text, sushiRecipe26_text, sushiRecipe27_text, sushiRecipe28_text, 
    sushiRecipe29_text, sushiRecipe30_text, sushiRecipe31_text, sushiRecipe32_text, sushiRecipe33_text, sushiRecipe34_text, sushiRecipe35_text, 
    sushiRecipe36_text, sushiRecipe37_text, sushiRecipe38_text, sushiRecipe39_text, sushiRecipe40_text, sushiRecipe41_text]

    naRecipe_text = Text(450, 285, "N/A", white, 70)

    #button object creation
    back_button = Button(65, 50, 70, 100, main_darkPurple2, False)
    fullRecipe_button = Button(170, 375, 30, 180, main_darkPurple3, False)
    start_button = Button(415, 420, 30, 180, main_brightPurple, False)
    exit_button = Button(705, 85, 40, 40, login_red1, False)
    recipePageR_button = Button(685, 535, 30, 30, main_darkPurple3, False)
    recipePageL_button = Button(310, 535, 30, 30, main_darkPurple3, False)

    #variables used
    count = 0

    while recipeLoop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                backPressed = back_button.checkPressed(pygame.mouse.get_pos()) #checks if its been pressed
                if backPressed:
                    recipeLoop = False
                    mainLoop = True
                fullRecipePressed = fullRecipe_button.checkPressed(pygame.mouse.get_pos())
                if fullRecipePressed: #if full recipe button is pressed
                    fullRecipe_button.setActive() #set it to active so it displays
                    count = 0 #tracks which page you're on
                exitPressed = exit_button.checkPressed(pygame.mouse.get_pos())
                if exitPressed: #if exit button is pressed
                    fullRecipe_button.setUnactive() #removes full recipe box
                recipePageRPressed = recipePageR_button.checkPressed(pygame.mouse.get_pos())
                if recipePageRPressed: #if the right arrow is pressed
                    count = count + 1 #increment count by 1
                recipePageLPressed = recipePageL_button.checkPressed(pygame.mouse.get_pos())
                if recipePageLPressed: #if left arrow is pressed
                    count = count - 1 #decrease count by 1
        
        #drawing onto screen
        WIN.blit(mainBg_image, bgPosition)
        WIN.blit(scaled_gameLogo, (450,10))
        recipeBg_box.drawBox()
        back_button.drawBox()
        back_text.drawText()
        recipeLabel_box.drawBox()
        informationLabel_box.drawBox()
        informationLabel_text.drawText()
        attemptsLabel_box.drawBox()
        attemptsLabel_text.drawText()
        recipeIconBg_box.drawBox()
        difficultyBg_box.drawBox()
        fullRecipe_button.drawBox()
        fullRecipe_text.drawText()
        descriptionLabel_box.drawBox()
        description_text.drawText()
        start_button.drawBox()
        start_text.drawText()
        leaderboardBg_box.drawBox()
        descriptionBg_box.drawBox()

        #displaying depending on the recipe that was chosen
        if recipeChosen == "burger":
            burgerLabel_text.drawText()
            WIN.blit(scaled_burger, (380, 180))
            WIN.blit(scaled_halal, (150, 247))
            WIN.blit(scaled_vegetarian, (230, 247))
            WIN.blit(scaled_vegan, (310, 247))
            easy_text.drawText()
            burgerDescription1_text.drawText()
            burgerDescription2_text.drawText()
            burgerDescription3_text.drawText()
            burgerDescription4_text.drawText()
        elif recipeChosen == "cake":
            cakeLabel_text.drawText()
            WIN.blit(scaled_cake, (420, 210))
            WIN.blit(scaled_halal, (190, 247))
            WIN.blit(scaled_vegetarian, (265, 247))
            medium_text.drawText()
            cakeDescription1_text.drawText()
            cakeDescription2_text.drawText()
            cakeDescription3_text.drawText()
            cakeDescription4_text.drawText()
        elif recipeChosen == "sushi":
            sushiLabel_text.drawText()
            WIN.blit(scaled_sushi, (420, 210))
            WIN.blit(scaled_halal, (230, 247))
            hard_text.drawText()
            sushiDescription1_text.drawText()
            sushiDescription2_text.drawText()
            sushiDescription3_text.drawText()
            sushiDescription4_text.drawText()
        elif recipeChosen == "cheese fondue":
            cheeseFondueLabel_text.drawText()
            WIN.blit(scaled_cheeseFondue, (420, 220))
            WIN.blit(scaled_vegetarian, (230, 247))
            medium_text.drawText()
            cheeseFondueDescription1_text.drawText()
            cheeseFondueDescription2_text.drawText()
            cheeseFondueDescription3_text.drawText()
            cheeseFondueDescription4_text.drawText()
        elif recipeChosen == "croissant":
            croissantLabel_text.drawText()
            WIN.blit(scaled_croissant, (420, 220))
            WIN.blit(scaled_halal, (190, 247))
            WIN.blit(scaled_vegetarian, (265, 247))
            easy_text.drawText()
            croissantDescription1_text.drawText()
            croissantDescription2_text.drawText()
            croissantDescription3_text.drawText()
            croissantDescription4_text.drawText()
        elif recipeChosen == "tofu":
            tofuLabel_text.drawText()
            WIN.blit(scaled_tofu, (420, 220))
            WIN.blit(scaled_halal, (150, 247))
            WIN.blit(scaled_vegetarian, (230, 247))
            WIN.blit(scaled_vegan, (310, 247))
            medium_text.drawText()
            tofuDescription1_text.drawText()
            tofuDescription2_text.drawText()
            tofuDescription3_text.drawText()
            tofuDescription4_text.drawText()

        fullRecipeActive = fullRecipe_button.getActive()
        #if the full recipe button has been pressed

        if fullRecipeActive:
            fullRecipeBg_box.drawBox() #draw the boxes
            exit_button.drawBox()
            exit_text.drawText()
            if count == 0: #it will begin on the first page so
                recipePageR_button.drawBox() #it will only have the right arrow button
                recipePageR_text.drawText()
            if recipeChosen == "burger": #if the user is on the burger recipe page
                if count == 1: #if the user clicks the right arrow
                    recipePageL_button.drawBox() #display all the text and the buttons
                    recipePageL_text.drawText()
                    for i in range (len(burgerRecipe)):
                        burgerRecipe[i].drawText()
                
            elif recipeChosen == "cake": #if on cake recipe page
                if count == 1: #if the user clicks the right arrow for the first time
                    recipePageL_button.drawBox() #display buttons and text
                    recipePageL_text.drawText()
                    recipePageR_button.drawBox()
                    recipePageR_text.drawText() 
                    for i in range (18):
                        cakeRecipe[i].drawText()
                          
                elif count == 2: #if the right arrow is clicked again
                    recipePageL_button.drawBox() #display buttons and text
                    recipePageL_text.drawText()
                    for i in range(len(cakeRecipe)-18):
                        cakeRecipe[i+18].drawText()
                    
                
            elif recipeChosen == "sushi": #if on sushi recipe page
                if count == 1: #if they clicked right arrow for the first time
                    recipePageL_button.drawBox() #display
                    recipePageL_text.drawText()
                    recipePageR_button.drawBox()
                    recipePageR_text.drawText()
                    for i in range(17):
                        sushiRecipe[i].drawText()

                elif count == 2: #if right arrow clicked for 2nd time
                    recipePageL_button.drawBox() #display
                    recipePageL_text.drawText()
                    recipePageR_button.drawBox()
                    recipePageR_text.drawText()
                    for i in range(18):
                        sushiRecipe[i+18].drawText()
                        print(i+18)
                    
                elif count == 3: #if right arrow clicked for 3rd time
                    recipePageL_button.drawBox() #display
                    recipePageL_text.drawText()
                    for i in range(len(sushiRecipe)-35):
                        sushiRecipe[i+35].drawText()

            elif recipeChosen == "cheese fondue":
                naRecipe_text.drawText()
            elif recipeChosen == "croissant":
                naRecipe_text.drawText()
            elif recipeChosen == "tofu":
                naRecipe_text.drawText()


        pygame.display.update()
    return mainLoop, recipeLoop, recipeChosen

def main(loginLoop, createLoop, mainLoop, settingsLoop, shopLoop, recipeLoop):
    clock = pygame.time.Clock()
    clock.tick(FPS)
    run = True
    #loops

    #input boxes
    usernameInput1_input = Input(480, 330, 37, 280, black, 20, False)
    passwordInput1_input = Input(480, 400, 37, 280, black, 20, True)
    usernameInput2_input = Input(480, 230, 37, 280, black, 20, False)
    passwordInput2_input = Input(480, 290, 37, 280, black, 20, True)
    search_input = Input(240, 100, 37, 570, black, 20, False)
    recipeChosen = "None"
    oldPassInput_input = Input(350, 250, 30, 280, black, 20, True)
    newPassInput_input = Input(350, 310, 30, 280, black, 20, True)

    while run:
        if loginLoop == True:
            loginLoop, createLoop, mainLoop, username = loginScreen(usernameInput1_input, passwordInput1_input, loginLoop, createLoop, mainLoop)

        if createLoop == True:
            createLoop, loginLoop = createScreen(usernameInput2_input, passwordInput2_input, createLoop, loginLoop)

        if mainLoop == True:
            mainLoop, shopLoop, settingsLoop, recipeLoop, recipeChosen = mainScreen(search_input, mainLoop, shopLoop, settingsLoop, recipeLoop, recipeChosen, username) 
        
        if shopLoop == True:
            mainLoop, shopLoop = shopScreen(mainLoop, shopLoop)

        if settingsLoop == True:
            mainLoop, settingsLoop = settingsScreen(mainLoop, settingsLoop, oldPassInput_input, newPassInput_input, username)

        if recipeLoop == True:
            mainLoop, recipeLoop, recipeChosen = recipeScreen(mainLoop, recipeLoop, recipeChosen)

loginLoop = True
createLoop = False
mainLoop = False
settingsLoop = False
shopLoop = False
recipeLoop = False
minigameLoop = False

main(loginLoop, createLoop, mainLoop, settingsLoop, shopLoop, recipeLoop)
        
