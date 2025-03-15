# Imports
import sys
import pygame
import random
import os
from collections import deque
import classes
import globalvariables

#variables
bgPosition = (0,0)

#loading images
gameBg_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','game1_background.png'))
clock_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','clock.png'))
clock_image = pygame.transform.scale(clock_image, (100, 100))
mixingBowl_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','mixingbowl.png'))
mixingBowl_image = pygame.transform.scale(mixingBowl_image, (300, 300))
mixingBowlSpilled_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','mixingbowl_spilled.png'))
pointingHand_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','pointinghand.png'))
cuttingBoard_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','cuttingboard.png'))
cuttingBoard_image = pygame.transform.scale(cuttingBoard_image, (600, 350))
fryingPan_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','fryingpan.png'))
fryingPanOil_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','fryingpan_oil.png'))
arrow_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','arrow.png'))
arrow_image = pygame.transform.scale(arrow_image, (200, 200))
arrow2_image = pygame.transform.rotate(arrow_image, (270))
arrow3_image = pygame.transform.rotate(arrow_image, (180))
offbutton_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','offbutton.png'))
shaker_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','seasoning_shaker.png'))
shaker_image = pygame.transform.scale(shaker_image, (100, 100))

#burger images
rawPatty_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','burgerpatty.png'))
beefMince_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','beefmince.png'))
beefMince_image = pygame.transform.scale(beefMince_image, (300, 200))
burgerPatty_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','burgerpatty.png'))
burgerPatty_image = pygame.transform.scale(burgerPatty_image, (200, 200))
cookedPatty_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','cookedPatty.png'))
cookedPatty_image = pygame.transform.scale(cookedPatty_image, (200, 200))
cooker_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','cooker.png'))
cooker_image = pygame.transform.scale(cooker_image, (600, 500))
oilBottle_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','oilBottle.png'))
oilBottle_image = pygame.transform.scale(oilBottle_image, (100, 100))
egg1_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','egg.1.png'))
egg1_image = pygame.transform.scale(egg1_image, (70, 100))

onioncut1_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','onioncut1.png'))
onioncut1_image = pygame.transform.scale(onioncut1_image, (300, 300))
onioncut2_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','onioncut2.png'))
onioncut2_image = pygame.transform.scale(onioncut2_image, (300, 300))
onioncut2_1_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','onioncut2.1.png'))
onioncut2_1_image = pygame.transform.scale(onioncut2_1_image, (300, 300))
onioncut3_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','onioncut3.png'))
onioncut3_image = pygame.transform.scale(onioncut3_image, (300, 300))
onioncut4_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','onioncut4.png'))
onioncut4_image = pygame.transform.scale(onioncut4_image, (300, 300))
onioncut4_1_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','onioncut4.1.png'))
onioncut4_2_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','onioncut4.2.png'))
onioncut4_3_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','onioncut4.3.png'))
onioncut4_4_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','onioncut4.4.png'))
onioncut4_5_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','onioncut4.5.png'))
onioncut4_6_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','onioncut4.6.png'))
onioncut4_7_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','onioncut4.7.png'))
onioncut4_8_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','onioncut4.8.png'))
onioncut4_9_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','onioncut4.9.png'))
dicedonion_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','dicedonion.png'))


onions = [ onioncut1_image, onioncut2_image, onioncut2_1_image, onioncut3_image, onioncut4_image, 
          onioncut4_1_image, onioncut4_2_image, onioncut4_3_image, onioncut4_4_image, onioncut4_5_image, 
          onioncut4_6_image, onioncut4_7_image, onioncut4_8_image, onioncut4_9_image, dicedonion_image]

for i in range(len(onions)):
    onions[i] = pygame.transform.scale(onions[i], (300,300))

#cake images
bakingpowder_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','bakingpowder.png'))
bakingpowder_image = pygame.transform.scale(bakingpowder_image, (150, 150))
bakingsoda_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','bakingsoda.png'))
bakingsoda_image = pygame.transform.scale(bakingsoda_image, (150, 150))
sugar_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','sugar.png'))
sugar_image = pygame.transform.scale(sugar_image, (150, 150))
yogurt_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','yogurt.png'))
yogurt_image = pygame.transform.scale(yogurt_image, (150, 150))
milk_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','milk.png'))
milk_image = pygame.transform.scale(milk_image, (150, 150))
vanilla_extract_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','vanilla_extract.png'))
vanilla_extract_image = pygame.transform.scale(vanilla_extract_image, (50, 150))
flour_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','flour.png'))
flour_image = pygame.transform.scale(flour_image, (150, 150))
cake_flour_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','cakeflour.png'))
cake_flour_image = pygame.transform.scale(cake_flour_image, (150, 150))
butter_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','butter.png'))
butter_image = pygame.transform.scale(butter_image, (150, 150))
caketin_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','caketin.png'))
caketin_image = pygame.transform.scale(caketin_image, (300, 150))
caketin_filled_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','caketin_filled.png'))
caketin_filled_image = pygame.transform.scale(caketin_filled_image, (300, 150))
oven_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','oven.png'))
oven_image = pygame.transform.scale(oven_image, (400, 400))
assembledcake_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','assembledcake.png'))
assembledcake_image = pygame.transform.scale(assembledcake_image, (400, 400))
frostedcake_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','frostedcake.png'))
frostedcake_image = pygame.transform.scale(frostedcake_image, (400, 400))

#sushi images

rice_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','rice.png'))
rice_image = pygame.transform.scale(rice_image, (150, 150))
sushiseasoning_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','sushiseasoning.png'))
sushiseasoning_image = pygame.transform.scale(sushiseasoning_image, (150, 150))
ricecooker_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','ricecooker.png'))
ricecooker_image = pygame.transform.scale(ricecooker_image, (400, 400))

cucumber1_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','cucumber1.png'))
cucumber2_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','cucumber2.png'))
cucumber3_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','cucumber3.png'))
cucumber4_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','cucumber4.png'))
cucumber5_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','cucumber5.png'))
cucumbers = [cucumber1_image, cucumber2_image, cucumber3_image, cucumber4_image, cucumber5_image]

for i in range(len(cucumbers)):
    cucumbers[i] = pygame.transform.scale(cucumbers[i], (450,300))

avocado1_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','avocado1.png'))
avocado2_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','avocado2.png'))
avocado3_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','avocado3.png'))
avocado4_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','avocado4.png'))
avocado5_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','avocado5.png'))
avocado6_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','avocado6.png'))
avocado7_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','avocado7.png'))
avocados = [avocado1_image, avocado2_image, avocado3_image, avocado4_image, avocado5_image, avocado6_image, 
            avocado7_image, ]

