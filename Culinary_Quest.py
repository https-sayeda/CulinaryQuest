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

def loginScreen(usernameInput1_input, passwordInput1_input, loginLoop, createLoop, mainLoop):

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

def mainScreen(search_input, mainLoop, shopLoop, settingsLoop, burgerLoop, cakeLoop, sushiLoop, username):

    #retrieving from database
    current_level = str(database.getLevel_main(username))
    current_points = str(100-(database.getPoints_main(username)))

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

    #this will hold the dietary requirements that have been selected via the filter tool, the values 
    #will change depending on what the user will select
    dietaryOption = [0, 0, 0]
    difficultyOption = "None"
    activeRecipes = [] #will hold the number of recipes that are active
    recipeBoxes = [recipeBg1_box, recipeBg2_box, recipeBg3_box] #stores all the recipe background boxes


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
                    burgerLoop = True
                cakePressed = cake_button.checkPressed(pygame.mouse.get_pos())
                if cakePressed:
                    mainLoop = False
                    cakeLoop = True
                sushiPressed = sushi_button.checkPressed(pygame.mouse.get_pos())
                if sushiPressed:
                    mainLoop = False
                    sushiLoop = True
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
                        else: #if no recipes have been found
                            errorBg_box.setActive() #error button is set to active so it can be displayed

                searchPressed = search_button.checkPressed(pygame.mouse.get_pos())
                if searchPressed: #if search button is pressed
                    burger_button.setUnactive()
                    cake_button.setUnactive()
                    sushi_button.setUnactive()
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
        elif len(activeRecipes) == 3: #if they've all been activated
            for x in range(len(recipeBoxes)):
                recipeBoxes[x].drawBox() #draws all the boxes
            for i in range(len(activeRecipes)): #draws all the recipe buttons
                activeRecipes[i].draw()
        elif len(activeRecipes) != 0 and len(activeRecipes) != 3 and errorActive == False: 
            #if they aren't all unactive / active
            for x in range(len(activeRecipes)): #draw the boxes based on the number of active recipes
                recipeBoxes[x].drawBox()
            for i in range(len(activeRecipes)): 
                if len(activeRecipes) == 1: #if there is only one active
                    if activeRecipes[i] == burger_button: #if the first one is burger
                        burger_button.draw() #draw burger 
                        #(the burger image doesn't work with the position below)
                    else:
                        activeRecipes[i].changePosition(145,180) #if it isn't burger, draw
                if len(activeRecipes) == 2: #if there are 2 active recipes
                    if activeRecipes[i] == burger_button and i == 0: #if it recipe is burger and it's 1st
                        burger_button.draw() #draw it
                    elif i == 0: #if it isnt burger but still the first recipe
                        activeRecipes[i].changePosition(145,180) #draw to that position
                    elif i == 1: #if second recipe..
                        activeRecipes[i].changePosition(355, 190) #draw
        elif errorActive: #if only the error box is active
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

    return mainLoop, shopLoop, settingsLoop, burgerLoop, cakeLoop, sushiLoop

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

def settingsScreen(mainLoop, settingsLoop):
    scaled_gameLogo = pygame.transform.scale(gameLogo_image, (125, 125))

    #box object creation
    settingsBg_box = Box(120, 150, 425, 750, main_lightPurple1, True)
    settingsLabel_box = Box(405, 160, 30, 200, main_darkPurple2, False)

    #text object creation
    back_text = Text(80, 55, "<--", white, 50)
    settingsLabel_text = Text(470, 162, "Settings", white, 22)

    #button object creation
    back_button = Button(65, 50, 70, 100, main_darkPurple2, False)

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
        
        #drawing onto screen
        WIN.blit(mainBg_image, bgPosition)
        WIN.blit(scaled_gameLogo, (450,10))
        settingsBg_box.drawBox()
        back_button.drawBox()
        back_text.drawText()
        settingsLabel_box.drawBox()
        settingsLabel_text.drawText()

        pygame.display.update()
    return mainLoop, settingsLoop
    
def burgerScreen(mainLoop, burgerLoop):
    scaled_gameLogo = pygame.transform.scale(gameLogo_image, (125, 125))

    #box object creation
    burgerBg_box = Box(120, 150, 425, 750, main_lightPurple1, True)
    burgerLabel_box = Box(410, 160, 30, 200, main_darkPurple2, False)

    #text object creation
    back_text = Text(80, 55, "<--", white, 50)
    burgerLabel_text = Text(480, 162, "Burger", white, 22)

    #button object creation
    back_button = Button(65, 50, 70, 100, main_darkPurple2, False)

    while burgerLoop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                backPressed = back_button.checkPressed(pygame.mouse.get_pos()) #checks if its been pressed
                if backPressed:
                    burgerLoop = False
                    mainLoop = True
        
        #drawing onto screen
        WIN.blit(mainBg_image, bgPosition)
        WIN.blit(scaled_gameLogo, (450,10))
        burgerBg_box.drawBox()
        back_button.drawBox()
        back_text.drawText()
        burgerLabel_box.drawBox()
        burgerLabel_text.drawText()

        back_activate = back_button.getActive()
        pygame.display.update()
        return mainLoop, burgerLoop

