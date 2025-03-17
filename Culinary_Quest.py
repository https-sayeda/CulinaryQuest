import os
import pygame
import time
import database
import sys
import minigames
from collections import deque
import classes
import globalvariables

pygame.init()

pygame.display.set_caption('Culinary Quest')

#Commonly Used Variables
bgPosition = (0,0)


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

main_lightOrange1 = pygame.Color(231, 189, 161)
main_lightOrange2 = pygame.Color(195, 129, 93)
main_darkOrange1 = pygame.Color(201, 129, 75)
main_darkOrange2 = pygame.Color(189, 88, 69)
main_darkOrange3 = pygame.Color(139, 50, 19)
main_brightOrange = pygame.Color(223, 97, 41)

main_beige = pygame.Color(232, 220, 211)
main_green = pygame.Color(68, 166, 84)
main_orange = pygame.Color(233, 113, 50)

#IMAGES
loginBg_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','login1_background.png'))
main1Bg_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','main1_background.png'))
main2Bg_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','main2_background.png'))
main2Bg_image = pygame.transform.scale(main2Bg_image, (1000, 600))
game1Bg_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','game1_background.png'))
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

#ingredients
rawPatty_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','burgerpatty.png'))
mixingBowl_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','mixingbowl.png'))
mixingBowlSpilled_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','mixingbowl_spilled.png'))

#music
pygame.mixer.init()

#SCREENS 

def loginScreen(usernameInput1_input, passwordInput1_input, loginLoop, createLoop, mainLoop):

    userInput = "None"
    #creating objects to display
    #boxes
    loginBg_box = classes.Box(280, 260, 200, 500, login_darkPurple1, True)
    doneBg1_box = classes.Box(150, 490, 80, 330, login_darkPurple1, True)
    createBg1_box = classes.Box(545, 490, 80, 330, login_darkPurple1, True)
    loginLabel_box = classes.Box(370, 270, 37, 300, login_lightPurple1, False)
    usernameLabel_box = classes.Box(300, 330, 37, 150, login_lightPurple1, False)
    passwordLabel_box = classes.Box(300, 400, 37, 150, login_lightPurple1, False)
    accountError_box = classes.Box(300, 371, 25, 460, login_red1, False)
    #buttons
    done1_button = classes.Button(165, 500, 60, 300, login_lightPurple1, False)
    create_button = classes.Button(560, 500, 60, 300, login_lightPurple1, False)
    #text
    loginLabel_text = classes.Text(495, 275, "Login", white, 22)
    done1_text = classes.Text(285, 510, "Done", white, 27)
    create_text = classes.Text(615, 510, "Create Account", white, 27)
    usernameLabel_text = classes.Text(327, 335, "Username", white, 22)
    passwordLabel_text = classes.Text(327, 405, "Password", white, 22)
    accountError_text = classes.Text(323, 371, "Please enter the correct username / password", white, 21)

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
        globalvariables.WIN.blit(loginBg_image, bgPosition)
        globalvariables.WIN.blit(gameLogo_image, (410,20))

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
    createBg_box = classes.Box(280, 150, 200, 500, login_darkPurple1, True)
    doneBg2_box = classes.Box(405, 360, 60, 230, login_darkPurple1, True)
    createLabel_box = classes.Box(370, 160, 37, 300, login_lightPurple1, False)
    usernameLabel2_box = classes.Box(300, 230, 37, 150, login_lightPurple1, False)
    passwordLabel2_box = classes.Box(300, 290, 37, 150, login_lightPurple1, False)
    userError_box = classes.Box(340, 430, 37, 350, login_red1, False)
    passError_box = classes.Box(340, 475, 115, 350, login_red1, False)
    #buttons
    done2_button = classes.Button(420, 370, 40, 200, login_lightPurple1, False)
    back_button = classes.Button(40, 70, 70, 100, login_darkPurple1, True)
    #text
    createLabel_text = classes.Text(450, 165, "Create Account", white, 22)
    usernameLabel2_text = classes.Text(327, 235, "Username", white, 22)
    passwordLabel2_text = classes.Text(327, 295, "Password", white, 22)
    done2_text = classes.Text(500, 375, "Done", white, 22)
    back_text = classes.Text(50, 75, "<--", white, 50)
    userError_text = classes.Text(365, 435, "Please enter a unique username", white, 22)
    passError1_text = classes.Text(355, 475, "Passwords must include at least:", white, 22)
    passError2_text = classes.Text(355, 500, "- 8 characters", white, 22)
    passError3_text = classes.Text(355, 520, "- 1 lowercase character", white, 22)
    passError4_text = classes.Text(355, 540, "- 1 uppercase character", white, 22)
    passError5_text = classes.Text(355, 560, "- 1 special symbol", white, 22)

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
        globalvariables.WIN.blit(loginBg_image, bgPosition)
        globalvariables.WIN.blit(scaled_gameLogo, (470,10))
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

def mainScreen(search_input, mainLoop, shopLoop, settingsLoop, recipeLoop, recipeChosen, username, theme_selected):

    #retrieving from database
    current_level = str(database.getData_main(username, "current_level"))
    current_points = str(100-(database.getData_main(username, "current_points")))

    if theme_selected == "theme1":
        colours = [main_lightPurple1, main_lightPurple2, main_darkPurple1, main_darkPurple2, main_darkPurple3, main_brightPurple]
        mainBg_image = main1Bg_image
    elif theme_selected == "theme2":
        colours = [main_lightOrange1, main_lightOrange2, main_darkOrange1, main_darkOrange2, main_darkOrange3, main_brightOrange]
        mainBg_image = main2Bg_image

    #scaling the game logo
    scaled_gameLogo = pygame.transform.scale(gameLogo_image, (75, 75))
    scaled_checkmarkIcon = pygame.transform.scale(checkmarkIcon_image, (30, 30))
    #box object creation
    recipeBg_box = classes.Box(120, 170, 425, 750, colours[0], True)
    overhead_box = classes.Box(0, 0, 75, 1000, colours[2], True)
    pointsNeeded_box = classes.Box(240, 15, 40, 300, colours[4], False)
    currentLevel_box = classes.Box(160, 15, 40, 90, colours[3], False)
    recipeBg1_box = classes.Box(130, 180, 180, 200, colours[1], False)
    recipeBg2_box = classes.Box(340, 180, 180, 200, colours[1], False)
    recipeBg3_box = classes.Box(550, 180, 180, 200, colours[1], False)
    recipeBg4_box = classes.Box(130, 380, 180, 200, colours[1], False)
    recipeBg5_box = classes.Box(340, 380, 180, 200, colours[1], False)
    recipeBg6_box = classes.Box(550, 380, 180, 200, colours[1], False)
    filterBg_box = classes.Box(820, 100, 37, 50, login_grey1, False)
    filtertoolBg_box = classes.Box(670, 150, 380, 300, login_grey1, False)
    dietaryBg_box = classes.Box(690, 160, 33, 265, colours[3], False)
    halalBg_box = classes.Box(690, 200, 33, 130, colours[0], False)
    vegeterianBg_box = classes.Box(690, 238, 33, 130, colours[0], False)
    veganBg_box = classes.Box(690, 276, 33, 130, colours[0], False)
    difficultyBg_box = classes.Box(690, 316, 33, 265, colours[3], False)
    easyBg_box = classes.Box(690, 356, 33, 130, colours[0], False)
    mediumBg_box = classes.Box(690, 394, 33, 130, colours[0], False)
    hardBg_box = classes.Box(690, 432, 33, 130, colours[0], False)
    errorBg_box = classes.Box(350, 230, 50, 300, login_red1, False)

    #text object creation
    searchLabel_text = classes.Text(150, 105, "Search", white, 22)
    error_text = classes.Text(405, 240, "Recipe not found", white, 25)
    dietary_text = classes.Text(720, 165, "Dietary Requirements", white, 22)
    halal_text = classes.Text(727, 205, "Halal", white, 22)
    vegetarian_text = classes.Text(703, 243, "Vegetarian", white, 22)
    vegan_text = classes.Text(725, 281, "Vegan", white, 22)
    difficulty_text = classes.Text(775, 321, "Difficulty", white, 22)
    easy_text = classes.Text(732, 361, "Easy", white, 22)
    medium_text = classes.Text(715, 399, "Medium", white, 22)
    hard_text = classes.Text(732, 437, "Hard", white, 22)
    filterText_text = classes.Text(800, 477, "Filter", white, 22)
    level_text = classes.Text(170, 20, "Level " + current_level, white, 22)
    pointsNeeded_text = classes.Text(263, 20, current_points + " points for the next level", white, 22)

    #button creation
    search_button = classes.Button(120, 100, 37, 120, colours[1], False)
    halal_button = classes.Button(840, 200, 33, 33, white, False)
    vegetarian_button = classes.Button(840, 238, 33, 33, white, False)
    vegan_button = classes.Button(840, 276, 33, 33, white, False)
    easy_button = classes.Button(840, 356, 33, 33, white, False)
    medium_button = classes.Button(840, 394, 33, 33, white, False)
    hard_button = classes.Button(840, 432, 33, 33, white, False)
    filterText_button = classes.Button(690, 472, 33, 265, colours[5], False)

    #image button creation
    shop_button = classes.ImageButton(600, 10, shopIcon_image, 1)
    settings_button = classes.ImageButton(850, 15, settingsIcon_image, 1)
    burger_button = classes.ImageButton(110, 155, burgerIcon_image, 0.45)
    cake_button = classes.ImageButton(355, 190, cakeIcon_image, 0.3)
    sushi_button = classes.ImageButton(570, 180, sushiIcon_image, 0.3)
    filter_button = classes.ImageButton(830, 102, filterIcon_image, 0.7)
    cheeseFondue_button = classes.ImageButton(145, 390, cheeseFondueIcon_image, 0.3)
    croissant_button = classes.ImageButton(355, 390, croissantIcon_image, 0.3)
    tofu_button = classes.ImageButton(570, 390, tofuIcon_image, 0.3)


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
        globalvariables.WIN.blit(mainBg_image, bgPosition)
        recipeBg_box.drawBox()
        overhead_box.drawBox()
        pointsNeeded_box.drawBox()
        currentLevel_box.drawBox()
        globalvariables.WIN.blit(scaled_gameLogo, (30,0))
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
            globalvariables.WIN.blit(scaled_checkmarkIcon, (845,198)) #the checkmark is displayed
        if vegetarianActive:
            globalvariables.WIN.blit(scaled_checkmarkIcon, (845,236))
        if veganActive:
            globalvariables.WIN.blit(scaled_checkmarkIcon, (845,275))
        if easyActive: #if the button is active
            globalvariables.WIN.blit(scaled_checkmarkIcon, (845,354)) #the checkmark is displayed
        if mediumActive:
            globalvariables.WIN.blit(scaled_checkmarkIcon, (845,392))
        if hardActive:
            globalvariables.WIN.blit(scaled_checkmarkIcon, (845,430))

        pygame.display.update()

    return mainLoop, shopLoop, settingsLoop, recipeLoop, recipeChosen