for i in range(len(avocados)):
    avocados[i] = pygame.transform.scale(avocados[i], (300,300))

salmon1_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','salmon.png'))
salmon2_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','salmon2.png'))
salmon3_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','salmon3.png'))

seaweed1_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','seaweed.png'))
seaweed2_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','seaweed2.png'))
seaweed3_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','seaweed3.png'))
seaweed4_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','seaweed4.png'))
seaweed5_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','seaweed5.png'))
seaweed6_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','seaweed6.png'))
seaweed7_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','seaweed7.png'))
seaweed8_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','seaweed8.png'))
seaweed9_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','seaweed9.png'))
seaweed10_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','seaweed10.png'))
seaweed11_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','seaweed11.png'))
seaweeds = [seaweed1_image, seaweed2_image, seaweed3_image, seaweed4_image, seaweed5_image, 
            seaweed6_image, seaweed7_image, seaweed8_image, seaweed9_image, seaweed10_image, seaweed11_image]

for i in range(len(seaweeds)):
    seaweeds[i] = pygame.transform.scale(seaweeds[i], (300,300))

sushiroll1_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','sushiroll.png'))
sushiroll2_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','sushiroll2.png'))
sushiroll3_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','sushiroll3.png'))
sushiroll4_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','sushiroll4.png'))
sushiroll5_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','sushiroll5.png'))
sushiroll6_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','sushiroll6.png'))
sushiroll7_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','sushiroll7.png'))
sushirolls = [sushiroll1_image, sushiroll2_image, sushiroll3_image, sushiroll4_image, sushiroll5_image, 
              sushiroll6_image, sushiroll7_image]

for i in range(len(sushirolls)):
    sushirolls[i] = pygame.transform.scale(sushirolls[i], (300,300))

bowl_width = 300
bowl_height = 300
oven_width = 400
oven_height = 400
ricecooker_width = 400
ricecooker_height = 400

#colours
cakebatter_colour = pygame.Color(248, 226, 159)
water_colour = pygame.Color(115, 203, 251)
fillBg_colour = pygame.Color(61, 61, 61)


class RecipeTree:

    def __init__(self, value):
        self.value = value #this will be the value stored in the node
        self.children = [] #this will hold all the children to the root node
    
    def add_child(self, child_node): 
        self.children.append(child_node) #this allows me to add child nodes
    
    def preorder(root, stack, visitedNodes):
 
        if len(visitedNodes) == 0 and len(stack) == 0:
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
                    all_children_visited = False #then all the children haven't been visited)
                    return (parent.children[i].value) #stops at each node
    
            if all_children_visited == True: #if all the children of the parent have been visited
                stack.pop() #remove the parent from the stack 
        #print(visitedNodes)
        
def treeTraversal(recipeChosen, stack, visitedNodes): 

    burgerRoot = RecipeTree("Burger") #the root of the tree will have "Burger"
    burgerRoot.children = [RecipeTree("Frying"), RecipeTree("Mixing"), RecipeTree("Shaping"), RecipeTree("Grilling"), RecipeTree("Assembly")]
    #these are the children directly under the root node
    burgerRoot.children[0].children = [RecipeTree("Frying 1"), RecipeTree("Frying 2"), RecipeTree("Frying 3"), RecipeTree("Frying 4")]
    #these are the children of the first node ("Frying")
    burgerRoot.children[1].children = [RecipeTree("Mixing 1"), RecipeTree("Mixing 2"), RecipeTree("Mixing 3"), RecipeTree("Mixing 4")]
    burgerRoot.children[2].children = [RecipeTree("Shaping 1")]
    burgerRoot.children[3].children = [RecipeTree("Grilling 1")]
    burgerRoot.children[4].children = [RecipeTree("Assembly 1")]

    cakeRoot = RecipeTree("Cake")
    cakeRoot.children = [RecipeTree("Mixing"), RecipeTree("Baking"), RecipeTree("Frosting"), RecipeTree("Decoration")]
    cakeRoot.children[0].children = [RecipeTree("Mixing 1")]
    cakeRoot.children[1].children = [RecipeTree("Baking 1"), RecipeTree("Baking 2")]
    cakeRoot.children[2].children = [RecipeTree("Frosting 1")]
    cakeRoot.children[3].children = [RecipeTree("Decoration 1"), RecipeTree("Decoration 2"), RecipeTree("Decoration 3")]

    sushiRoot = RecipeTree("Sushi")
    sushiRoot.children = [RecipeTree("Cooking"), RecipeTree("Assembly"), RecipeTree("Cutting")]
    sushiRoot.children[0].children = [RecipeTree("Cooking 1"), RecipeTree("Cooking 2"), RecipeTree("Cooking 3")]
    sushiRoot.children[1].children = [RecipeTree("Assembly 1"), RecipeTree("Assembly 2"), RecipeTree("Assembly 3"), RecipeTree("Assembly 4"), RecipeTree("Assembly 5"),]
    sushiRoot.children[2].children = [RecipeTree("Cutting 1")]
    
    if recipeChosen == "burger": #determines which tree is being traversed
        value = burgerRoot.preorder(stack, visitedNodes)
    elif recipeChosen == "cake":
        value = cakeRoot.preorder(stack, visitedNodes)
    elif recipeChosen == "sushi":
        value = sushiRoot.preorder(stack, visitedNodes)
    
    return value, stack, visitedNodes

def draw(draw, x1, y1, x2, y2, x3, y3, x4, y4, game_ticks, timer_text, timer_box):

    flag1 = False #these flags represent whether the drawn circle has touched a coordinate
    flag2 = False #there are 4 points to the arrow, so four coordinates (x1, y2), (x2, y2) etc. = four flags
    flag3 = False 
    flag4 = False
    # the colour and size of the brush
    drawColour = [0, 0, 255]
    brushSize = 5
    canvasSize = [800, 800]

    # Canvas
    canvas = pygame.Surface((canvasSize),pygame.SRCALPHA)
    canvas.set_alpha(200) 
    #makes the canvas transparent so that it doesn't cover the background image

    other_ticks = pygame.time.get_ticks() 

    while draw: #ensures that the user only draws when they havent drawn the arrow
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break
        
        timer_box.drawBox()
        timer_text.changeText(str(((pygame.time.get_ticks() - other_ticks) + game_ticks) / 1000))

        # Draw the Canvas at the center of the screen
        x, y = globalvariables.WIN.get_size() 
        globalvariables.WIN.blit(canvas, [x/2 - canvasSize[0]/2, y/2 - canvasSize[1]/2])
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

            print(dx, dy)

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
    
    return other_ticks
      