def cakeScreen(mainLoop, cakeLoop):
    scaled_gameLogo = pygame.transform.scale(gameLogo_image, (125, 125))

    #box object creation
    cakeBg_box = Box(120, 150, 425, 750, main_lightPurple1, True)
    cakeLabel_box = Box(410, 160, 30, 200, main_darkPurple2, False)

    #text object creation
    back_text = Text(80, 55, "<--", white, 50)
    cakeLabel_text = Text(485, 162, "Cake", white, 22)

    #button object creation
    back_button = Button(65, 50, 70, 100, main_darkPurple2, False)
    
    while cakeLoop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                backPressed = back_button.checkPressed(pygame.mouse.get_pos()) #checks if its been pressed
                if backPressed:
                    cakeLoop = False
                    mainLoop = True
        
        #drawing onto screen
        WIN.blit(mainBg_image, bgPosition)
        WIN.blit(scaled_gameLogo, (450,10))
        cakeBg_box.drawBox()
        back_button.drawBox()
        back_text.drawText()
        cakeLabel_box.drawBox()
        cakeLabel_text.drawText()

        pygame.display.update()
    return mainLoop, cakeLoop

def sushiScreen(mainLoop, sushiLoop):
    scaled_gameLogo = pygame.transform.scale(gameLogo_image, (125, 125))

    #box object creation
    sushiBg_box = Box(120, 150, 425, 750, main_lightPurple1, True)
    sushiLabel_box = Box(410, 160, 30, 200, main_darkPurple2, False)

    #text object creation
    back_text = Text(80, 55, "<--", white, 50)
    sushiLabel_text = Text(480, 162, "Sushi", white, 22)

    #button object creation
    back_button = Button(65, 50, 70, 100, main_darkPurple2, False)

    while sushiLoop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                backPressed = back_button.checkPressed(pygame.mouse.get_pos()) #checks if its been pressed
                if backPressed:
                    sushiLoop = False
                    mainLoop = True
        
        #drawing onto screen
        WIN.blit(mainBg_image, bgPosition)
        WIN.blit(scaled_gameLogo, (450,10))
        sushiBg_box.drawBox()
        back_button.drawBox()
        back_text.drawText()
        sushiLabel_box.drawBox()
        sushiLabel_text.drawText()

        pygame.display.update()
    return mainLoop, sushiLoop

def main(loginLoop, createLoop, mainLoop, settingsLoop, shopLoop, burgerLoop, cakeLoop, sushiLoop):
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
    
    while run:
        if loginLoop == True:
            loginLoop, createLoop, mainLoop, username = loginScreen(usernameInput1_input, passwordInput1_input, loginLoop, createLoop, mainLoop)

        if createLoop == True:
            createLoop, loginLoop = createScreen(usernameInput2_input, passwordInput2_input, createLoop, loginLoop)

        if mainLoop == True:
            mainLoop, shopLoop, settingsLoop, burgerLoop, cakeLoop, sushiLoop = mainScreen(search_input, mainLoop, shopLoop, settingsLoop, burgerLoop, cakeLoop, sushiLoop, username) 
        
        if shopLoop == True:
            mainLoop, shopLoop = shopScreen(mainLoop, shopLoop)

        if settingsLoop == True:
            mainLoop, settingsLoop = settingsScreen(mainLoop, settingsLoop)

        if burgerLoop == True:
            mainLoop, burgerLoop = burgerScreen(mainLoop, burgerLoop)

        if cakeLoop == True:
            mainLoop, cakeLoop = cakeScreen(mainLoop, cakeLoop)

        if sushiLoop == True:
            mainLoop, sushiLoop = sushiScreen(mainLoop, sushiLoop)

loginLoop = True
createLoop = False
mainLoop = False
settingsLoop = False
shopLoop = False
recipeLoop = False
burgerLoop = False
cakeLoop = False
sushiLoop = False

main(loginLoop, createLoop, mainLoop, settingsLoop, shopLoop, burgerLoop, cakeLoop, sushiLoop)
        