def shopScreen(mainLoop, shopLoop, username, theme_selected):

    #retrieving from database
    current_level = int(database.getData_main(username, "current_level"))

    if theme_selected == "theme1":
        colours = [main_lightPurple1, main_lightPurple2, main_darkPurple1, main_darkPurple2, main_darkPurple3, main_brightPurple]
        mainBg_image = main1Bg_image
    elif theme_selected == "theme2":
        colours = [main_lightOrange1, main_lightOrange2, main_darkOrange1, main_darkOrange2, main_darkOrange3, main_brightOrange]
        mainBg_image = main2Bg_image

    scaled_gameLogo = pygame.transform.scale(gameLogo_image, (125, 125))

    #box object creation
    shopBg_box = classes.Box(120, 150, 425, 750, colours[0], True)
    shopLabel_box = classes.Box(410, 160, 30, 200, colours[3], False)
    musicLabel_box = classes.Box(140, 200, 30, 90, colours[3], False)
    disc1Label_box = classes.Box(140, 250, 60, 180, colours[2], False)
    disc2Label_box = classes.Box(390, 250, 60, 180, colours[2], False)
    disc3Label_box = classes.Box(640, 250, 60, 180, colours[2], False)
    themeLabel_box = classes.Box(140, 380, 30, 90, colours[3], False)
    theme1Label_box = classes.Box(140, 430, 60, 180, main_darkPurple1, False)
    theme2Label_box = classes.Box(390, 430, 60, 180, main_orange, False)
    theme3Label_box = classes.Box(640, 430, 60, 180, colours[2], False)


    #text object creation
    back_text = classes.Text(80, 55, "<--", white, 50)
    shopLabel_text = classes.Text(485, 162, "Shop", white, 22)
    musicLabel_text = classes.Text(155, 202, "Music", white, 22)
    disc1Label_text = classes.Text(195, 265, "Disc 1", white, 25)
    disc2Label_text = classes.Text(445, 265, "Disc 2", white, 25)
    disc3Label_text = classes.Text(695, 265, "Disc 3", white, 25)
    themeLabel_text = classes.Text(150, 382, "Theme", white, 22)
    theme1Label_text = classes.Text(190, 445, "Purple", white, 25)
    theme2Label_text = classes.Text(440, 445, "Orange", white, 25)
    theme3Label_text = classes.Text(710, 445, "N/A", white, 25)
    discSelected_text = classes.Text(185, 332, "Selected", white, 22)
    themeSelected_text = classes.Text(185, 512, "Selected", white, 22)
    disc2Required_text = classes.Text(405, 332, "Must be level 5", white, 22)
    disc3Required_text = classes.Text(655, 332, "Must be level 10", white, 22)
    theme2Required_text = classes.Text(405, 512, "Must be level 10", white, 22)
    theme3NA_text = classes.Text(715, 512, "N/A", white, 22)
    disc2Unlock_text = classes.Text(437, 332, "Unlock", white, 22)
    disc3Unlock_text = classes.Text(687, 332, "Unlock", white, 22)
    theme2Unlock_text = classes.Text(437, 512, "Unlock", white, 22)
    disc1Select_text = classes.Text(187, 332, "Select", white, 22)
    disc2Select_text = classes.Text(437, 332, "Select", white, 22)
    disc3Select_text = classes.Text(687, 332, "Select", white, 22)
    theme1Select_text = classes.Text(187, 512, "Select", white, 22)
    theme2Select_text = classes.Text(437, 512, "Select", white, 22)

    #button object creation
    back_button = classes.Button(65, 50, 70, 100, colours[3], False)
    disc1Unlock_button = classes.Button(140, 330, 30, 180, colours[4], False)
    disc2Unlock_button = classes.Button(390, 330, 30, 180, colours[4], False)
    disc3Unlock_button = classes.Button(640, 330, 30, 180, colours[4], False)
    theme1Unlock_button = classes.Button(140, 510, 30, 180, colours[4], False)
    theme2Unlock_button = classes.Button(390, 510, 30, 180, colours[4], False)
    theme3Unlock_button = classes.Button(640, 510, 30, 180, colours[4], False)

    while shopLoop:

        disc_selected = str(database.getData_main(username, "disc_selected"))
        theme_selected = str(database.getData_main(username, "theme_selected"))
        disc1_available = bool(database.getShopData_main(username, "disc1"))
        disc2_available = bool(database.getShopData_main(username, "disc2"))
        disc3_available = bool(database.getShopData_main(username, "disc3"))
        theme1_available = bool(database.getShopData_main(username, "theme1"))
        theme2_available = bool(database.getShopData_main(username, "theme2"))

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
                disc1Pressed = disc1Unlock_button.checkPressed(pygame.mouse.get_pos())
                if disc1Pressed: #if the button for disc1 has been pressed
                    if disc_selected != "disc1": #checks that it isn't already selected
                        database.changeData_main("disc_selected", "disc1", username)
                        #changes the selected disc to disc1 in database
                disc2Pressed = disc2Unlock_button.checkPressed(pygame.mouse.get_pos())
                if disc2Pressed:
                    if disc_selected != "disc2": #checks that disc 2 not already selected
                        if disc2_available == True: #if it has already been unlocked
                            database.changeData_main("disc_selected", "disc2", username)
                            #make it become the selected disc
                        elif current_level >= 5: #if it hasn't been unlocked and the level is at least 5
                            database.changeData_main("disc2", True, username) #make it so the disc is unlocked
                disc3Pressed = disc3Unlock_button.checkPressed(pygame.mouse.get_pos())
                if disc3Pressed:
                    if disc_selected != "disc3":
                        if disc3_available == True:
                            database.changeData_main("disc_selected", "disc3", username)
                        elif current_level >= 10:
                            database.changeData_main("disc3", True, username)
                theme1Pressed = theme1Unlock_button.checkPressed(pygame.mouse.get_pos())
                if theme1Pressed: #if theme1 button pressed
                    if theme_selected != "theme1": #checks not already selected
                        database.changeData_main("theme_selected", "theme1", username)
                        #if it hasn't been selected, then changes it to be selected
                theme2Pressed = theme2Unlock_button.checkPressed(pygame.mouse.get_pos())
                if theme2Pressed:
                    if theme_selected != "theme2":
                        if theme2_available == True:
                            database.changeData_main("theme_selected", "theme2", username)
                        elif current_level >= 10:
                            database.changeData_main("theme2", True, username)
            
        #drawing onto screen
        globalvariables.WIN.blit(mainBg_image, bgPosition)
        globalvariables.WIN.blit(scaled_gameLogo, (450,10))
        shopBg_box.drawBox()
        back_button.drawBox()
        back_text.drawText()
        shopLabel_box.drawBox()
        shopLabel_text.drawText()
        musicLabel_box.drawBox()
        disc1Label_box.drawBox()
        disc2Label_box.drawBox()
        disc3Label_box.drawBox()
        disc1Unlock_button.drawBox()
        disc2Unlock_button.drawBox()
        disc3Unlock_button.drawBox()
        themeLabel_box.drawBox()
        theme1Label_box.drawBox()
        theme2Label_box.drawBox()
        theme3Label_box.drawBox()
        theme1Unlock_button.drawBox()
        theme2Unlock_button.drawBox()
        theme3Unlock_button.drawBox()
        musicLabel_text.drawText()
        disc1Label_text.drawText()
        disc2Label_text.drawText()
        disc3Label_text.drawText()
        themeLabel_text.drawText()
        theme1Label_text.drawText()
        theme2Label_text.drawText()
        theme3Label_text.drawText()
        theme3NA_text.drawText()

        if disc_selected == "disc1": #if the disc has been selected
            discSelected_text.drawText() #display that it has been selected under that box
        elif disc1_available == True: #if it hasn't been selected but has been unlocked
            disc1Select_text.drawText() #display that it can be selected under that box

        if disc_selected == "disc2":
            discSelected_text.changePosition(435, 332)
        elif disc2_available == True:
            disc2Select_text.drawText()
        elif current_level >= 5:
            disc2Unlock_text.drawText()
        else:
            disc2Required_text.drawText()

        if disc_selected == "disc3":
            discSelected_text.changePosition(685, 332)
        elif disc3_available == True:
            disc3Select_text.drawText()
        elif current_level >= 10:
            disc3Unlock_text.drawText()
        else:
            disc3Required_text.drawText()

        if theme_selected == "theme1": #if the theme has been selected
            themeSelected_text.drawText() #display that it has been selected under that box
        elif theme1_available == True:
            theme1Select_text.drawText()

        if theme_selected == "theme2":
            themeSelected_text.changePosition(435, 512)
        elif theme2_available == True:
            theme2Select_text.drawText()
        elif current_level >= 10:
            theme2Unlock_text.drawText()
        else:
            theme2Required_text.drawText()

        pygame.display.update()

    return mainLoop, shopLoop, disc_selected, theme_selected