def recipeAssembly(assembly, recipeChosen, colours):

    hand_width = 150
    hand_height = 150
    hand_x = globalvariables.window_x // 2 - hand_width
    hand_y = globalvariables.window_y - hand_height - 20
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

    cakeLayer1_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','cakelayer1.png'))
    cakeLayer2_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','cakelayer2.png'))
    cakeLayer3_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','cakelayer3.png'))
    
    #transforming images
    hand_image = pygame.transform.scale(hand_image, (hand_width, hand_height))

    topBun_image = pygame.transform.scale(topBun_image, (component_width, component_height))
    bottomBun_image = pygame.transform.scale(bottomBun_image, (component_width, component_height))
    cheeseLayer_image = pygame.transform.scale(cheeseLayer_image, (component_width, component_height))
    lettuceLayer_image = pygame.transform.scale(lettuceLayer_image, (component_width, component_height))
    onionLayer_image = pygame.transform.scale(onionLayer_image, (component_width, component_height))
    meatLayer_image = pygame.transform.scale(meatLayer_image, (component_width, component_height))
    tomatoLayer_image = pygame.transform.scale(tomatoLayer_image, (component_width, component_height))

    cakeLayer1_image = pygame.transform.scale(cakeLayer1_image, (component_width, component_height))
    cakeLayer2_image = pygame.transform.scale(cakeLayer2_image, (component_width, component_height - 20))
    cakeLayer3_image = pygame.transform.scale(cakeLayer3_image, (component_width, component_height + 20))

    burgerLayer_images = [bottomBun_image, lettuceLayer_image, meatLayer_image, cheeseLayer_image, tomatoLayer_image, onionLayer_image, topBun_image]
    burgerLayer_order = []

    cakeLayer_images = [cakeLayer1_image, cakeLayer2_image, cakeLayer3_image]
    cakeLayer_order = []

    if recipeChosen == "burger":
        layer_images = burgerLayer_images
        layer_order = burgerLayer_order
    elif recipeChosen == "cake":
        layer_images = cakeLayer_images
        layer_order = cakeLayer_order

    component_x = random.randint(0, globalvariables.window_x - component_width)
    component_y = 0
    
    clock = pygame.time.Clock()

    back_button = classes.Button(770, 500, 70, 100, colours[3], False)
    back_button.setUnactive()
    back_text = classes.Text(785, 503, "-->", (255, 255, 255), 50)

    while assembly == True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                backPressed = back_button.checkPressed(pygame.mouse.get_pos())
                backActive = back_button.getActive()
                if backPressed == True and backActive == False:
                    assembly = False
                    back_button.setActive()

        if count != (len(layer_images) + 1):

            keys = pygame.key.get_pressed()
            clock.tick(60)

            globalvariables.WIN.blit(gameBg_image, bgPosition)

            if count != (len(layer_images)):
                component_rect = globalvariables.WIN.blit(layer_images[count], (component_x, component_y))
                #a rect is created for the component and hand that will be used to detect a collision between them
            
            hand_rect = globalvariables.WIN.blit(hand_image, (hand_x, hand_y))
            

            if len(layer_order) != 0: #checks that at least one component has been caught
                layer_x = hand_x
                for i in range(len(layer_order)): #goes through array
                    globalvariables.WIN.blit(layer_order[i], (layer_x, hand_y - (10*(i+1)))) 
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
            elif hand_x >= (globalvariables.window_x - hand_width):
                hand_x = (globalvariables.window_x - hand_width)
            
            component_y += component_speed

            if count == (len(layer_images)): #if all layers have been displayed
                count = count + 1
            else:
                if component_y > globalvariables.window_y: #if component falls off the screen
                    component_x = random.randint(0, globalvariables.window_x - component_width) #new x coordinate is generated
                    component_y = 0
                elif hand_rect.colliderect(component_rect): #if the component and hand collide..
                    layer_order.append(layer_images[count]) #adds the correct layer to the array
                    component_x = random.randint(0, globalvariables.window_x - component_width) #generates new x coordinate
                    component_y = 0
                    if count != (len(layer_images)):
                        count = count + 1 #increments count to show that the next layer should be displayed
        else:
            back_button.drawBox()
            back_text.drawText()

        pygame.display.update()
    

    return assembly

def flip(flip, bar_x, bar_y, images, coordinates):
    
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
    fillArrow_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','fillArrow.png'))

    #transforming images
    temperatureBar_image = pygame.transform.scale(temperatureBar_image, (bar_width, bar_height))
    fillArrow_image = pygame.transform.scale(fillArrow_image, (arrow_width, arrow_height))

    while flip: #while it is running

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break
        
        #displaying the images on the screen
        globalvariables.WIN.blit(gameBg_image, bgPosition)
        for i in range(len(images)):
            globalvariables.WIN.blit(images[i], coordinates[i])
        globalvariables.WIN.blit(temperatureBar_image, (bar_x, bar_y))
        globalvariables.WIN.blit(fillArrow_image, (arrow_x, arrow_y))

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
            globalvariables.WIN.blit(fillArrow_image, (arrow_x, arrow_y)) #stop the arrow at that position
            flip = False #no longer running


        pygame.display.update()

def fill(fill, fill_colour, colours):
    
    fillBg_box = classes.Box(300, 50, 500, 400, fillBg_colour, False)
    fill_box = classes.Box(302, 540, 10, 396, fill_colour, True)
    fill_line = classes.Box(300, 100, 10, 400, (214, 135, 140), False) 
    #the colour will change depending on the recipe as sushi uses water while cake will use cake batter
    fill_height = 0 #the initial height of the liquid is 0
    spacebar_down = False #the spacebar being pressed is initially set to false
    fill_y = 540 #the y coordinate of where the liquid is

    back_button = classes.Button(770, 500, 70, 100, colours[3], False)
    back_button.setUnactive()
    back_text = classes.Text(785, 503, "-->", (255, 255, 255), 50)

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
            if event.type == pygame.MOUSEBUTTONDOWN:
                backPressed = back_button.checkPressed(pygame.mouse.get_pos())
                backActive = back_button.getActive()
                if backPressed == True and backActive == False:
                    fill = False
                    back_button.setActive()

        #displaying image and boxes 
        globalvariables.WIN.blit(gameBg_image, bgPosition) 
        fillBg_box.drawBox()
        fill_box.drawBox()
        fill_line.drawBox()
        back_button.drawBox()
        back_text.drawText()

        if spacebar_down == True and fill_height < 500: 
            #if the spacebar is being pressed and the liquid is below the max height
            fill_y = fill_box.changeY(fill_y - 1) #increase the fill by 1
            fill_height = fill_box.changeHeight(1)
        if fill_height > 450: #if it goes over the red line
            print("Too much!") #it's too much


        
        pygame.display.update()
        
