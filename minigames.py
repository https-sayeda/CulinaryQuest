# Imports
import sys
import pygame
import random
import os
from collections import deque


class RecipeTree:

    def __init__(self, value):
        self.value = value
        #self.recipe = recipe
        self.children = []
    
    def add_child(self, child_node):
        self.children.append(child_node)
    
    def preorder(root):
 
        stack = deque([]) #creates a stack to traverse through the nodes within the tree
        visitedNodes = [] #contains all the visited nodes
        visitedNodes.append(root.value) #adds the root node to the array
        stack.append(root) #adds the root to the stack (it has been visited)

        while len(stack) > 0: #while there are still nodes in the stack
            all_children_visited = True 
            #checks whether all the child nodes have been visited (initially set to true)
            parent = stack[len(stack)-1] #the top of the stack is a parent (it has child nodes)

            for i in range(0, len(parent.children)): #goes through the child nodes of the parent
                if parent.children[i].value not in visitedNodes: #if there is a child that is unvisited
                    stack.append(parent.children[i]) #push it to the stack
                    visitedNodes.append(parent.children[i].value) #add it to the array of visited nodes
                    all_children_visited = False #then all the children haven't been visited
                    break
    
            if all_children_visited == True: #if all the children of the parent have been visited
                stack.pop() #remove the parent from the stack 
        print(visitedNodes)
        
def treeTraversal():
    burgerRoot = RecipeTree("Burger")
    burgerRoot.children = [RecipeTree("Frying"), RecipeTree("Mixing"), RecipeTree("Shaping"), RecipeTree("Grilling"), RecipeTree("Assembly")]
    burgerRoot.children[0].children = [RecipeTree("Frying 1"), RecipeTree("Frying 2"), RecipeTree("Frying 3"), RecipeTree("Frying 4")]
    burgerRoot.children[1].children = [RecipeTree("Mixing 1"), RecipeTree("Mixing 2"), RecipeTree("Mixing 3"), RecipeTree("Step 4")]
    burgerRoot.children[2].children = [RecipeTree("Shaping 1")]
    burgerRoot.children[3].children = [RecipeTree("Grilling 1"), RecipeTree("Grilling 2")]
    burgerRoot.children[4].children = [RecipeTree("Assembly 1")]
    burgerRoot.preorder()


def draw(WIN, draw, x1, y1, x2, y2, x3, y3, x4, y4):

    flag1 = False #these flags represent whether the drawn circle has touched a coordinate
    flag2 = False #there are 4 points to the arrow, so four coordinates (x1, y2), (x2, y2) etc. = four flags
    flag3 = False 
    flag4 = False
    # the colour and size of the brush
    drawColour = [0, 0, 255]
    brushSize = 10
    canvasSize = [800, 800]

    # Canvas
    canvas = pygame.Surface((canvasSize),pygame.SRCALPHA)
    canvas.set_alpha(200) 
    #makes the canvas transparent so that it doesn't cover the background image

    while draw: #ensures that the user only draws when they havent drawn the arrow
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break
        # Draw the Canvas at the center of the screen
        x, y = WIN.get_size() 
        WIN.blit(canvas, [x/2 - canvasSize[0]/2, y/2 - canvasSize[1]/2])
        if flag1 == True and flag2 == True and flag3 == True and flag4 == True: 
            #if all the flags have been set to true, they can no longer draw
            draw = False
            pygame.display.update() #updates the screen to show the final arrow 

        dx = 0 
        dy = 0
        # Drawing with the mouse
        if pygame.mouse.get_pressed()[0]: #if the mouse is pressed
            mx, my = pygame.mouse.get_pos() #get the position of the mouse

            # Calculate the position of the mouse on the Canvas
            dx = mx - x/2 + canvasSize[0]/2
            dy = my - y/2 + canvasSize[1]/2

            pygame.draw.circle(canvas, drawColour,[dx, dy], brushSize) #draws the circle

        if (x1-5.0) <= dx <= (x1+5.0) and (y1-5.0) <= dy <= (y1+5.0): 
            #this  ensures that the user doesnt need to get an exact coordinate, but instead a range within
            #a certain area
            flag1 = True #if the circle is drawn in the range, then the flag is set to true
        if (x2-5.0) <= dx <= (x2+5.0) and (y2-5.0) <= dy <= (y2+5.0):
            flag2 = True
        if (x3-5.0) <= dx <= (x3+5.0) and (y3-5.0) <= dy <= (y3+5.0):
            flag3 = True
        if (x4-5.0) <= dx <= (x4+5.0) and (y4-5.0) <= dy <= (y4+5.0):
            flag4 = True

        pygame.display.update() #updates the screen
      