def settingsScreen(mainLoop, settingsLoop, oldPassInput_input, newPassInput_input, username, theme_selected):

    volume_level = database.getData_main(username, "volume_level")

    if theme_selected == "theme1":
        colours = [main_lightPurple1, main_lightPurple2, main_darkPurple1, main_darkPurple2, main_darkPurple3, main_brightPurple]
        mainBg_image = main1Bg_image
    elif theme_selected == "theme2":
        colours = [main_lightOrange1, main_lightOrange2, main_darkOrange1, main_darkOrange2, main_darkOrange3, main_brightOrange]
        mainBg_image = main2Bg_image

    scaled_gameLogo = pygame.transform.scale(gameLogo_image, (125, 125))
    scaled_checkmarkIcon = pygame.transform.scale(checkmarkIcon_image, (35, 35))

    #box object creation
    settingsBg_box = classes.Box(120, 150, 425, 750, colours[0], True)
    settingsLabel_box = classes.Box(405, 160, 30, 200, colours[3], False)
    changePassLabel_box = classes.Box(140, 200, 30, 210, colours[3], False)
    volumeLabel_box = classes.Box(140, 360, 30, 210, colours[3], False)
    measurementLabel_box = classes.Box(140, 460, 30, 210, colours[3], False)
    oldPasswordLabel_box = classes.Box(140, 250, 30, 210, colours[4], False)
    newPasswordLabel_box = classes.Box(140, 310, 30, 210, colours[4], False)
    errorBg1_box = classes.Box(655, 180, 30, 200, login_red1, False)
    errorBg2_box = classes.Box(655, 230, 130, 200, login_red1, False)
    passwordChangedBg_box = classes.Box(655, 180, 30, 200, main_green, False)
    metricLabel_box = classes.Box(140, 520, 30, 200, colours[4], False)
    UScustomaryLabel_box = classes.Box(440, 520, 30, 200, colours[4], False)
    volumeBg_box = classes.Box(140, 410, 30, 500, white, False)
    volumeBar_box = classes.Box(140, 410, 30, volume_level*5, colours[2], False)

    #text object creation
    back_text = classes.Text(80, 55, "<--", white, 50)
    settingsLabel_text = classes.Text(470, 162, "Settings", white, 22)
    changePassLabel_text = classes.Text(155, 202, "Change Password", white, 22)
    volumeLabel_text = classes.Text(175, 362, "Music Volume", white, 22)
    measurementLabel_text = classes.Text(155, 462, "Measurement Type", white, 22)
    oldPasswordLabel_text = classes.Text(175, 252, "Old Password", white, 22)
    newPasswordLabel_text = classes.Text(175, 312, "New Password", white, 22)
    save_text = classes.Text(385, 202, "Save", white, 22)
    incorrectPassword_text = classes.Text(660, 182, "Incorrect old password", white, 19)
    passwordRequirements1_text = classes.Text(660, 232, "Passwords must have :", white, 19)
    passwordRequirements2_text = classes.Text(660, 252, "- at least 8 characters", white, 18)
    passwordRequirements3_text = classes.Text(660, 272, "- at least 1 uppercase", white, 18)
    passwordRequirements4_text = classes.Text(660, 292, "- at least 1 lowercase", white, 18)
    passwordRequirements5_text = classes.Text(660, 312, "- at least 1 special", white, 18)
    passwordRequirements6_text = classes.Text(670, 332, "symbol", white, 18)
    passwordChanged_text = classes.Text(670, 182, "Password changed.", white, 19)
    metricLabel_text = classes.Text(165, 522, "Metric System", white, 22)
    UScustomaryLabel_text = classes.Text(465, 522, "US Customary", white, 22)
    volumeUp_text = classes.Text(660, 395, "/\\", white, 20)
    volumeDown_text = classes.Text(660, 423, "\/", white, 20)

    #button object creation
    back_button = classes.Button(65, 50, 70, 100, colours[3], False)
    save_button = classes.Button(370, 200, 30, 75, colours[5], False)
    metric_button = classes.Button(370, 518, 33, 33, white, False)
    UScustomary_button = classes.Button(670, 518, 33, 33, white, False)
    volumeUp_button = classes.Button(650, 397, 22, 33, colours[4], False)
    volumeDown_button = classes.Button(650, 423, 22, 33, colours[4], False)

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
                volumeUpPressed = volumeUp_button.checkPressed(pygame.mouse.get_pos()) 
                #checks if volume up button pressed 
                if volumeUpPressed: #if it has been
                    if volume_level < 100: #checks that the volume is less than 100
                        volume = volumeBar_box.changeLength(5) #if it is, increase bar length by 5
                        volume_level = volume / 5 #convert to volume value so increases by 1
                    elif volume_level > 100: #if it is more than 100
                        volume_level = 100 #set volume to 100
                    database.changeData_main("volume_level", volume_level, username) 
                    #change volume in database
                volumeDownPressed = volumeDown_button.checkPressed(pygame.mouse.get_pos()) 
                #checks if volume down button pressed
                if volumeDownPressed: #if it has been
                    if volume_level > 0: #checks that the volume is above 0
                        volume = volumeBar_box.changeLength(-5) #if it is, decrease bar length by 5
                        volume_level = volume / 5 #convert to volume value so decreases by 1
                    elif volume_level < 0: #if less than 0
                        volume_level = 0 #set to 0
                    database.changeData_main("volume_level", volume_level, username) #change in database

        
            oldPassInput_input.handleEvent(event)
            newPassInput_input.handleEvent(event)
        pygame.mixer.music.set_volume(volume_level / 100) #sets the volume to that level
        
        #drawing onto screen
        globalvariables.WIN.blit(mainBg_image, bgPosition)
        globalvariables.WIN.blit(scaled_gameLogo, (450,10))
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
        volumeBg_box.drawBox()
        volumeBar_box.drawBox()
        volumeUp_button.drawBox()
        volumeDown_button.drawBox()
        volumeUp_text.drawText()
        volumeDown_text.drawText()

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
        if measurement_type: #if its true
            globalvariables.WIN.blit(scaled_checkmarkIcon, (370, 511)) #blit chekcmark where metric system is
        else: #if false
            globalvariables.WIN.blit(scaled_checkmarkIcon, (670, 511)) #blit where us customary is

        pygame.display.update()
    return mainLoop, settingsLoop
    