def mixingBowl(mixing, image, image_x, image_y, image_width, image_height):

    orientation = "right" #the orientation of the bowl is initially set to the right
    time_down = 0.0 #used to measure the amount of time between the bowl being flipped
    time_elapsed = 0.0 #records the total time
    count = 0 #records how often they went too fast
    mix = 0 #how many times they mixed successfully
    rate = pygame.time.Clock() #used to time

    #loading image
    mixingBowlSpilled_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','mixingbowl_spilled.png'))
    mixingBowlSpilled_image = pygame.transform.scale(mixingBowlSpilled_image, (image_width, image_height))

    while mixing: #while it is running

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break
            if event.type == pygame.KEYDOWN: #detects whether a key has been pressed down
                if event.key == pygame.K_LEFT or event.key == pygame.K_a: #if it is the left arrow or a
                    orientation = "left" #orientation switched to left
                    mix = mix + 1
                    time_down = pygame.time.get_ticks() #the time is recorded
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d: #if right arrow or d pressed
                    orientation = "right" #orientation switched to right
                    time_elapsed = (pygame.time.get_ticks() - time_down) / 1000.0 
                    #timer ends and total time calculated

        if count >= 5: #if they went too fast 5 times
            globalvariables.WIN.blit(gameBg_image, bgPosition) 
            globalvariables.WIN.blit(mixingBowlSpilled_image, (image_x, image_y)) #th mixture is spilled so display new image
            mixing = False #set to false
            pygame.display.update() #update screen
        elif mix == 7:
            mixing = False #set to false

        if count < 5: #as long as the mixture hasn;t spilled
        
            globalvariables.WIN.blit(gameBg_image, bgPosition) #background image displayed
            if orientation == "right" and count < 5: #if the bowl is flipped to the right
                globalvariables.WIN.blit(image, (image_x, image_y)) #it is normal so display as normal
            elif orientation == "left" and count < 5: #if it's to the left
                image2 = pygame.transform.flip(image, True, False) #it needs to be flipped horizontally
                globalvariables.WIN.blit(image2, (image_x, image_y)) #it is drawn
            if 0 < time_elapsed < 0.30: #if the tipe between pressing the keys is less than 0.3 seconds
                print("Too fast!") #it is considered to be too fast
                time_down = 0.0 #time reset
                time_elapsed = 0.0
                count = count + 1 #count is incremented to represet the no. of times they went too fast

        rate.tick()

        pygame.display.update()
        
def seasoning(seasoning, image, image_x, image_y, image_width, image_height, seasoning_type):
    
    #variables that are needed
    #image_width = 200
    #image_height = 200
    seasoning_width = 25
    seasoning_height = 25
    mouse_y_position = []
    shaking = False
    seasoning_amount = []
    seasoning_position_x = []
    seasoning_position_y = []

    #loading and transforming images
    shaker_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','seasoning_shaker.png'))
    shaker_image = pygame.transform.scale(shaker_image, (100, 100))
    shaker_image = pygame.transform.flip(shaker_image, False, True)
    image = pygame.transform.scale(image, (image_width, image_height))
    if seasoning_type == "sprinkles": #the seasoning will depend on the recipe
        seasoning_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','sprinkles.png'))
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
        globalvariables.WIN.blit(gameBg_image, bgPosition) #display image
        globalvariables.WIN.blit(image, (image_x, image_y)) #display seasoning shaker
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
                globalvariables.WIN.blit(seasoning_image, (seasoning_position_x[i], seasoning_position_y[i])) 
                #display the seasoning at those positions
        
        if shaking == True and image_x <= mouse_x <= image_x + image_width:
            #if it has been considered that the user is shaking the seasoning out and it is within the 
            #boundary of the object to be seasoned
            seasoning_amount.append(True) 
            #append true so we know how many times the ingredient has been seasoned
            shaking = False #set to false
        
        if len(seasoning_amount) == 35: #if they have seasoned 35 times
            seasoning = False #set to false so it stoped running
        
        globalvariables.WIN.blit(shaker_image, (mouse_x - 50, mouse_y - 50)) 
        #display the seasoning shaker next to the mouse so it moves as the mouse moves

        pygame.display.update()
 
def drag(bowl_x, bowl_y, bowl_width, bowl_height, showIngredient, active_ingredient, ingredient_rect, draggedImage):

    for event in pygame.event.get(): #allows user to quit the window
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            break
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if ingredient_rect.collidepoint(event.pos):
                    active_ingredient = True
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                active_ingredient = False
        if event.type == pygame.MOUSEMOTION:
            if active_ingredient:
                ingredient_rect.move_ip(event.rel)
    
    if showIngredient:
        globalvariables.WIN.blit(draggedImage, ingredient_rect)

