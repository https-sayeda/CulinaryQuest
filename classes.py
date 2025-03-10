import globalvariables
import pygame
import os

specialCharacters = "!£$%^&*()_+-={['#~.,<>/?|\¬`;:}]@"

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
        globalvariables.WIN.blit(drawnText, (self.x,self.y))
    
    def changePosition(self, newX, newY):
        drawnText = pygame.font.Font(os.path.join('Culinary Quest ASSETS', 'Aptos.ttf'), self.size).render(self.text, True, self.colour)
        globalvariables.WIN.blit(drawnText, (newX,newY))

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
            pygame.draw.rect(globalvariables.WIN, self.colour, pygame.Rect(self.x, self.y, self.length, self.height) ,0, 3)
        else:
            boxSurface = pygame.Surface((self.length, self.height),pygame.SRCALPHA)
            boxSurface.set_alpha(200)
            pygame.draw.rect(boxSurface, self.colour, boxSurface.get_rect(), 0, 3)
            globalvariables.WIN.blit(boxSurface, (self.x, self.y))
    
    def changeLength(self, size):
        self.length = self.length + size #adds the value passed to the subroutine to the current length of the box
        return self.length #returns the length of the box

    def changeHeight(self, size):
        self.height = self.height + size #adds the value passed to the subroutine to the current length of the box
        return self.height #returns the length of the box

    def changeY(self, y_coordinate):
        self.y = y_coordinate
        return self.y
    
    
    def changeColour(self, colour):
        self.colour = colour

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
        globalvariables.WIN.blit(self.image, (self.rect.x, self.rect.y))
    
    def changePosition(self, newX, newY):
        #changes position of the button if needed
        globalvariables.WIN.blit(self.image, (newX, newY))
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
        self.colourBox = (242, 234, 239)
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
        pygame.draw.rect(globalvariables.WIN, self.colourBox, self.rect, 0, 3)
        globalvariables.WIN.blit(self.text_surface, (self.rect.x+5, self.rect.y+5))

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