def recipeScreen(mainLoop, recipeLoop, minigameLoop, recipeChosen, username, theme_selected):

    measurementType = database.getData_main(username, "measurement_type")

    if theme_selected == "theme1":
        colours = [main_lightPurple1, main_lightPurple2, main_darkPurple1, main_darkPurple2, main_darkPurple3, main_brightPurple]
        mainBg_image = main1Bg_image
    elif theme_selected == "theme2":
        colours = [main_lightOrange1, main_lightOrange2, main_darkOrange1, main_darkOrange2, main_darkOrange3, main_brightOrange]
        mainBg_image = main2Bg_image
    
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
    recipeBg_box = classes.Box(120, 150, 425, 750, colours[0], True)
    recipeLabel_box = classes.Box(410, 160, 30, 200, colours[3], False)
    informationLabel_box = classes.Box(170, 210, 30, 180, colours[3], False)
    attemptsLabel_box = classes.Box(660, 210, 30, 180, colours[3], False)
    recipeIconBg_box = classes.Box(390, 210, 195, 235, white, False)
    difficultyBg_box = classes.Box(170, 330, 30, 180, colours[2], False)
    descriptionLabel_box = classes.Box(170, 420, 30, 180, colours[3], False)
    leaderboardBg_box = classes.Box(660, 247, 205, 180, colours[2], False)
    descriptionBg_box = classes.Box(170, 465, 90, 670, colours[2], False)
    fullRecipeBg_box = classes.Box(310, 100, 480, 410, colours[4], False)

    #text object creation
    back_text = classes.Text(80, 55, "<--", white, 50)
    informationLabel_text = classes.Text(200, 212, "Information", white, 22)
    attemptsLabel_text = classes.Text(685, 212, "Past Attempts", white, 22)
    burgerLabel_text = classes.Text(480, 162, "Burger", white, 22)
    cakeLabel_text = classes.Text(485, 162, "Cake", white, 22)
    sushiLabel_text = classes.Text(485, 162, "Sushi", white, 22)
    cheeseFondueLabel_text = classes.Text(435, 162, "Cheese Fondue", white, 22)
    croissantLabel_text = classes.Text(465, 162, "Croissant", white, 22)
    tofuLabel_text = classes.Text(490, 162, "Tofu", white, 22)
    easy_text = classes.Text(235, 332, "Easy", white, 22)
    medium_text = classes.Text(222, 332, "Medium", white, 22)
    hard_text = classes.Text(235, 332, "Hard", white, 22)
    fullRecipe_text = classes.Text(205, 377, "Full Recipe", white, 22)
    description_text = classes.Text(205, 422, "Description", white, 22)
    start_text = classes.Text(485, 422, "Start", white, 22)
    exit_text = classes.Text(717, 86, "X", white, 30)
    recipePageR_text = classes.Text(695, 540, ">", white, 27)
    recipePageL_text = classes.Text(320, 540, "<", white, 27)
    
    #description text
    burgerDescription1_text = classes.Text(180, 467, "A burger consists of a ground meat patty enclosed in a bun. The", white, 22)
    burgerDescription2_text = classes.Text(180, 487, "patty can be made from beef, chicken, turkey, or even plant-based", white, 22)
    burgerDescription3_text = classes.Text(180, 507, "alternatives. The bun is typically soft, and holds the burger ingredients", white, 22)
    burgerDescription4_text = classes.Text(180, 527, "together, which includes lettuce, cheese, tomatoes, and more.", white, 22)

    cakeDescription1_text = classes.Text(180, 467, "Cake is a flour confection made from flour, sugar, and other ingredients", white, 22)
    cakeDescription2_text = classes.Text(180, 487, "and is usually baked. In their oldest forms, cakes were modifications of", white, 22)
    cakeDescription3_text = classes.Text(180, 507, "bread, but cakes now cover a wide range of preparations and share", white, 22)
    cakeDescription4_text = classes.Text(180, 527, "features with desserts such as pastries, meringues, custards, and pies.", white, 22)

    sushiDescription1_text = classes.Text(180, 467, "A staple rice dish of Japanese cuisine, consisting of cooked rice", white, 22)
    sushiDescription2_text = classes.Text(180, 487, "flavored with vinegar and a variety of vegetable, egg, or raw seafood", white, 22)
    sushiDescription3_text = classes.Text(180, 507, "garnishes and served cold. Restaurants specializing in sushi abound", white, 22)
    sushiDescription4_text = classes.Text(180, 527, "in Japan, and the dish has gained popularity in the USA and elsewhere.", white, 22)

    cheeseFondueDescription1_text = classes.Text(180, 467, "A Swiss national dish of melted cheese and wine served in a", white, 22)
    cheeseFondueDescription2_text = classes.Text(180, 487, "communal pot over a portable stove and eaten by dipping bread,", white, 22)
    cheeseFondueDescription3_text = classes.Text(180, 507, "vegetables or other foods into the cheese using long-stemmed forks.", white, 22)
    cheeseFondueDescription4_text = classes.Text(180, 527, "This meal was supposedly to use up stale bread and cheese.", white, 22)

    croissantDescription1_text = classes.Text(180, 467, "It is a buttery, flaky, viennoiserie pastry inspired by the shape of the", white, 22)
    croissantDescription2_text = classes.Text(180, 487, "Austrian kipferl, but using the French yeast-leavened laminated dough.", white, 22)
    croissantDescription3_text = classes.Text(180, 507, "Croissants are named for their historical crescent shape and are a", white, 22)
    croissantDescription4_text = classes.Text(180, 527, "common part of a continental breakfast in many European countries.", white, 22)

    tofuDescription1_text = classes.Text(180, 467, "Tofu, which originates from China, is a vegan cheese alternative and is", white, 22)
    tofuDescription2_text = classes.Text(180, 487, "condensed soy milk that people press into blocks of different firmness.", white, 22)
    tofuDescription3_text = classes.Text(180, 507, "It is a nutrient-dense food that is high in protein and contains all the", white, 22)
    tofuDescription4_text = classes.Text(180, 527, "essential amino acids your body needs.", white, 22)
    
    #full recipe text objects
    
    burgerRecipe1_text = classes.Text(315, 105, "1. Heat the olive oil in a frying pan, add", white, 22)
    burgerRecipe2_text = classes.Text(337, 125, "the onion and cook for 5 minutes until", white, 22)
    burgerRecipe3_text = classes.Text(337, 145, "softened and starting to turn golden.", white, 22)
    burgerRecipe4_text = classes.Text(337, 165, "Set aside", white, 22)
    burgerRecipe5_text = classes.Text(315, 205, "2. In a bowl, combine the beef mince with ", white, 22)
    burgerRecipe6_text = classes.Text(337, 225, "the herbs and the egg. Seaston, add the", white, 22)
    burgerRecipe7_text = classes.Text(337, 245, "onions and mix well. Shape into 4 patties", white, 22)
    burgerRecipe8_text = classes.Text(337, 265, "(or use store bought patties instead)", white, 22)
    burgerRecipe9_text = classes.Text(315, 305, "3. Cook the burgers on a preheated pan ", white, 22)
    burgerRecipe10_text = classes.Text(337, 325, "for 5-6 minutes on each side, while the", white, 22)
    burgerRecipe11_text = classes.Text(337, 345, "second side is cooking, lay a slice of", white, 22)
    burgerRecipe12_text = classes.Text(337, 365, "cheese on top to melt slightly (if using)", white, 22)
    burgerRecipe13_text = classes.Text(315, 405, "4. Meanwhile, lightly toast the cut sides", white, 22)
    burgerRecipe14_text = classes.Text(337, 425, "on the pan. Fill with the lettuce, burgers", white, 22)
    burgerRecipe15_text = classes.Text(337, 445, "and tomato slices (and other toppings)", white, 22)
    burgerRecipe16_text = classes.Text(337, 485, "This can easily fit dietary requirements", white, 22)
    burgerRecipe17_text = classes.Text(337, 505, "by replacing certain ingredients. Enjoy!!", white, 22)

    cakeRecipe1_text = classes.Text(315, 105, "1. Place the cake flour, all-purpose flour,", white, 22)
    cakeRecipe2_text = classes.Text(337, 125, "sugar, baking powder, baking soda, in the", white, 22)
    cakeRecipe3_text = classes.Text(337, 145, "bowl of an electric mixer, and stir on low", white, 22)
    cakeRecipe4_text = classes.Text(337, 165, "speed to combine.", white, 22)
    cakeRecipe5_text = classes.Text(315, 205, "2. Add the butter, mixing on medium-low", white, 22)
    cakeRecipe6_text = classes.Text(337, 225, "speed until the mixture resembles damp", white, 22)
    cakeRecipe7_text = classes.Text(337, 245, "sand, for about one minute.", white, 22)
    cakeRecipe8_text = classes.Text(315, 285, "3. Add the eggs, one at a time, scraping the", white, 22)
    cakeRecipe9_text = classes.Text(337, 305, "bottom and sides of the bowl to be sure", white, 22)
    cakeRecipe10_text = classes.Text(337, 325, "all the ingredients are fully incorporated", white, 22)
    cakeRecipe11_text = classes.Text(315, 365, "4. Add the milk and vanilla. Mix on medium", white, 22)
    cakeRecipe12_text = classes.Text(337, 385, "speed for 2 to 3 minutes, to aerate the", white, 22)
    cakeRecipe13_text = classes.Text(337, 405, "batter and build the cake’s structure.", white, 22)
    cakeRecipe14_text = classes.Text(315, 445, "5. Divide the batter equally between the", white, 22)
    cakeRecipe15_text = classes.Text(337, 465, "prepared pans, and bake for 30 to 40", white, 22)
    cakeRecipe16_text = classes.Text(337, 485, "minutes, or until a toothpick inserted in", white, 22)
    cakeRecipe17_text = classes.Text(337, 505, "the thickest part of the cake comes out", white, 22)
    cakeRecipe18_text = classes.Text(337, 525, "clean or with a few moist crumbs.", white, 22)
    cakeRecipe19_text = classes.Text(315, 105, "6. Cool completely before frosting", white, 22)
    cakeRecipe20_text = classes.Text(315, 145, "7. Beat butter with paddle attachment in", white, 22)
    cakeRecipe21_text = classes.Text(337, 165, "stand mixer for 3 minutes on high until it", white, 22)
    cakeRecipe22_text = classes.Text(337, 185, " changes from yellow to almost white,", white, 22)
    cakeRecipe23_text = classes.Text(337, 205, "and it becomes fluffy and creamy.", white, 22)
    cakeRecipe24_text = classes.Text(315, 245, "8. Add icing sugar / powdered sugar", white, 22)
    cakeRecipe25_text = classes.Text(337, 265, "gradually in 3 lots, beating slowly then", white, 22)
    cakeRecipe26_text = classes.Text(337, 285, "once mostly incorporated, beat on high", white, 22)
    cakeRecipe27_text = classes.Text(337, 305, "for a full 3 minutes until fluffy.", white, 22)
    cakeRecipe28_text = classes.Text(315, 345, "9. Add vanilla and milk, then beat for a", white, 22)
    cakeRecipe29_text = classes.Text(337, 365, " further 30 seconds. Use milk only if", white, 22)
    cakeRecipe30_text = classes.Text(337, 385, "needed to make it lovely and soft but", white, 22)
    cakeRecipe31_text = classes.Text(337, 405, "still holds its form (e.g. for piping).", white, 22)
    cakeRecipe32_text = classes.Text(337, 425, "Use immediately.", white, 22)

    sushiRecipe1_text = classes.Text(315, 105, "1. Take your rice, rinse well in cold water.", white, 22)
    sushiRecipe2_text = classes.Text(315, 145, "2. Place the rice in a pot and add water, add", white, 22)
    sushiRecipe3_text = classes.Text(337, 165, "the lid and bring to the boil", white, 22)
    sushiRecipe4_text = classes.Text(315, 205, "3. Once its boiling reduce to simmer for", white, 22)
    sushiRecipe5_text = classes.Text(337, 225, "about 8-10 minutes (but keep an eye on it,", white, 22)
    sushiRecipe6_text = classes.Text(337, 245, "you want the rice to absorb all the water", white, 22)
    sushiRecipe7_text = classes.Text(337, 265, "but not burn or stick to the bottom on", white, 22)
    sushiRecipe8_text = classes.Text(337, 285, "the pot)", white, 22)
    sushiRecipe9_text = classes.Text(315, 325, "4. Cool it quickly by spreading it out on a", white, 22)
    sushiRecipe10_text = classes.Text(337, 345, "tray, add 2 to 3 tablespoons of the sushi", white, 22)
    sushiRecipe11_text = classes.Text(337, 365, "seasoning and mix well", white, 22)
    sushiRecipe12_text = classes.Text(315, 405, "5. Place your nori sheet longest edge at", white, 22)
    sushiRecipe13_text = classes.Text(337, 425, "the bottom, shiny side facing down, on", white, 22)
    sushiRecipe14_text = classes.Text(337, 445, "the sushi mat to help you roll it.", white, 22)
    sushiRecipe15_text = classes.Text(315, 485, "6. Leaving about an inch gap at the top.", white, 22)
    sushiRecipe16_text = classes.Text(337, 505, "place a thin layer of rice across the sheet.", white, 22)
    sushiRecipe17_text = classes.Text(337, 525, "(Wet hands to prevent rice from sticking)", white, 22)
    sushiRecipe18_text = classes.Text(337, 105, "Add salmon, cucumber, avocado, that", white, 22)
    sushiRecipe19_text = classes.Text(337, 125, "are thinly sliced and a similar length,", white, 22)
    sushiRecipe20_text = classes.Text(337, 145, "place your filling half way up the rice", white, 22)
    sushiRecipe21_text = classes.Text(337, 165, "and let it hang over the sides.", white, 22)
    sushiRecipe22_text = classes.Text(315, 205, "7. Take the bottom of the sheet and roll it", white, 22)
    sushiRecipe23_text = classes.Text(337, 225, "up so that the bottom meets the top line", white, 22)
    sushiRecipe24_text = classes.Text(337, 245, "of the rice.", white, 22)
    sushiRecipe25_text = classes.Text(315, 285, "8. Try to make one full roll of the rice", white, 22)
    sushiRecipe26_text = classes.Text(337, 305, "keeping it tight, hold the roll in place.", white, 22)
    sushiRecipe27_text = classes.Text(337, 325, "Then wet your fingers with the water and", white, 22)
    sushiRecipe28_text = classes.Text(337, 345, "slightly dampen the remaining edge of", white, 22)
    sushiRecipe29_text = classes.Text(337, 365, "the nori sheet then continue to roll,", white, 22)
    sushiRecipe30_text = classes.Text(337, 385, "sealing it.", white, 22)
    sushiRecipe31_text = classes.Text(315, 425, "9. Roll the mat around the sushi giving it a", white, 22)
    sushiRecipe32_text = classes.Text(337, 445, "gentle yet firm squeeze (you want to", white, 22)
    sushiRecipe33_text = classes.Text(337, 465, "compact the roll keeping it round but not", white, 22)
    sushiRecipe34_text = classes.Text(337, 485, "squash it)", white, 22)
    sushiRecipe35_text = classes.Text(315, 525, "10. Once you have made up all your rolls,", white, 22)
    sushiRecipe36_text = classes.Text(337, 105, "make sure your knife is sharp and run", white, 22)
    sushiRecipe37_text = classes.Text(337, 125, "the edge of the knife under a running tap", white, 22)
    sushiRecipe38_text = classes.Text(337, 145, "to prevent the rice from sticking to it.", white, 22)
    sushiRecipe39_text = classes.Text(337, 165, "Cut the roll in half then keep cutting", white, 22)
    sushiRecipe40_text = classes.Text(337, 185, "the pieces in half again until you have", white, 22)
    sushiRecipe41_text = classes.Text(337, 205, "8 pieces", white, 22)

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

    naRecipe_text = classes.Text(450, 285, "N/A", white, 70)

    #ingredient text objects

    ingredientsLabel_text = classes.Text(315, 105, "Ingredients: ", white, 22)
    burgerMetricIngredients1_text = classes.Text(315, 145, "7ml olive oil", white, 22)
    burgerMetricIngredients2_text = classes.Text(315, 165, "170g onion, peeled and chopped", white, 22)
    burgerMetricIngredients3_text = classes.Text(315, 185, "500g beef steak mince (or alternatives)", white, 22)
    burgerMetricIngredients4_text = classes.Text(315, 205, "4g mixed dried herbs", white, 22)
    burgerIngredients5_text = classes.Text(315, 225, "1 egg, beaten", white, 22)
    burgerMetricIngredients6_text = classes.Text(315, 245, "75g of cheese (optional)", white, 22)
    burgerIngredients7_text = classes.Text(315, 265, "4 white rolls", white, 22)
    burgerMetricIngredients8_text = classes.Text(315, 285, "15g lettuce", white, 22)
    burgerMetricIngredients9_text = classes.Text(315, 305, "75g tomato, sliced", white, 22)

    burgerUSIngredients1_text = classes.Text(315, 145, "1/2 tbsp olive oil", white, 22)
    burgerUSIngredients2_text = classes.Text(315, 165, "1 medium onion, peeled and chopped", white, 22)
    burgerUSIngredients3_text = classes.Text(315, 185, "500g beef steak mince (or alternatives)", white, 22)
    burgerUSIngredients4_text = classes.Text(315, 205, "1 tsp mixed dried herbs", white, 22)
    burgerUSIngredients6_text = classes.Text(315, 245, "4 slices of cheese (optional)", white, 22)
    burgerUSIngredients8_text = classes.Text(315, 285, "3 lettuce leaves", white, 22)
    burgerUSIngredients9_text = classes.Text(315, 305, "1 medium tomato, sliced", white, 22)

    cakeIngredientsLabel_text = classes.Text(315, 105, "Cake Ingredients: ", white, 22)
    cakeMetricIngredients1_text = classes.Text(315, 145, "187.5g cake flour", white, 22)
    cakeMetricIngredients2_text = classes.Text(315, 165, "93.75g all-purpose flour", white, 22)
    cakeMetricIngredients3_text = classes.Text(315, 185, "200g granulated sugar", white, 22)
    cakeMetricIngredients4_text = classes.Text(315, 205, "4g baking powder", white, 22)
    cakeMetricIngredients5_text = classes.Text(315, 225, "3g baking soda", white, 22)
    cakeMetricIngredients6_text = classes.Text(315, 245, "4.5g kosher salt", white, 22)
    cakeMetricIngredients7_text = classes.Text(315, 265, "170.25g unsalted butter, softened", white, 22)
    cakeIngredients8_text = classes.Text(315, 285, "2 large eggs", white, 22)
    cakeMetricIngredients9_text = classes.Text(315, 305, "153g sour cream/ Greek yogurt", white, 22)
    cakeIngredients10_text = classes.Text(315, 325, "/ buttermilk (can be substituted)", white, 22)
    cakeMetricIngredients11_text = classes.Text(315, 345, "122ml milk", white, 22)
    cakeMetricIngredients12_text = classes.Text(315, 365, "8g vanilla extract", white, 22)
    buttercreamIngredientsLabel_text = classes.Text(315, 405, "Buttercream Ingredients: ", white, 22)
    cakeMetricIngredients13_text = classes.Text(315, 445, "225g unsalted butter , softened", white, 22)
    cakeMetricIngredients14_text = classes.Text(315, 465, "500g soft icing sugar", white, 22)
    cakeIngredients15_text = classes.Text(315, 485, "/ powdered sugar, SIFTED", white, 22)
    cakeMetricIngredients16_text = classes.Text(315, 505, "15ml vanilla extract", white, 22)
    cakeMetricIngredients17_text = classes.Text(315, 525, "19-58ml milk, to adjust thickeness", white, 22)

    cakeUSIngredients1_text = classes.Text(315, 145, "1 1/2 cups cake flour", white, 22)
    cakeUSIngredients2_text = classes.Text(315, 165, "3/4 cup all-purpose flour", white, 22)
    cakeUSIngredients3_text = classes.Text(315, 185, "1 cup granulated sugar", white, 22)
    cakeUSIngredients4_text = classes.Text(315, 205, "1 teaspoon baking powder", white, 22)
    cakeUSIngredients5_text = classes.Text(315, 225, "1 teaspoon baking soda", white, 22)
    cakeUSIngredients6_text = classes.Text(315, 245, "3/4 teaspoon kosher salt", white, 22)
    cakeUSIngredients7_text = classes.Text(315, 265, "3/4 cup unsalted butter, softened", white, 22)
    cakeUSIngredients9_text = classes.Text(315, 305, "2/3 cup sour cream, Greek yogurt", white, 22)
    cakeUSIngredients11_text = classes.Text(315, 345, "1/2 cup milk", white, 22)
    cakeUSIngredients12_text = classes.Text(315, 365, "2 teaspoons vanilla extract", white, 22)
    cakeUSIngredients13_text = classes.Text(315, 445, "1 cup unsalted butter , softened", white, 22)
    cakeUSIngredients14_text = classes.Text(315, 465, "2 1/2 soft icing sugar", white, 22)
    cakeUSIngredients16_text = classes.Text(315, 505, "3 tsp vanilla extract", white, 22)
    cakeUSIngredients17_text = classes.Text(315, 525, "2–4 tbsp milk, to adjust thickeness", white, 22)

    sushiIngredients1_text = classes.Text(315, 145, "1 nori / sushi sheets", white, 22)
    sushiMetricIngredients2_text = classes.Text(315, 165, "10g of sushi seasoning", white, 22)
    sushiIngredients3_text = classes.Text(315, 185, "/ sushi vinegar, adjust to taste", white, 22)
    sushiMetricIngredients4_text = classes.Text(315, 205, "200g sushi rice / short grain rice", white, 22)
    sushiMetricIngredients5_text = classes.Text(315, 225, "85g of salmon", white, 22)
    sushiIngredients6_text = classes.Text(315, 245, "Half of a cucumber", white, 22)
    sushiIngredients7_text = classes.Text(315, 265, "Half of an avocado", white, 22)

    sushiUSIngredients2_text = classes.Text(315, 165, "2/3 tbsp of sushi seasoning", white, 22)
    sushiUSIngredients4_text = classes.Text(315, 205, "1 cup sushi rice / short grain rice", white, 22)
    sushiUSIngredients5_text = classes.Text(315, 225, "1 packet of salmon", white, 22)

    burgerMetricIngredients = [ingredientsLabel_text, burgerMetricIngredients1_text, burgerMetricIngredients2_text, burgerMetricIngredients3_text,
                               burgerMetricIngredients4_text, burgerIngredients5_text, burgerMetricIngredients6_text,
                               burgerIngredients7_text, burgerMetricIngredients8_text, burgerMetricIngredients9_text,]
    burgerUSIngredients = [ingredientsLabel_text, burgerUSIngredients1_text, burgerUSIngredients2_text, burgerUSIngredients3_text,
                           burgerUSIngredients4_text, burgerIngredients5_text, burgerUSIngredients6_text,
                           burgerIngredients7_text, burgerUSIngredients8_text, burgerUSIngredients9_text,]
    
    cakeMetricIngredients = [cakeIngredientsLabel_text, cakeMetricIngredients1_text, cakeMetricIngredients2_text, cakeMetricIngredients3_text,
                             cakeMetricIngredients4_text, cakeMetricIngredients5_text, cakeMetricIngredients6_text,
                             cakeMetricIngredients7_text, cakeIngredients8_text, cakeMetricIngredients9_text,
                             cakeIngredients10_text, cakeMetricIngredients11_text, cakeMetricIngredients12_text, buttercreamIngredientsLabel_text,
                             cakeMetricIngredients13_text, cakeMetricIngredients14_text, cakeIngredients15_text,
                             cakeMetricIngredients16_text, cakeMetricIngredients17_text]
    cakeUSIngredients = [cakeIngredientsLabel_text, cakeUSIngredients1_text, cakeUSIngredients2_text, cakeUSIngredients3_text,
                             cakeUSIngredients4_text, cakeUSIngredients5_text, cakeUSIngredients6_text,
                             cakeUSIngredients7_text, cakeIngredients8_text, cakeUSIngredients9_text,
                             cakeIngredients10_text, cakeUSIngredients11_text, cakeUSIngredients12_text, buttercreamIngredientsLabel_text,
                             cakeUSIngredients13_text, cakeUSIngredients14_text, cakeIngredients15_text,
                             cakeUSIngredients16_text, cakeUSIngredients17_text]
    
    sushiMetricIngredients = [ ingredientsLabel_text, sushiIngredients1_text, sushiMetricIngredients2_text, sushiIngredients3_text,
                              sushiMetricIngredients4_text, sushiMetricIngredients5_text, sushiIngredients6_text,
                              sushiIngredients7_text]
    sushiUSIngredients = [ingredientsLabel_text, sushiIngredients1_text, sushiUSIngredients2_text, sushiIngredients3_text,
                          sushiUSIngredients4_text, sushiUSIngredients5_text, sushiIngredients6_text,
                          sushiIngredients7_text]

    if recipeChosen == "burger":
        if measurementType:
            ingredients = burgerMetricIngredients
        else:
            ingredients = burgerUSIngredients
    elif recipeChosen == "cake":
        if measurementType:
            ingredients = cakeMetricIngredients
        else:
            ingredients = cakeUSIngredients
    elif recipeChosen == "sushi":
        if measurementType:
            ingredients = sushiMetricIngredients
        else:
            ingredients = sushiUSIngredients

    #button object creation
    back_button = classes.Button(65, 50, 70, 100, colours[3], False)
    fullRecipe_button = classes.Button(170, 375, 30, 180, colours[4], False)
    start_button = classes.Button(415, 420, 30, 180, colours[5], False)
    exit_button = classes.Button(705, 85, 40, 40, login_red1, False)
    recipePageR_button = classes.Button(685, 535, 30, 30, colours[4], False)
    recipePageL_button = classes.Button(310, 535, 30, 30, colours[4], False)

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
                startPressed = start_button.checkPressed(pygame.mouse.get_pos())
                if startPressed:
                    recipeLoop = False
                    minigameLoop = True
        
        #drawing onto screen
        globalvariables.WIN.blit(mainBg_image, bgPosition)
        globalvariables.WIN.blit(scaled_gameLogo, (450,10))
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
            globalvariables.WIN.blit(scaled_burger, (380, 180))
            globalvariables.WIN.blit(scaled_halal, (150, 247))
            globalvariables.WIN.blit(scaled_vegetarian, (230, 247))
            globalvariables.WIN.blit(scaled_vegan, (310, 247))
            easy_text.drawText()
            burgerDescription1_text.drawText()
            burgerDescription2_text.drawText()
            burgerDescription3_text.drawText()
            burgerDescription4_text.drawText()
        elif recipeChosen == "cake":
            cakeLabel_text.drawText()
            globalvariables.WIN.blit(scaled_cake, (420, 210))
            globalvariables.WIN.blit(scaled_halal, (190, 247))
            globalvariables.WIN.blit(scaled_vegetarian, (265, 247))
            medium_text.drawText()
            cakeDescription1_text.drawText()
            cakeDescription2_text.drawText()
            cakeDescription3_text.drawText()
            cakeDescription4_text.drawText()
        elif recipeChosen == "sushi":
            sushiLabel_text.drawText()
            globalvariables.WIN.blit(scaled_sushi, (420, 210))
            globalvariables.WIN.blit(scaled_halal, (230, 247))
            hard_text.drawText()
            sushiDescription1_text.drawText()
            sushiDescription2_text.drawText()
            sushiDescription3_text.drawText()
            sushiDescription4_text.drawText()
        elif recipeChosen == "cheese fondue":
            cheeseFondueLabel_text.drawText()
            globalvariables.WIN.blit(scaled_cheeseFondue, (420, 220))
            globalvariables.WIN.blit(scaled_vegetarian, (230, 247))
            medium_text.drawText()
            cheeseFondueDescription1_text.drawText()
            cheeseFondueDescription2_text.drawText()
            cheeseFondueDescription3_text.drawText()
            cheeseFondueDescription4_text.drawText()
        elif recipeChosen == "croissant":
            croissantLabel_text.drawText()
            globalvariables.WIN.blit(scaled_croissant, (420, 220))
            globalvariables.WIN.blit(scaled_halal, (190, 247))
            globalvariables.WIN.blit(scaled_vegetarian, (265, 247))
            easy_text.drawText()
            croissantDescription1_text.drawText()
            croissantDescription2_text.drawText()
            croissantDescription3_text.drawText()
            croissantDescription4_text.drawText()
        elif recipeChosen == "tofu":
            tofuLabel_text.drawText()
            globalvariables.WIN.blit(scaled_tofu, (420, 220))
            globalvariables.WIN.blit(scaled_halal, (150, 247))
            globalvariables.WIN.blit(scaled_vegetarian, (230, 247))
            globalvariables.WIN.blit(scaled_vegan, (310, 247))
            medium_text.drawText()
            tofuDescription1_text.drawText()
            tofuDescription2_text.drawText()
            tofuDescription3_text.drawText()
            tofuDescription4_text.drawText()

        fullRecipeActive = fullRecipe_button.getActive()
        #if the full recipe button has been pressed
        measurementType = bool(database.getData_main(username, "measurement_type"))
        #checks what measurement type the user prefers

        if fullRecipeActive:
            fullRecipeBg_box.drawBox() #draw the boxes
            exit_button.drawBox()
            exit_text.drawText()
            if recipeChosen == "burger": #if the user is on the burger recipe page
                if count == 0: #it will begin on the first page so
                    recipePageR_button.drawBox() #it will only have the right arrow button
                    recipePageR_text.drawText()
                    for i in range(len(ingredients)):
                        ingredients[i].drawText() 
                        #displays ingredients depending on measurement type
            
                if count == 1: #if the user clicks the right arrow
                    recipePageL_button.drawBox() #display all the text and the buttons
                    recipePageL_text.drawText()
                    for i in range (len(burgerRecipe)):
                        burgerRecipe[i].drawText()
                
            elif recipeChosen == "cake": #if on cake recipe page
                if count == 0: #it will begin on the first page so
                    recipePageR_button.drawBox() #it will only have the right arrow button
                    recipePageR_text.drawText()
                    for i in range(len(ingredients)):
                        ingredients[i].drawText() 
                        #displays ingredients depending on measurement type
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
                if count == 0: #it will begin on the first page so
                    recipePageR_button.drawBox() #it will only have the right arrow button
                    recipePageR_text.drawText()
                    for i in range(len(ingredients)):
                        ingredients[i].drawText() 
                        #displays ingredients depending on measurement type
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
    return mainLoop, recipeLoop, minigameLoop, recipeChosen, ingredients