def burgerGame(value, stack, visitedNodes, score, colours):

    #the steps are initially set to false
    frying = False
    mixing = False
    shaping = False
    grilling = False
    assembly = False

    if value == "Frying": 
        #they are set to true based on what is stored in value, this will run the correct step
        frying = True
        value, stack, visitedNodes = treeTraversal("burger", stack, visitedNodes)
    elif value == "Mixing":
        mixing = True
        value, stack, visitedNodes = treeTraversal("burger", stack, visitedNodes)
    elif value == "Shaping":
        shaping = True
        value, stack, visitedNodes = treeTraversal("burger", stack, visitedNodes)
    elif value == "Grilling":
        grilling = True
        value, stack, visitedNodes = treeTraversal("burger", stack, visitedNodes)
    elif value == "Assembly":
        assembly = True
        value, stack, visitedNodes = treeTraversal("burger", stack, visitedNodes)

    #variables
    game_ticks = pygame.time.get_ticks()
    clock = pygame.time.Clock()
    other_ticks = 0
    cut = 0
    fry = 0
    mix = 0

    #text object
    timer_text = classes.Text(52, 12, "00.00", (255, 255, 255), 24)
    timer_box = classes.Box(50, 10, 50, 50, colours[5], False)

    #button objects
    onioncut2_1_button = classes.ImageButton(340, 210, onions[2], 1)
    onioncut3_button = classes.ImageButton(340, 210, onions[3], 1)
    onioncut4_9_button = classes.ImageButton(340, 210, onions[13], 1)
    dicedonion_button = classes.ImageButton(340, 210, onions[14], 1)
    oilBottle_button = classes.ImageButton(720, 280, oilBottle_image, 2.5)
    offbutton_button = classes.ImageButton(720, 280, offbutton_image, 1)
    burgerPatty_button = classes.ImageButton(150, 350, burgerPatty_image, 1)
    cookedPatty_button = classes.ImageButton(250, 300, cookedPatty_image, 1)

    active_ingredient = False
    mince_rect = beefMince_image.get_rect()
    mince_rect.center = (150, 450)
    egg_rect = egg1_image.get_rect()
    egg_rect.center = (100, 400)
    rects = [mince_rect, egg_rect]

    while frying:
        for event in pygame.event.get(): #allows user to quit the window
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                onioncut2_1Pressed = onioncut2_1_button.checkPressed(pygame.mouse.get_pos())
                if onioncut2_1Pressed and cut == 2:
                    cut = cut + 1
                onioncut3Pressed = onioncut3_button.checkPressed(pygame.mouse.get_pos())
                if onioncut3Pressed and cut == 3:
                    cut = cut + 1
                onioncut4_9Pressed = onioncut4_9_button.checkPressed(pygame.mouse.get_pos())
                onioncut4_9Active = onioncut4_9_button.getActive()
                if onioncut4_9Pressed and cut == 13 and onioncut4_9Active == False:
                    cut = cut + 1
                    onioncut4_9_button.setActive()
                dicedonionPressed = dicedonion_button.checkPressed(pygame.mouse.get_pos())
                dicedonionActive = dicedonion_button.getActive()
                if dicedonionPressed == True and cut == 14 and onioncut4_9Active == True:
                    fry = fry + 1
                    value, stack, visitedNodes = treeTraversal("burger", stack, visitedNodes)
                    cut = cut + 1
                elif dicedonionPressed == True and value == "Frying 3" and dicedonionActive == False:
                    fry = fry + 1
                    start_ticks = pygame.time.get_ticks()
                    value, stack, visitedNodes = treeTraversal("burger", stack, visitedNodes)
                    dicedonion_button.setActive()
                oilBottlePressed = oilBottle_button.checkPressed(pygame.mouse.get_pos())
                oilBottleActive = oilBottle_button.getActive()
                if oilBottlePressed and oilBottleActive == False:
                    fry = fry + 1
                    value, stack, visitedNodes = treeTraversal("burger", stack, visitedNodes)
                    start_ticks = pygame.time.get_ticks()
                    oilBottle_button.setActive() 
                offbuttonPressed = offbutton_button.checkPressed(pygame.mouse.get_pos())
                if offbuttonPressed == True and value == "Frying 4":
                    frying = False
        
        globalvariables.WIN.blit(gameBg_image, bgPosition)
        globalvariables.WIN.blit(clock_image, (20, 10))
        timer_box.drawBox()
        #game_ticks = pygame.time.get_ticks()
        print((((pygame.time.get_ticks() - game_ticks) / 1000)))
        timer_text.changeText(str(((pygame.time.get_ticks() - other_ticks) + game_ticks) / 1000))

        if value == "Frying 1":
            globalvariables.WIN.blit(cuttingBoard_image, (100, 170))
            if cut == 0:
                globalvariables.WIN.blit(onions[0], (340, 210))
                globalvariables.WIN.blit(arrow2_image, (370, 215))
                other_ticks = draw(True, 282.0, 412.0, 436.0, 377.0, 465.0, 412.0, 435.0, 459.0, 0, timer_text, timer_box)
                cut = cut + 1
            elif cut == 1:
                globalvariables.WIN.blit(onions[1], (340, 210))
                globalvariables.WIN.blit(arrow3_image, (390, 295))
                other_ticks = draw(True, 349.0, 562.0, 392.0, 587.0, 431.0, 561.0, 387.0, 407.0, game_ticks, timer_text, timer_box)
                cut = cut + 1
            elif cut == 2:
                onioncut2_1_button.draw()
            elif cut == 3:
                onioncut3_button.draw()
            elif cut == 4:
                globalvariables.WIN.blit(onions[4], (340, 210))
                globalvariables.WIN.blit(pygame.transform.scale(arrow3_image, (200, 300)), (305, 215))
                other_ticks = draw(True, 263.0, 565.0, 307.0, 608.0, 350.0, 565.0, 303.0, 332.0, game_ticks + other_ticks, timer_text, timer_box)
                cut = cut + 1
            elif cut == 5:
                globalvariables.WIN.blit(onions[5], (340, 210))
                globalvariables.WIN.blit(pygame.transform.scale(arrow3_image, (200, 300)), (345, 215))
                other_ticks = draw(True, 344.0, 610.0, 305.0, 567.0, 384.0, 564.0, 344.0, 333.0, game_ticks + other_ticks, timer_text, timer_box)
                cut = cut + 1
            elif cut == 6:
                globalvariables.WIN.blit(onions[6], (340, 210))
                globalvariables.WIN.blit(pygame.transform.scale(arrow3_image, (200, 300)), (390, 215))
                other_ticks = draw(True, 352.0, 567.0, 387.0, 609.0, 433.0, 561.0, 387.0, 335.0, game_ticks + other_ticks, timer_text, timer_box)
                cut = cut + 1
            elif cut == 7:
                globalvariables.WIN.blit(onions[7], (340, 210))
                globalvariables.WIN.blit(pygame.transform.scale(arrow3_image, (200, 300)), (420, 215))
                other_ticks = draw(True, 418.0, 334.0, 375.0, 561.0, 423.0, 611.0, 469.0, 561.0, game_ticks + other_ticks, timer_text, timer_box)
                cut = cut + 1
            elif cut == 8:
                globalvariables.WIN.blit(onions[8], (340, 210))
                globalvariables.WIN.blit(pygame.transform.scale(arrow3_image, (200, 300)), (460, 215))
                other_ticks = draw(True, 419.0, 565.0, 460.0, 607.0, 507.0, 561.0, 455.0, 330.0, game_ticks  + other_ticks, timer_text, timer_box)
                cut = cut + 1
            elif cut == 9:
                globalvariables.WIN.blit(onions[9], (340, 210))
                globalvariables.WIN.blit(pygame.transform.scale(arrow3_image, (200, 300)), (433, 215))
                other_ticks = draw(True, 394.0, 565.0, 434.0, 605.0, 478.0, 561.0, 430.0, 334.0, game_ticks  + other_ticks, timer_text, timer_box)
                cut = cut + 1
            elif cut == 10:
                globalvariables.WIN.blit(onions[10], (340, 210))
                globalvariables.WIN.blit(pygame.transform.scale(arrow2_image, (310, 200)), (330, 315))
                other_ticks = draw(True, 487.0, 555.0, 492.0, 472.0, 533.0, 516.0, 240.0, 517.0, game_ticks  + other_ticks, timer_text, timer_box)
                cut = cut + 1
            elif cut == 11:
                globalvariables.WIN.blit(onions[11], (340, 210))
                globalvariables.WIN.blit(pygame.transform.scale(arrow2_image, (310, 200)), (330, 270))
                other_ticks = draw(True, 248.0, 473.0, 489.0, 511.0, 485.0, 429.0, 531.0, 470.0, game_ticks  + other_ticks, timer_text, timer_box)
                cut = cut + 1
            elif cut == 12:
                globalvariables.WIN.blit(onions[12], (340, 210))
                globalvariables.WIN.blit(pygame.transform.scale(arrow2_image, (310, 200)), (330, 215))
                other_ticks = draw(True, 489.0, 451.0, 245.0, 413.0, 480.0, 372.0, 529.0, 417.0, game_ticks  + other_ticks, timer_text, timer_box)
                cut = cut + 1
            elif cut == 13:
                onioncut4_9_button.draw()
            elif cut == 14:
                dicedonion_button.draw()
        
        if value == "Frying 2":
            globalvariables.WIN.blit(cooker_image, (180, 190))
            if fry == 1:
                globalvariables.WIN.blit(fryingPan_image, (-50, 60))
                oilBottle_button.draw()
            elif fry == 2:
                globalvariables.WIN.blit(fryingPanOil_image, (-50, 60))
        
        if value == "Frying 3":
            globalvariables.WIN.blit(cooker_image, (180, 190))
            globalvariables.WIN.blit(fryingPanOil_image, (-50, 60))
            if fry == 2:
                seconds = ((pygame.time.get_ticks() - start_ticks) / 1000)
                if seconds > 7.0:
                    dicedonion_button.changePosition(720, 280)
                    print(value)
            if fry == 3:
                dicedonion_button.changePosition(150, 160)
        
        if value == "Frying 4":
            globalvariables.WIN.blit(cooker_image, (180, 190))
            globalvariables.WIN.blit(fryingPanOil_image, (-50, 60))
            dicedonion_button.changePosition(250, 300)
            if fry == 3:
                seconds = ((pygame.time.get_ticks() - start_ticks) / 1000)
                if seconds > 10.0:
                    offbutton_button.draw()
        
        clock.tick(globalvariables.FPS)

        pygame.display.update()
    
    while mixing:
        for event in pygame.event.get(): #allows user to quit the window
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if rects[mix].collidepoint(event.pos):
                        active_ingredient = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    active_ingredient = False
            if event.type == pygame.MOUSEMOTION:
                if active_ingredient:
                    rects[mix].move_ip(event.rel)
        
        globalvariables.WIN.blit(gameBg_image, bgPosition)
        if value == "Mixing 1":
            seasoning(True, beefMince_image, 300, 365, 300, 200, "herbs")
            value, stack, visitedNodes = treeTraversal("burger", stack, visitedNodes)
        if value == "Mixing 2" or value == "Mixing 3" or value == "Mixing 4":
            globalvariables.WIN.blit(mixingBowl_image, (575, 265))
        if value == "Mixing 2" or value == "Mixing 3":
            if active_ingredient:
                mx, my = pygame.mouse.get_pos()
                if 575 <= mx - 120 <= (575 + bowl_width) and 265 + 20 <= my - 120 <= (265 + bowl_height):
                    if value == "Mixing 2":
                        value, stack, visitedNodes = treeTraversal("burger", stack, visitedNodes)
                        mix = mix + 1
                    else:
                        value, stack, visitedNodes = treeTraversal("burger", stack, visitedNodes)
                    print(value)

                    active_ingredient = False
        if value == "Mixing 2":
            globalvariables.WIN.blit(beefMince_image, mince_rect)
        if value == "Mixing 3":
            globalvariables.WIN.blit(egg1_image, egg_rect)
        if value == "Mixing 4":
            mixingBowl(True, mixingBowl_image, 300, 265, 300, 300)
            mixing = False

        pygame.display.update()
    
    nextPatty = True 
    shaped = 0

    while shaping:

        for event in pygame.event.get(): #allows user to quit the window
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                burgerPattyPressed = burgerPatty_button.checkPressed(pygame.mouse.get_pos())
                if burgerPattyPressed:
                    nextPatty = True
                    shaped = shaped + 1
        
        globalvariables.WIN.blit(gameBg_image, bgPosition)
        if value == "Shaping 1":
            if nextPatty:
                flip(True, 400, 10, [beefMince_image], [(150, 350)])
                nextPatty = False
            if nextPatty == False:
                burgerPatty_button.draw()
            if shaped == 4:
                shaping = False
        

        pygame.display.update()

    grilled = 0
    
    while grilling:
        for event in pygame.event.get(): #allows user to quit the window
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                burgerPattyPressed = burgerPatty_button.checkPressed(pygame.mouse.get_pos())
                if burgerPattyPressed:
                    nextPatty = True
                cookedPattyPressed = cookedPatty_button.checkPressed(pygame.mouse.get_pos())
                if cookedPattyPressed:
                    nextPatty = True
                    grilled = grilled + 1
        
        globalvariables.WIN.blit(gameBg_image, bgPosition)
        if value == "Grilling 1":
            if nextPatty:
                flip(True, 700, 10, [cooker_image, fryingPan_image, burgerPatty_image], [(180, 190), (-50, 60), (250, 300)])
                nextPatty = False
            if nextPatty == False:
                globalvariables.WIN.blit(cooker_image, (180, 190))
                globalvariables.WIN.blit(fryingPan_image, (-50, 60))
                cookedPatty_button.draw()
            if grilled == 4:
                grilling = False
        

        pygame.display.update()
    
    while assembly:

        for event in pygame.event.get(): #allows user to quit the window
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break
                
        if value == "Assembly 1":
            recipeAssembly(True, "burger", colours)
            assembly = False

        pygame.display.update()

    return value, stack, visitedNodes