def assembly(window_x, window_y, WIN, main1Bg_image, bgPosition, assembly):

    hand_width = 150
    hand_height = 150
    hand_x = window_x // 2 - hand_width
    hand_y = window_y - hand_height - 20
    hand_speed = 10
    component_width = 200
    component_height = 100
    component_speed = 5
    count = 0
    layer_x = ((hand_x + hand_width + 10) // 2)

    #images
    hand_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','hand.png'))
    topBun_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','burger_bun.png'))
    bottomBun_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','burger_bottombun.png'))
    cheeseLayer_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','burger_cheese.png'))
    lettuceLayer_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','burger_lettuce.png'))
    onionLayer_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','burger_onion.png'))
    meatLayer_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','burger_meat.png'))
    tomatoLayer_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','burger_tomato.png'))
    
    #transforming images
    hand_image = pygame.transform.scale(hand_image, (hand_width, hand_height))
    topBun_image = pygame.transform.scale(topBun_image, (component_width, component_height))
    bottomBun_image = pygame.transform.scale(bottomBun_image, (component_width, component_height))
    cheeseLayer_image = pygame.transform.scale(cheeseLayer_image, (component_width, component_height))
    lettuceLayer_image = pygame.transform.scale(lettuceLayer_image, (component_width, component_height))
    onionLayer_image = pygame.transform.scale(onionLayer_image, (component_width, component_height))
    meatLayer_image = pygame.transform.scale(meatLayer_image, (component_width, component_height))
    tomatoLayer_image = pygame.transform.scale(tomatoLayer_image, (component_width, component_height))

    burgerLayer_images = [bottomBun_image, lettuceLayer_image, meatLayer_image, cheeseLayer_image, tomatoLayer_image, onionLayer_image, topBun_image]
    burgerLayer_order = []


    component_x = random.randint(0, window_x - component_width)
    component_y = 0
    
    clock = pygame.time.Clock()

    while assembly == True and count != 7:

        clock.tick(60)
        WIN.blit(main1Bg_image, bgPosition)
        component_rect = WIN.blit(burgerLayer_images[count], (component_x, component_y))
        #a rect is created for the component and hand that will be used to detect a collision between them
        hand_rect = WIN.blit(hand_image, (hand_x, hand_y))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break

        keys = pygame.key.get_pressed()

        if len(burgerLayer_order) != 0: #checks that at least one component has been caught
            layer_x = hand_x
            for i in range(len(burgerLayer_order)): #goes through array
                WIN.blit(burgerLayer_order[i], (layer_x, hand_y - (10*(i+1)))) 
                #displays them on top of each other
            if keys[pygame.K_LEFT] == True or keys[pygame.K_a] == True:
                layer_x -= hand_speed
            if keys[pygame.K_RIGHT] == True or keys[pygame.K_d] == True:
                layer_x += hand_speed #makes sure the components moves with the hand
        
        if keys[pygame.K_LEFT] == True or keys[pygame.K_a] == True:
            hand_x -= hand_speed
        if keys[pygame.K_RIGHT] == True or keys[pygame.K_d] == True:
            hand_x += hand_speed
            
        if hand_x <= 0: #prevents hand from moving off screen
            hand_x = 0
        elif hand_x >= (window_x - hand_width):
            hand_x = (window_x - hand_width)
        
        component_y += component_speed

        if component_y > window_y: #if component falls off the screen
            component_x = random.randint(0, window_x - component_width) #new x coordinate is generated
            component_y = 0
        elif hand_rect.colliderect(component_rect): #if the component and hand collide..
            burgerLayer_order.append(burgerLayer_images[count]) #adds the correct layer to the array
            component_x = random.randint(0, window_x - component_width) #generates new x coordinate
            component_y = 0
            if count != 7:
                count = count + 1 #increments count to show that the next layer should be displayed

        pygame.display.update()
    
        if count == 7: #if all layers have been displayed
            assembly = False #minigame ends

    return assembly

def flip(flip, WIN, bar_x, bar_y, main1Bg_image, bgPosition):
    
    #variables that are needed
    arrow_speed = 7.5
    bar_width = 200
    bar_height = 500
    arrow_width = 100
    arrow_height = 100
    arrow_x = bar_x - 100
    bar_bottom = bar_y + (bar_height // 2) + 170
    bar_top = bar_y - 20
    arrow_y = bar_bottom
    top_reached = False
    bottom_reached = True

    #loading images
    temperatureBar_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','temperature_bar.png'))
    arrow_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','arrow.png'))

    #transforming images
    temperatureBar_image = pygame.transform.scale(temperatureBar_image, (bar_width, bar_height))
    arrow_image = pygame.transform.scale(arrow_image, (arrow_width, arrow_height))

    while flip: #while it is running

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break
        
        #displaying the images on the screen
        WIN.blit(main1Bg_image, bgPosition)
        WIN.blit(temperatureBar_image, (bar_x, bar_y))
        WIN.blit(arrow_image, (arrow_x, arrow_y))

        keys = pygame.key.get_pressed() 
        if keys[pygame.K_SPACE] != True: #while the space key has not been pressed

            if top_reached != True: #checks that the arrow has not reached the top of the bar
                arrow_y -= arrow_speed #will move upwards
                if arrow_y <= bar_top: #if it has reached the top
                    top_reached = True #set to true
                    bottom_reached = False #if it's at the top, it is not at the bottom so set to false
            elif bottom_reached != True: #if the bottom hasn't been reached
                arrow_y += arrow_speed #it will move downwards
                if arrow_y >= bar_bottom: #if it reaches the bottom
                    bottom_reached = True
                    top_reached = False

        else: #if the space key is pressed then..
            WIN.blit(arrow_image, (arrow_x, arrow_y)) #stop the arrow at that position
            flip = False #no longer running


        pygame.display.update()

def fill(fill, WIN, fill_colour, fillBg_box, fill_box, fill_line, main1Bg_image, bgPosition):
    
    fill_box.changeColour(fill_colour) 
    #the colour will change depending on the recipe as sushi uses water while cake will use cake batter
    fill_height = 0 #the initial height of the liquid is 0
    spacebar_down = False #the spacebar being pressed is initially set to false
    fill_y = 540 #the y coordinate of where the liquid is

    while fill: #while it's running
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #allows user to quit program
                pygame.quit()
                sys.exit()
                break
            if event.type == pygame.KEYDOWN: #if a key has been pressed down
                if event.key == pygame.K_SPACE: #if its the space bar
                    spacebar_down = True  # spacebar is pressed
            if event.type == pygame.KEYUP: #if a key has been released
                if event.key == pygame.K_SPACE: #if it's the spacebar
                    spacebar_down = False  # spacebar is no longer being pressed

        #displaying image and boxes 
        WIN.blit(main1Bg_image, bgPosition) 
        fillBg_box.drawBox()
        fill_box.drawBox()
        fill_line.drawBox()

        if spacebar_down == True and fill_height < 500: 
            #if the spacebar is being pressed and the liquid is below the max height
            fill_y = fill_box.changeY(fill_y - 1) #increase the fill by 1
            fill_height = fill_box.changeHeight(1)
        if fill_height > 450: #if it goes over the red line
            print("Too much!") #it's too much

        
        pygame.display.update()
        
def mixing(mixing, WIN, main1Bg_image, bgPosition, image, image_x, image_y):

    orientation = "right" #the orientation of the bowl is initially set to the right
    time_down = 0.0 #used to measure the amount of time between the bowl being flipped
    time_elapsed = 0.0 #records the total time
    count = 0 #records how often they went too fast
    rate = pygame.time.Clock() #used to time

    #loading image
    mixingBowlSpilled_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','mixingbowl_spilled.png'))

    while mixing: #while it is running

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break
            if event.type == pygame.KEYDOWN: #detects whether a key has been pressed down
                if event.key == pygame.K_LEFT or event.key == pygame.K_a: #if it is the left arrow or a
                    orientation = "left" #orientation switched to left
                    time_down = pygame.time.get_ticks() #the time is recorded
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d: #if right arrow or d pressed
                    orientation = "right" #orientation switched to right
                    time_elapsed = (pygame.time.get_ticks() - time_down) / 1000.0 
                    #timer ends and total time calculated

        if count >= 5: #if they went too fast 5 times
            WIN.blit(main1Bg_image, bgPosition) 
            WIN.blit(mixingBowlSpilled_image, (image_x, image_y)) #th mixture is spilled so display new image
            mixing = False #set to false
            pygame.display.update() #update screen

        if count < 5: #as long as the mixture hasn;t spilled
        
            WIN.blit(main1Bg_image, bgPosition) #background image displayed
            if orientation == "right" and count < 5: #if the bowl is flipped to the right
                WIN.blit(image, (image_x, image_y)) #it is normal so display as normal
            elif orientation == "left" and count < 5: #if it's to the left
                image2 = pygame.transform.flip(image, True, False) #it needs to be flipped horizontally
                WIN.blit(image2, (image_x, image_y)) #it is drawn
            if 0 < time_elapsed < 0.30: #if the tipe between pressing the keys is less than 0.3 seconds
                print("Too fast!") #it is considered to be too fast
                time_down = 0.0 #time reset
                time_elapsed = 0.0
                count = count + 1 #count is incremented to represet the no. of times they went too fast

        rate.tick()

        pygame.display.update()
        
def seasoning(seasoning, WIN, main1Bg_image, bgPosition, image, image_x, image_y, seasoning_type):
    
    #variables that are needed
    shaker_width = 100 
    shaker_height = 100
    image_width = 200
    image_height = 200
    seasoning_width = 25
    seasoning_height = 25
    mouse_y_position = []
    shaking = False
    seasoning_amount = []
    seasoning_position_x = []
    seasoning_position_y = []

    #loading and transforming images
    shaker_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','seasoning_shaker.png'))
    shaker_image = pygame.transform.scale(shaker_image, (shaker_width, shaker_height))
    shaker_image = pygame.transform.flip(shaker_image, False, True)
    image = pygame.transform.scale(image, (image_width, image_height))
    if seasoning_type == "salt": #the seasoning will depend on the recipe
        seasoning_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','salt.png'))
    else:
        seasoning_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','herbs.png'))
    seasoning_image = pygame.transform.scale(seasoning_image, (seasoning_width, seasoning_height))


    while seasoning: #while running

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break
        
        mouse_x, mouse_y = pygame.mouse.get_pos() #get the x and y coordinate of the position of the mouse
        mouse_y_position.append(mouse_y) #put the y coordinate into the array
        WIN.blit(main1Bg_image, bgPosition) #display image
        WIN.blit(image, (image_x, image_y)) #display seasoning shaker
        if len(mouse_y_position) == 2: #when there are two values stored in the array
            if mouse_y_position[0] >= mouse_y_position[1] + 10: 
                #compare them to each other and if they are a distance of 10 apart
                shaking = True #this means the user is trying to shake out the seasoning
            mouse_y_position = [] #set the array to have no values again
            
        if len(seasoning_amount) != 0: #as long as the amount of seasoning is more than 0
            for i in range(len(seasoning_amount)-1): #go through the array
                x = random.randint(image_x + 20, image_x + image_width - 40) 
                #randomly generate the x and y coordinate, but it must stay within the boundary of
                #the ingredient that is being seasoned
                y = random.randint(image_y + 20, image_y + image_height - 40)
                seasoning_position_x.append(x) #add the coordinates to the list
                seasoning_position_y.append(y)
                WIN.blit(seasoning_image, (seasoning_position_x[i], seasoning_position_y[i])) 
                #display the seasoning at those positions
        
        if shaking == True and image_x <= mouse_x <= image_x + image_width:
            #if it has been considered that the user is shaking the seasoning out and it is within the 
            #boundary of the object to be seasoned
            seasoning_amount.append(True) 
            #append true so we know how many times the ingredient has been seasoned
            shaking = False #set to false
        
        if len(seasoning_amount) == 35: #if they have seasoned 35 times
            seasoning = False #set to false so it stoped running
        
        WIN.blit(shaker_image, (mouse_x - 50, mouse_y - 50)) 
        #display the seasoning shaker next to the mouse so it moves as the mouse moves

        pygame.display.update()
 
treeTraversal()


    