def minigameScreen(minigameLoop, recipeLoop, recipeChosen, theme_selected, ingredients):

    startingScreen = True #the starting screen will show all the steps, this will reappear every time the user finishes a minigame
    exitMessage = False #this will be set to true when the user presses the back button
    stack = deque([]) #creates a stack to traverse through the nodes within the tree
    visitedNodes = [] #contains all the visited nodes
    flag = True #indicates whether to traverse the tree
    score = 0
    value = ""
    minigame = False

    if theme_selected == "theme1": #changes the colours of the boxes and buttons depending on the theme that has been chosen
            colours = [main_lightPurple1, main_lightPurple2, main_darkPurple1, main_darkPurple2, main_darkPurple3, main_brightPurple]
            gameBg_image = game1Bg_image
    elif theme_selected == "theme2":
        colours = [main_lightOrange1, main_lightOrange2, main_darkOrange1, main_darkOrange2, main_darkOrange3, main_brightOrange]
        gameBg_image = gameBg_image

    #text
    back_text = classes.Text(80, 55, "<--", white, 50)
    burgerLabel_text = classes.Text(480, 55, "Burger", white, 22)
    cakeLabel_text = classes.Text(480, 55, "Cake", white, 22)
    sushiLabel_text = classes.Text(480, 55, "Sushi", white, 22)

    gameLabel1_burger_text = classes.Text(330, 153, "Frying", white, 24)
    gameLabel2_burger_text = classes.Text(330, 233, "Mixing", white, 24)
    gameLabel3_burger_text = classes.Text(320, 313, "Shaping", white, 24)
    gameLabel4_burger_text = classes.Text(320, 393, "Grilling", white, 24)
    gameLabel5_burger_text = classes.Text(320, 473, "Assembly", white, 24)

    gameLabel1_cake_text = classes.Text(330, 153, "Mixing", white, 24)
    gameLabel2_cake_text = classes.Text(330, 233, "Baking", white, 24)
    gameLabel3_cake_text = classes.Text(320, 313, "Frosting", white, 24)
    gameLabel4_cake_text = classes.Text(320, 393, "Decoration", white, 24)

    gameLabel1_sushi_text = classes.Text(330, 153, "Cooking", white, 24)
    gameLabel2_sushi_text = classes.Text(330, 233, "Assembly", white, 24)
    gameLabel3_sushi_text = classes.Text(320, 313, "Cutting", white, 24)

    start_text = classes.Text(615, 153, "Start", white, 24)

    locked2_text = classes.Text(610, 233, "Locked", white, 24)
    locked3_text = classes.Text(610, 313, "Locked", white, 24)
    locked4_text = classes.Text(610, 393, "Locked", white, 24)
    locked5_text = classes.Text(610, 473, "Locked", white, 24)

    completed1_text = classes.Text(610, 153, "Completed", white, 24)
    completed2_text = classes.Text(610, 233, "Completed", white, 24)
    completed3_text = classes.Text(610, 313, "Completed", white, 24)
    completed4_text = classes.Text(610, 393, "Completed", white, 24)


    exitMessage1_text = classes.Text(285, 172, "Are you sure you want to exit?", white, 35)
    exitMessage2_text = classes.Text(330, 212, "Your progress will not save.", white, 30)
    exitYes_text = classes.Text(347, 292, "Yes", (100, 0, 0), 24)
    exitNo_text = classes.Text(637, 292, "No", (100, 0, 0), 24)

    #boxes
    recipeLabel_box = classes.Box(410, 50, 40, 200, colours[5], False)
    gameLabel1_box = classes.Box(260, 150, 40, 200, colours[1], False)
    gameLabel2_box = classes.Box(260, 230, 40, 200, colours[1], False)
    gameLabel3_box = classes.Box(260, 310, 40, 200, colours[1], False)
    gameLabel4_box = classes.Box(260, 390, 40, 200, colours[1], False)
    gameLabel5_box = classes.Box(260, 470, 40, 200, colours[1], False)
    start1_box = classes.Box(550, 150, 40, 200, colours[2], False)
    start2_box = classes.Box(550, 230, 40, 200, colours[2], False)
    start3_box = classes.Box(550, 310, 40, 200, colours[2], False)
    start4_box = classes.Box(550, 390, 40, 200, colours[2], False)
    start5_box = classes.Box(550, 470, 40, 200, colours[2], False)
    exitMessage_box = classes.Box(260, 150, 200, 500, login_red1, False)


    #buttons
    back_button = classes.Button(65, 50, 70, 100, colours[3], False)
    start1_button = classes.Button(550, 150, 40, 200, colours[2], False)
    start2_button = classes.Button(550, 230, 40, 200, colours[2], False)
    start3_button = classes.Button(550, 310, 40, 200, colours[2], False)
    start4_button = classes.Button(550, 390, 40, 200, colours[2], False)
    start5_button = classes.Button(550, 470, 40, 200, colours[2], False)
    exitYes_button = classes.Button(320, 290, 40, 100, white, False)
    exitNo_button = classes.Button(610, 290, 40, 100, white, False)


    while minigameLoop:

        for event in pygame.event.get(): #allows user to quit the window
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if startingScreen: #the back button will only be available on the starting screen so if it's true
                    backPressed = back_button.checkPressed(pygame.mouse.get_pos()) #checks if it has been pressed
                    if backPressed: #if it has
                        exitMessage = True #output the exit message
                    exitYesPressed = exitYes_button.checkPressed(pygame.mouse.get_pos()) 
                    if exitYesPressed: #if yes has been pressed
                        minigameLoop = False
                        recipeLoop = True #go back to recipe screen
                    exitNoPressed = exitNo_button.checkPressed(pygame.mouse.get_pos())
                    if exitNoPressed: #if no has been pressed
                        exitMessage = False #remove the exit message

                    start1Pressed = start1_button.checkPressed(pygame.mouse.get_pos())
                    start1Active = start1_button.getActive()
                    if start1Pressed == True and start1Active == False:
                        minigame = True

                    start2Pressed = start2_button.checkPressed(pygame.mouse.get_pos())
                    start2Active = start2_button.getActive()
                    if start2Pressed == True and start2Active == False:
                        minigame = True

                    start3Pressed = start3_button.checkPressed(pygame.mouse.get_pos())
                    start3Active = start3_button.getActive()
                    if start3Pressed == True and start3Active == False:
                        minigame = True

                    start4Pressed = start4_button.checkPressed(pygame.mouse.get_pos())
                    start4Active = start4_button.getActive()
                    if start4Pressed == True and start4Active == False:
                        minigame = True

                    start5Pressed = start5_button.checkPressed(pygame.mouse.get_pos())
                    start5Active = start5_button.getActive()
                    if start5Pressed == True and start5Active == False:
                        minigame = True

        #tree traversal
        if flag:
            value, stack, visitedNodes = minigames.treeTraversal(recipeChosen, stack, visitedNodes)
            flag = False
        #print(value)
        #displaying onto the screen
        globalvariables.WIN.blit(gameBg_image, bgPosition)

        if startingScreen:
            back_button.drawBox()
            back_text.drawText()
            recipeLabel_box.drawBox()
            gameLabel1_box.drawBox()
            gameLabel2_box.drawBox()
            gameLabel3_box.drawBox()

            if recipeChosen == "burger":
                burgerLabel_text.drawText()
                gameLabel4_box.drawBox()
                gameLabel5_box.drawBox()
                start1_box.drawBox()
                start2_box.drawBox()
                start3_box.drawBox()
                start4_box.drawBox()
                start5_box.drawBox()
                gameLabel1_burger_text.drawText()
                gameLabel2_burger_text.drawText()
                gameLabel3_burger_text.drawText()
                gameLabel4_burger_text.drawText()
                gameLabel5_burger_text.drawText()
                
                print(value)
                if value == "Frying":
                    start1_button.drawBox()
                    start_text.drawText()
                    locked2_text.drawText()
                    locked3_text.drawText()
                    locked4_text.drawText()
                    locked5_text.drawText()
                elif value == "Mixing":
                    start2_button.drawBox()
                    completed1_text.drawText()
                    start_text.changePosition(615,233)
                    locked3_text.drawText()
                    locked4_text.drawText()
                    locked5_text.drawText()
                elif value == "Shaping":
                    start3_button.drawBox()
                    start_text.changePosition(615,313)
                    locked4_text.drawText()
                    locked5_text.drawText()
                elif value == "Grilling":
                    start4_button.drawBox()
                    completed1_text.drawText()
                    completed2_text.drawText()
                    completed3_text.drawText()
                    start_text.changePosition(615,393)
                    locked5_text.drawText()
                elif value == "Assembly":
                    start5_button.drawBox()
                    completed1_text.drawText()
                    completed2_text.drawText()
                    completed3_text.drawText()
                    completed4_text.drawText()
                    start_text.changePosition(615,473)

            elif recipeChosen == "cake":
                cakeLabel_text.drawText()
                gameLabel4_box.drawBox()
                start1_box.drawBox()
                start2_box.drawBox()
                start3_box.drawBox()
                start4_box.drawBox()
                gameLabel1_cake_text.drawText()
                gameLabel2_cake_text.drawText()
                gameLabel3_cake_text.drawText()
                gameLabel4_cake_text.drawText()

                if value == "Mixing":
                    start1_button.drawBox()
                    start_text.drawText()
                    locked2_text.drawText()
                    locked3_text.drawText()
                    locked4_text.drawText()
                elif value == "Baking":
                    start2_button.drawBox()
                    completed1_text.drawText()
                    start_text.changePosition(615,233)
                    locked3_text.drawText()
                    locked4_text.drawText()
                elif value == "Frosting":
                    start3_button.changeY(390)
                    completed1_text.drawText()
                    completed2_text.drawText()
                    start_text.changePosition(615,313)
                    locked4_text.drawText()
                elif value == "Decoration":
                    start4_button.drawBox()
                    completed1_text.drawText()
                    completed2_text.drawText()
                    completed3_text.drawText()
                    start_text.changePosition(615,393)

            elif recipeChosen == "sushi":
                start1_box.drawBox()
                start2_box.drawBox()
                start3_box.drawBox()
                sushiLabel_text.drawText()
                gameLabel1_sushi_text.drawText()
                gameLabel2_sushi_text.drawText()
                gameLabel3_sushi_text.drawText()

                if value == "Cooking":
                    start1_button.drawBox()
                    start_text.drawText()
                    locked2_text.drawText()
                    locked3_text.drawText()
                elif value == "Assembly":
                    start2_button.drawBox()
                    completed1_text.drawText()
                    start_text.changePosition(615,233)
                    locked3_text.drawText()
                elif value == "Cutting":
                    start3_button.drawBox()
                    completed1_text.drawText()
                    completed2_text.drawText()
                    start_text.changePosition(615,313)
            
            if exitMessage:
                exitMessage_box.drawBox()
                exitMessage1_text.drawText()
                exitMessage2_text.drawText()
                exitYes_button.drawBox()
                exitYes_text.drawText()
                exitNo_button.drawBox()
                exitNo_text.drawText()

        if minigame:
            if recipeChosen == "burger":
                value, stack, visitedNodes = minigames.burgerGame(value, stack, visitedNodes, score, colours, ingredients)
                flag = True
                minigame = False
            elif recipeChosen == "cake":
                value, stack, visitedNodes = minigames.cakeGame(value, stack, visitedNodes, score,  colours, ingredients)
                flag = True
                minigame = False
            elif recipeChosen == "sushi":
                value, stack, visitedNodes = minigames.sushiGame(value, stack, visitedNodes, score, colours, ingredients)
                flag = True
                minigame = False

        pygame.display.update()
    
    return minigameLoop, recipeLoop, recipeChosen
        