def cakeGame(value, stack, visitedNodes, score, colours):
    mixing = False
    baking = False
    frosting = False
    decorating = False

    if value == "Mixing":
        mixing = True
        value, stack, visitedNodes = treeTraversal("cake", stack, visitedNodes)
    elif value == "Baking":
        baking = True
        value, stack, visitedNodes = treeTraversal("cake", stack, visitedNodes)
    elif value == "Frosting":
        frosting = True
        value, stack, visitedNodes = treeTraversal("cake", stack, visitedNodes)
    elif value == "Decoration":
        decorating = True
        value, stack, visitedNodes = treeTraversal("cake", stack, visitedNodes)
    
    active_ingredient = False
    bakingpowder_rect = bakingpowder_image.get_rect()
    bakingpowder_rect.center = (250, 450)
    bakingsoda_rect = bakingsoda_image.get_rect()
    bakingsoda_rect.center = (250, 450)
    flour_rect = flour_image.get_rect()
    flour_rect.center = (250, 450)
    sugar_rect = sugar_image.get_rect()
    sugar_rect.center = (250, 450)
    cake_flour_rect = cake_flour_image.get_rect()
    cake_flour_rect.center = (250, 450)
    vanilla_extract_rect = vanilla_extract_image.get_rect()
    vanilla_extract_rect.center = (250, 450)
    milk_rect = milk_image.get_rect()
    milk_rect.center = (250, 450)
    yogurt_rect = yogurt_image.get_rect()
    yogurt_rect.center = (250, 450)
    shaker_rect = shaker_image.get_rect()
    shaker_rect.center = (250, 450)
    butter_rect = butter_image.get_rect()
    butter_rect.center = (250, 450)
    egg_rect = egg1_image.get_rect()
    egg_rect.center = (200, 500)
    
    mixing_rects = [flour_rect, cake_flour_rect, sugar_rect, shaker_rect, bakingpowder_rect, bakingsoda_rect, butter_rect, egg_rect, egg_rect, milk_rect, vanilla_extract_rect]
    
    mix = 0
    filling = 0

    caketin_button = classes.ImageButton(300, 265, caketin_image, 1)
    oven_button = classes.ImageButton(530, 200, oven_image, 1)

    timer_text = classes.Text(52, 12, "00.00", (255, 255, 255), 24)
    timer_box = classes.Box(50, 10, 50, 50, colours[5], False)

    active_ingredient = False
    caketin_filled1_rect = caketin_filled_image.get_rect()
    caketin_filled2_rect = caketin_filled_image.get_rect()
    caketin_filled1_rect.center = (270, 500)
    caketin_filled2_rect.center = (270, 500)

    oven_rects = [caketin_filled1_rect, caketin_filled2_rect]

    oven = 0
    bake = 0

    while mixing:
        for event in pygame.event.get(): #allows user to quit the window
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if mixing_rects[mix].collidepoint(event.pos):
                        active_ingredient = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    active_ingredient = False
            if event.type == pygame.MOUSEMOTION:
                if active_ingredient:
                    mixing_rects[mix].move_ip(event.rel)

        globalvariables.WIN.blit(gameBg_image, bgPosition)
        if value == "Mixing 1":
            if mix <= 11:
                globalvariables.WIN.blit(mixingBowl_image, (575, 265))
                if active_ingredient:
                    mx, my = pygame.mouse.get_pos()
                    if 575 <= mx - 120 <= (575 + bowl_width) and 265 + 20 <= my - 120 <= (265 + bowl_height):
                        mix = mix + 1
                        active_ingredient = False
            if mix == 0:
                globalvariables.WIN.blit(flour_image, flour_rect)
            if mix == 1:
                globalvariables.WIN.blit(cake_flour_image, cake_flour_rect)
            if mix == 2:
                globalvariables.WIN.blit(sugar_image, sugar_rect)
            if mix == 3:
                globalvariables.WIN.blit(shaker_image, shaker_rect)
            if mix == 4:
                globalvariables.WIN.blit(bakingpowder_image, bakingpowder_rect)
            if mix == 5:
                globalvariables.WIN.blit(bakingsoda_image, bakingsoda_rect)
            if mix == 6:
                globalvariables.WIN.blit(butter_image, butter_rect)
            if mix == 7:
                globalvariables.WIN.blit(egg1_image, egg_rect)
            if mix == 8:
                globalvariables.WIN.blit(egg1_image, egg_rect)
            if mix == 9:
                globalvariables.WIN.blit(milk_image, milk_rect)
            if mix == 10:
                globalvariables.WIN.blit(vanilla_extract_image, vanilla_extract_rect)
            if mix == 11:
                mixingBowl(True, mixingBowl_image, 300, 265, 300, 300)
                mixing = False

        pygame.display.update()
    
    while baking:
        for event in pygame.event.get(): #allows user to quit the window
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                caketinPressed = caketin_button.checkPressed(pygame.mouse.get_pos())
                if caketinPressed:
                    filling = filling + 1
                ovenPressed = oven_button.checkPressed(pygame.mouse.get_pos())
                ovenActive = oven_button.getActive()
                if ovenPressed == True and ovenActive == True:
                    baking = False
                    oven_button.setUnactive()
                if event.button == 1:
                    if oven_rects[oven].collidepoint(event.pos):
                        active_ingredient = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    active_ingredient = False
            if event.type == pygame.MOUSEMOTION:
                if active_ingredient:
                    oven_rects[oven].move_ip(event.rel)

        globalvariables.WIN.blit(gameBg_image, bgPosition)
        
        if value == "Baking 1":
            caketin_button.draw()
            if filling == 1:
                fill(True, cakebatter_colour, colours)
                filling = filling + 1
            if filling == 2:
                caketin_button.draw()
            if filling == 3:
                fill(True, cakebatter_colour, colours)
                value, stack, visitedNodes = treeTraversal("burger", stack, visitedNodes)
                bake = bake + 1
        if value == "Baking 2" :
            if bake == 1 or bake == 2 or bake == 3:
                globalvariables.WIN.blit(oven_image, (530, 200))
            if bake == 1 or bake == 2:
                if active_ingredient:
                    mx, my = pygame.mouse.get_pos()
                    if 530 <= mx - 190 <= (530 + oven_width) and 200 <= my - 190 <= (200 + oven_height):
                        if bake == 1:
                            bake = bake + 1
                            oven = oven + 1
                        else:
                            bake = bake + 1
                        active_ingredient = False

            if bake == 1:
                globalvariables.WIN.blit(caketin_filled_image, caketin_filled1_rect)
            if bake == 2:
                globalvariables.WIN.blit(caketin_filled_image, caketin_filled2_rect)
            if bake == 3:
                oven_button.setActive()
                oven_button.draw()

        
        pygame.display.update()

    frosting_rects = [butter_rect, sugar_rect, vanilla_extract_rect, milk_rect]

    while frosting:
        for event in pygame.event.get(): #allows user to quit the window
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if frosting_rects[mix].collidepoint(event.pos):
                        active_ingredient = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    active_ingredient = False
            if event.type == pygame.MOUSEMOTION:
                if active_ingredient:
                    frosting_rects[mix].move_ip(event.rel)

            globalvariables.WIN.blit(gameBg_image, bgPosition)
            if value == "Frosting 1":
                if mix <= 4:
                    globalvariables.WIN.blit(mixingBowl_image, (575, 265))
                    if active_ingredient:
                        mx, my = pygame.mouse.get_pos()
                        if 575 <= mx - 120 <= (575 + bowl_width) and 265 + 20 <= my - 120 <= (265 + bowl_height):
                            mix = mix + 1
                            active_ingredient = False
                if mix == 0:
                    globalvariables.WIN.blit(butter_image, butter_rect)
                if mix == 1:
                    globalvariables.WIN.blit(sugar_image, sugar_rect)
                if mix == 2:
                    globalvariables.WIN.blit(vanilla_extract_image, vanilla_extract_rect)
                if mix == 3:
                    globalvariables.WIN.blit(milk_image, milk_rect)
                if mix == 4:
                    mixingBowl(True, mixingBowl_image, 300, 265, 300, 300)
                    frosting = False

            pygame.display.update()
    
    while decorating:
        for event in pygame.event.get(): #allows user to quit the window
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break
        

        if value == "Decoration 1":
            recipeAssembly(True, "cake", colours)
            value, stack, visitedNodes = treeTraversal("burger", stack, visitedNodes)
        if value == "Decoration 2":
            globalvariables.WIN.blit(gameBg_image, bgPosition)
            globalvariables.WIN.blit(assembledcake_image, (300, 200))
            draw(True, 401.0, 656.0, 233.0, 521.0, 565.0, 518.0, 399.0, 329.0, 0, timer_text, timer_box)
            value, stack, visitedNodes = treeTraversal("burger", stack, visitedNodes)
        if value == "Decoration 3":
            globalvariables.WIN.blit(gameBg_image, bgPosition)
            globalvariables.WIN.blit(frostedcake_image, (300, 200))
            seasoning(True, frostedcake_image, 300, 200, 400, 400, "sprinkles")
            decorating = False



        pygame.display.update()

    return value, stack, visitedNodes

def sushiGame(value, stack, visitedNodes, score, colours):

    cooking = False
    assembly = False
    cutting = False

    value = "Assembly"

    if value == "Cooking":
        cooking = True
        value = "Cooking 1"
    elif value == "Assembly":
        assembly = True
        value = "Assembly 1"
    elif value == "Cutting":
        cutting = True
    
    timer_text = classes.Text(52, 12, "00.00", (255, 255, 255), 24)
    timer_box = classes.Box(50, 10, 50, 50, colours[5], False)
    game_ticks = 0
    other_ticks = 0

    cook = 0
    cut = 0

    active_ingredient = False
    rice_rect = rice_image.get_rect()
    rice_rect.center = (250, 450)
    sushiseasoning_rect = sushiseasoning_image.get_rect()
    sushiseasoning_rect.center = (250, 450)
    rects = [rice_rect, sushiseasoning_rect]

    #buttons
    cucumber2_button = classes.ImageButton(340, 280, cucumber2_image, 1)

    while cooking:
        for event in pygame.event.get(): #allows user to quit the window
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break
        
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if rects[cook].collidepoint(event.pos):
                        active_ingredient = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    active_ingredient = False
            if event.type == pygame.MOUSEMOTION:
                if active_ingredient:
                    rects[cook].move_ip(event.rel)

        globalvariables.WIN.blit(gameBg_image, bgPosition)
        if value == "Cooking 1":
            if cook <= 2:
                globalvariables.WIN.blit(ricecooker_image, (525, 235))
                if active_ingredient:
                    mx, my = pygame.mouse.get_pos()
                    if 525 <= mx - 190 <= (525 + ricecooker_width) and 235 + 20 <= my - 190 <= (235 + ricecooker_height):
                        cook = cook + 1
                        active_ingredient = False
            if cook == 0:
                globalvariables.WIN.blit(rice_image, rice_rect)
            if cook == 1:
                globalvariables.WIN.blit(sushiseasoning_image, sushiseasoning_rect)
            if cook == 2:
                value = "Cooking 2" #CHANGE THIS
        if value == "Cooking 2":
            fill(True, water_colour, colours)


        pygame.display.update()
    
    while assembly:
        for event in pygame.event.get(): #allows user to quit the window
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break
        
            if event.type == pygame.MOUSEBUTTONDOWN:
                cucumber2Pressed = cucumber2_button.checkPressed(pygame.mouse.get_pos())
                cucumber2Active = cucumber2_button.getActive()
                if cucumber2Pressed == True and cucumber2Active == True:
                    cut = cut + 1
                    cucumber2_button.setUnactive()
        
        globalvariables.WIN.blit(gameBg_image, bgPosition)
        globalvariables.WIN.blit(clock_image, (20, 10))
        timer_box.drawBox()
        #game_ticks = pygame.time.get_ticks()
        print((((pygame.time.get_ticks() - game_ticks) / 1000)))
        timer_text.changeText(str(((pygame.time.get_ticks() - other_ticks) + game_ticks) / 1000))

        if value == "Assembly 1":
            globalvariables.WIN.blit(cuttingBoard_image, (100, 170))
            if cut == 0:
                globalvariables.WIN.blit(cucumbers[0], (340, 280))
                globalvariables.WIN.blit(pygame.transform.scale(arrow2_image, (300, 200)), (400, 250))
                other_ticks = draw(True, 591.0, 452.0, 547.0, 493.0, 550.0, 407.0, 317.0, 453.0, 0, timer_text, timer_box)
                cut = cut + 1
            elif cut == 1:
                cucumber2_button.draw()
                cucumber2_button.setActive()
            elif cut == 2:
                globalvariables.WIN.blit(cucumbers[2], (340, 280))
                globalvariables.WIN.blit(pygame.transform.scale(arrow2_image, (300, 200)), (400, 270))
                other_ticks = draw(True, 349.0, 562.0, 392.0, 587.0, 431.0, 561.0, 387.0, 407.0, game_ticks, timer_text, timer_box)
                cut = cut + 1
    
    while cutting:
        for event in pygame.event.get(): #allows user to quit the window
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break






    