def playDisc(disc_selected):
    if disc_selected == "disc1":
            pygame.mixer.music.load(os.path.join('Culinary Quest ASSETS',"gingko.mp3"))
    elif disc_selected == "disc2":
        pygame.mixer.music.load(os.path.join('Culinary Quest ASSETS',"old_feelings.mp3"))
    elif disc_selected == "disc3":
        pygame.mixer.music.load(os.path.join('Culinary Quest ASSETS',"sunday_morning.mp3"))
    pygame.mixer.music.play(-1)

def main(loginLoop, createLoop, mainLoop, settingsLoop, shopLoop, recipeLoop, minigameLoop):
    clock = pygame.time.Clock()
    clock.tick(globalvariables.FPS)
    run = True
    #loops

    #input boxes
    usernameInput1_input = classes.Input(480, 330, 37, 280, black, 20, False)
    passwordInput1_input = classes.Input(480, 400, 37, 280, black, 20, True)
    usernameInput2_input = classes.Input(480, 230, 37, 280, black, 20, False)
    passwordInput2_input = classes.Input(480, 290, 37, 280, black, 20, True)
    search_input = classes.Input(240, 100, 37, 570, black, 20, False)
    recipeChosen = ""
    theme_selected = ""
    oldPassInput_input = classes.Input(350, 250, 30, 280, black, 20, True)
    newPassInput_input = classes.Input(350, 310, 30, 280, black, 20, True)


    while run:
            
        if loginLoop == True:
            pygame.mixer.music.set_volume(0)
            loginLoop, createLoop, mainLoop, username = loginScreen(usernameInput1_input, passwordInput1_input, loginLoop, createLoop, mainLoop)
            if mainLoop:
                disc_selected = str(database.getData_main(username, "disc_selected"))
                playDisc(disc_selected)

        if createLoop == True:
            createLoop, loginLoop = createScreen(usernameInput2_input, passwordInput2_input, createLoop, loginLoop)

        if mainLoop == True:
            theme_selected = str(database.getData_main(username, "theme_selected"))
            volume_level = database.getData_main(username, "volume_level")
            pygame.mixer.music.set_volume((volume_level) / 100)
            mainLoop, shopLoop, settingsLoop, recipeLoop, recipeChosen = mainScreen(search_input, mainLoop, shopLoop, settingsLoop, recipeLoop, recipeChosen, username, theme_selected) 
        
        if shopLoop == True:
            mainLoop, shopLoop, disc_selected, theme_selected = shopScreen(mainLoop, shopLoop, username, theme_selected)
            playDisc(disc_selected)

        if settingsLoop == True:
            mainLoop, settingsLoop = settingsScreen(mainLoop, settingsLoop, oldPassInput_input, newPassInput_input, username, theme_selected)

        if recipeLoop == True:
            mainLoop, recipeLoop, minigameLoop, recipeChosen, ingredients = recipeScreen(mainLoop, recipeLoop, minigameLoop, recipeChosen, username, theme_selected)

        if minigameLoop == True:
            minigameLoop, recipeLoop, recipeChosen = minigameScreen(minigameLoop, recipeLoop, recipeChosen, theme_selected, ingredients)

loginLoop = True
createLoop = False
mainLoop = False
settingsLoop = False
shopLoop = False
recipeLoop = False
minigameLoop = False

main(loginLoop, createLoop, mainLoop, settingsLoop, shopLoop, recipeLoop, minigameLoop)