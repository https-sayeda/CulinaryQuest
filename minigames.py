# Imports
import sys
import pygame
import random
import os
import classes
import globalvariables

#variables
bgPosition = (0,0)

#loading and transforming commonly used images images
game1Bg_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','game1_background.png'))
game2Bg_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','minigame1_background.png'))
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

#burger images, loading and transforming them
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

#made the onion images into an array to make it easier to access
onions = [ onioncut1_image, onioncut2_image, onioncut2_1_image, onioncut3_image, onioncut4_image, 
          onioncut4_1_image, onioncut4_2_image, onioncut4_3_image, onioncut4_4_image, onioncut4_5_image, 
          onioncut4_6_image, onioncut4_7_image, onioncut4_8_image, onioncut4_9_image, dicedonion_image]

#transforming the onion images
for i in range(len(onions)):
    onions[i] = pygame.transform.scale(onions[i], (300,300))

dicedonion2_image = pygame.transform.scale(dicedonion_image, (300,300))

#cake images, loading and transforming them
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

#sushi images, loading and transforming
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

#cucumbers transformed using an array to make it easier
for i in range(len(cucumbers)):
    cucumbers[i] = pygame.transform.scale(cucumbers[i], (300,150))

avocado1_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','avocado1.png'))
avocado1_5_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','avocado1_5.png'))
avocado2_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','avocado2.png'))
avocado3_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','avocado3.png'))
avocado4_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','avocado4.png'))
avocado5_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','avocado5.png'))
avocado6_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','avocado6.png'))
avocado7_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','avocado7.png'))
avocados = [avocado1_image, avocado1_5_image, avocado2_image, avocado3_image, avocado4_image, avocado5_image, avocado6_image, 
            avocado7_image, ]

#avocados transformed using an array to make it easier
for i in range(len(avocados)):
    avocados[i] = pygame.transform.scale(avocados[i], (300,300))

salmon1_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','salmon.png'))
salmon2_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','salmon2.png'))
salmon3_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','salmon3.png'))
salmon1_image = pygame.transform.scale(salmon1_image, (300,300))
salmon2_image = pygame.transform.scale(salmon2_image, (300,300))
salmon3_image = pygame.transform.scale(salmon3_image, (300,300))

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

#seaweed images transformed using an array to make it easier
for i in range(len(seaweeds)):
    seaweeds[i] = pygame.transform.scale(seaweeds[i], (500,500))

sushiroll1_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','sushiroll.png'))
sushiroll2_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','sushiroll2.png'))
sushiroll3_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','sushiroll3.png'))
sushiroll4_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','sushiroll4.png'))
sushiroll5_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','sushiroll5.png'))
sushiroll6_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','sushiroll6.png'))
sushiroll7_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','sushiroll7.png'))
sushirolls = [sushiroll1_image, sushiroll2_image, sushiroll3_image, sushiroll4_image, sushiroll5_image, 
              sushiroll6_image, sushiroll7_image]

#the sushi roll images transformed using an array to make it easier
for i in range(len(sushirolls)):
    sushirolls[i] = pygame.transform.scale(sushirolls[i], (800, 180))

slicedcucumber_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','slicedcucumber.png'))
slicedavocado_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','slicedavocado.png'))
slicedsalmon_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','slicedsalmon.png'))
slicedcucumber_image = pygame.transform.scale(slicedcucumber_image, (250, 100))
slicedavocado_image = pygame.transform.scale(slicedavocado_image, (250, 100))
slicedsalmon_image = pygame.transform.scale(slicedsalmon_image, (250, 100))

#width and height of objects that will be needed to use
bowl_width = 300
bowl_height = 300
oven_width = 400
oven_height = 400
ricecooker_width = 400
ricecooker_height = 400
seaweed_width = 500
seaweed_height = 500

#colours
cakebatter_colour = pygame.Color(248, 226, 159)
water_colour = pygame.Color(115, 203, 251)
fillBg_colour = pygame.Color(61, 61, 61)

#text boxes
draw1instruction_text = classes.Text(2, 553, "Trace the arrow to cut the ingredient", (255, 255, 255), 24)
draw2instruction_text = classes.Text(2, 553, "Frost the cake by covering all of it", (255, 255, 255), 24)
draw3instruction_text = classes.Text(2, 553, "Cover the seaweed, leaving 1 inch at the top", (255, 255, 255), 24)

flipinstruction_text = classes.Text(2, 553, "Press space when the arrow is on green", (255, 255, 255), 24)
mixinstruction_text = classes.Text(2, 553, "Press A/D or <-/-> to mix the ingredients", (255, 255, 255), 24)
fillinstruction_text = classes.Text(2, 553, "Hold space to fill up until the red line", (255, 255, 255), 24)
seasoninginstruction_text = classes.Text(2, 553, "Move your mouse up and down", (255, 255, 255), 24)
assemblyinstruction_text = classes.Text(2, 553, "Press A/D or <-/-> to catch the ingredients", (255, 255, 255), 24)

drag1instruction_text = classes.Text(2, 553, "Drag the ingredient into the bowl", (255, 255, 255), 24)
drag2instruction_text = classes.Text(2, 553, "Drag the ingredient into the oven", (255, 255, 255), 24)
drag3instruction_text = classes.Text(2, 553, "Drag the ingredient into the rice cooker", (255, 255, 255), 24)

clickinstruction_text = classes.Text(2, 553, "Click the ingredient to continue", (255, 255, 255), 24)
click2instruction_text = classes.Text(2, 553, "Click the button to continue", (255, 255, 255), 24)

waitinstruction_text = classes.Text(2, 553, "Wait a few seconds...", (255, 255, 255), 24)

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
    burgerRoot.children[1].children = [RecipeTree("Mixing 1"), RecipeTree("Mixing 2"), RecipeTree("Mixing 3"), RecipeTree("Mixing 4"), RecipeTree("Mixing 5")]
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
    sushiRoot.children[0].children = [RecipeTree("Cooking 1"), RecipeTree("Cooking 2")]
    sushiRoot.children[1].children = [RecipeTree("Assembly 1"), RecipeTree("Assembly 2"), RecipeTree("Assembly 3"), RecipeTree("Assembly 4")]
    sushiRoot.children[2].children = [RecipeTree("Cutting 1")]
    
    if recipeChosen == "burger": #determines which tree is being traversed
        value = burgerRoot.preorder(stack, visitedNodes)
    elif recipeChosen == "cake":
        value = cakeRoot.preorder(stack, visitedNodes)
    elif recipeChosen == "sushi":
        value = sushiRoot.preorder(stack, visitedNodes)
    
    return value, stack, visitedNodes

def draw(draw, x1, y1, x2, y2, x3, y3, x4, y4, brushSize, boundary, start_time, counting_time, timer_text, timer_box, colours):

    flag1 = False #these flags represent whether the drawn circle has touched a coordinate
    flag2 = False #there are 4 points to the arrow, so four coordinates (x1, y2), (x2, y2) etc. = four flags
    flag3 = False 
    flag4 = False
    # the colour and size of the brush
    drawColour = colours[1] #depends on the theme selected
    canvasSize = [800, 800]

    # Canvas
    canvas = pygame.Surface((canvasSize),pygame.SRCALPHA)
    canvas.set_alpha(200) 
    #makes the canvas transparent so that it doesn't cover the background image

    clock = pygame.time.Clock()

    while draw: #ensures that the user only draws when they havent drawn the arrow
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break
        
        timer_box.drawBox()
        counting_time = pygame.time.get_ticks() - start_time
        timer_text.changeText(str( int(counting_time/1000) ).zfill(2))

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

            pygame.draw.circle(canvas, drawColour,[dx, dy], brushSize) #draws the circle

        if (x1- boundary) <= dx <= (x1+ boundary) and (y1- boundary) <= dy <= (y1+ boundary): 
            #this  ensures that the user doesnt need to get an exact coordinate, but instead a range within
            #a certain area
            flag1 = True #if the circle is drawn in the range, then the flag is set to true
        if (x2- boundary) <= dx <= (x2+ boundary) and (y2- boundary) <= dy <= (y2+ boundary):
            flag2 = True
        if (x3- boundary) <= dx <= (x3+ boundary) and (y3- boundary) <= dy <= (y3+ boundary):
            flag3 = True
        if (x4- boundary) <= dx <= (x4+ boundary) and (y4- boundary) <= dy <= (y4+ boundary):
            flag4 = True

        clock.tick(globalvariables.FPS)
        pygame.display.update() #updates the screen
    
    return start_time, counting_time
      
def recipeAssembly(assembly, recipeChosen, colours, start_time, counting_time, timer_text, timer_box, themeSelected):

    clock = pygame.time.Clock()
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

    if themeSelected == "theme1":
        gameBg_image = game1Bg_image #displays correct background image
    elif themeSelected == "theme2":
        gameBg_image = game2Bg_image

    hand_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','hand.png'))

    topBun_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','burger_bun.png'))
    bottomBun_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','burger_bottombun.png'))
    cheeseLayer_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','burger_cheese.png'))
    lettuceLayer_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','burger_lettuce.png'))
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
    meatLayer_image = pygame.transform.scale(meatLayer_image, (component_width, component_height))
    tomatoLayer_image = pygame.transform.scale(tomatoLayer_image, (component_width, component_height))

    cakeLayer1_image = pygame.transform.scale(cakeLayer1_image, (component_width, component_height))
    cakeLayer2_image = pygame.transform.scale(cakeLayer2_image, (component_width, component_height - 20))
    cakeLayer3_image = pygame.transform.scale(cakeLayer3_image, (component_width, component_height + 20))

    burgerLayer_images = [bottomBun_image, lettuceLayer_image, meatLayer_image, cheeseLayer_image, tomatoLayer_image, topBun_image]
    burgerLayer_order = []

    cakeLayer_images = [cakeLayer1_image, cakeLayer2_image, cakeLayer3_image]
    cakeLayer_order = []

    if recipeChosen == "burger":
        layer_images = burgerLayer_images #determines which images will be used based on the recipe chosen
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

    instruction_box = classes.Box(0, 550, 40, 400, colours[2], False)

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
        

        if count != (len(layer_images) + 1): #while it has not reached the end of the layers + 1 (allows the top layer to be added)

            keys = pygame.key.get_pressed()
            clock.tick(60)
            globalvariables.WIN.blit(gameBg_image, bgPosition)
            if len(layer_order) == 0: #if there are no layers that have been caught yet
                instruction_box.drawBox()
                assemblyinstruction_text.drawText() #display the instruction
            
            globalvariables.WIN.blit(clock_image, (20, 10))
            timer_box.drawBox()
            counting_time = pygame.time.get_ticks() - start_time
            timer_text.changeText(str( int(counting_time/1000) ).zfill(2)) #displays the time

            if count != (len(layer_images)): #if not all the layers have been caught
                component_rect = globalvariables.WIN.blit(layer_images[count], (component_x, component_y))
                #a rect is created for the component and hand that will be used to detect a collision between them
            
            hand_rect = globalvariables.WIN.blit(hand_image, (hand_x, hand_y)) #display the hand

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

        clock.tick(globalvariables.FPS)
        pygame.display.update()
    

    return start_time, counting_time

def flip(flip, bar_x, bar_y, images, coordinates, colours, start_time, counting_time, timer_text, timer_box, flippingScore, themeSelected):
    
    #variables that are needed
    clock = pygame.time.Clock()
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

    if themeSelected == "theme1":
        gameBg_image = game1Bg_image #background image displayed depends on the theme
    elif themeSelected == "theme2":
        gameBg_image = game2Bg_image

    temperatureBar_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','temperature_bar.png'))
    fillArrow_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','fillArrow.png'))

    #transforming images
    temperatureBar_image = pygame.transform.scale(temperatureBar_image, (bar_width, bar_height))
    fillArrow_image = pygame.transform.scale(fillArrow_image, (arrow_width, arrow_height))

    instruction_box = classes.Box(0, 550, 40, 430, colours[2], False)

    while flip: #while it is running

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break
        
        #displaying the images on the screen
        globalvariables.WIN.blit(gameBg_image, bgPosition)
        globalvariables.WIN.blit(clock_image, (20, 10))
        timer_box.drawBox()
        counting_time = pygame.time.get_ticks() - start_time
        timer_text.changeText(str( int(counting_time/1000) ).zfill(2)) #displays the time

        for i in range(len(images)):
            globalvariables.WIN.blit(images[i], coordinates[i])
        globalvariables.WIN.blit(temperatureBar_image, (bar_x, bar_y))
        globalvariables.WIN.blit(fillArrow_image, (arrow_x, arrow_y))

        instruction_box.drawBox()
        flipinstruction_text.drawText()

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
            if (bar_y) <= arrow_y <= (bar_y + 2*(bar_height // 11)) or ((bar_y + bar_height) - 2*(bar_height // 11)) <= arrow_y <= (bar_y + bar_height):
                flippingScore = flippingScore - 20
            elif (bar_y + 2*(bar_height // 11)) <= arrow_y <= (bar_y + 4*(bar_height // 11)) or ((bar_y + bar_height) - 4*(bar_height // 11))  <= arrow_y <=  ((bar_y + bar_height) - 2*(bar_height // 11)):
                flippingScore = flippingScore - 10
            elif (bar_y + 4*(bar_height // 11)) <= arrow_y <= (bar_y + 8*(bar_height // 11)) or (bar_y + bar_height - 8*(bar_height // 11)) <= arrow_y <= (bar_y + bar_height - 4*(bar_height // 11)):
                flippingScore = flippingScore
            flip = False #no longer running


        pygame.display.update()
    return start_time, counting_time, flippingScore

def fill(fill, fill_colour, colours, start_time, counting_time, timer_text, timer_box, themeSelected):
    
    clock = pygame.time.Clock()
    fillBg_box = classes.Box(300, 50, 500, 400, fillBg_colour, False)
    fill_box = classes.Box(302, 540, 10, 396, fill_colour, True)
    fill_line = classes.Box(300, 100, 10, 400, (214, 135, 140), False) 
    #the colour will change depending on the recipe as sushi uses water while cake will use cake batter
    fill_height = 0 #the initial height of the liquid is 0
    spacebar_down = False #the spacebar being pressed is initially set to false
    fill_y = 540 #the y coordinate of where the liquid is

    back_button = classes.Button(770, 500, 70, 100, colours[3], False) #back button to move onto next step
    back_button.setUnactive()
    back_text = classes.Text(785, 503, "-->", (255, 255, 255), 50)
    fillingScore = 0
    goodFill = False

    instruction_box = classes.Box(0, 550, 40, 430, colours[2], False) #box for instruction

    if themeSelected == "theme1":
        gameBg_image = game1Bg_image #background used based on theme
    elif themeSelected == "theme2":
        gameBg_image = game2Bg_image

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
        globalvariables.WIN.blit(clock_image, (20, 10))
        timer_box.drawBox()
        counting_time = pygame.time.get_ticks() - start_time
        timer_text.changeText(str( int(counting_time/1000) ).zfill(2)) #displays time
        fillBg_box.drawBox()
        fill_box.drawBox()
        fill_line.drawBox()
        back_button.drawBox()
        back_text.drawText()
        instruction_box.drawBox()
        fillinstruction_text.drawText() #displays instruction

        if spacebar_down == True and fill_height < 500: 
            #if the spacebar is being pressed and the liquid is below the max height
            fill_y = fill_box.changeY(fill_y - 1) #increase the fill by 1
            fill_height = fill_box.changeHeight(1)
        if 450 < fill_height or fill_height < 410: #if it goes over the red line or too below the line
            goodFill = True


        clock.tick(globalvariables.FPS)
        pygame.display.update()
    if goodFill:
        fillingScore = -40 #score will decrease by 40
    return start_time, counting_time, fillingScore
        
def mixingBowl(mixing, image, image_x, image_y, image_width, image_height, colours, start_time, counting_time, timer_text, timer_box, themeSelected):

    clock = pygame.time.Clock()
    orientation = "right" #the orientation of the bowl is initially set to the right
    time_down = 0.0 #used to measure the amount of time between the bowl being flipped
    time_elapsed = 0.0 #records the total time
    count = 0 #records how often they went too fast
    mix = 0 #how many times they mixed successfully
    rate = pygame.time.Clock() #used to time
    spilled = False
    mixingScore = 0

    #loading image
    mixingBowlSpilled_image = pygame.image.load(os.path.join('Culinary Quest ASSETS','mixingbowl_spilled.png'))
    mixingBowlSpilled_image = pygame.transform.scale(mixingBowlSpilled_image, (image_width, image_height))

    back_button = classes.Button(770, 500, 70, 100, colours[3], False)
    back_button.setUnactive()
    back_text = classes.Text(785, 503, "-->", (255, 255, 255), 50)

    instruction_box = classes.Box(0, 550, 40, 430, colours[2], False)
    toofast_box = classes.Box(500, 200, 40, 90, colours[2], False)
    toofast_text = classes.Text(502, 203, "Too fast!", (255, 255, 255), 24)

    if themeSelected == "theme1":
        gameBg_image = game1Bg_image
    elif themeSelected == "theme2":
        gameBg_image = game2Bg_image

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
            if event.type == pygame.MOUSEBUTTONDOWN:
                backPressed = back_button.checkPressed(pygame.mouse.get_pos())
                backActive = back_button.getActive()
                if backPressed == True and backActive == False:
                    mixing = False
                    back_button.setActive()

        if count >= 5: #if they went too fast 5 times
            globalvariables.WIN.blit(gameBg_image, bgPosition) 
            globalvariables.WIN.blit(clock_image, (20, 10))
            timer_box.drawBox()
            counting_time = pygame.time.get_ticks() - start_time
            timer_text.changeText(str( int(counting_time/1000) ).zfill(2)) #displays the time
            globalvariables.WIN.blit(mixingBowlSpilled_image, (image_x, image_y)) #th mixture is spilled so display new image
            spilled = True
            back_button.drawBox()
            back_text.drawText()
            pygame.display.update() #update screen
        elif mix == 7:
            timer_box.drawBox()
            counting_time = pygame.time.get_ticks() - start_time
            timer_text.changeText(str( int(counting_time/1000) ).zfill(2))
            back_button.drawBox()
            back_text.drawText()
            pygame.display.update()

        if count < 5: #as long as the mixture hasn;t spilled
            globalvariables.WIN.blit(gameBg_image, bgPosition) #background image displayed
            instruction_box.drawBox()
            mixinstruction_text.drawText()
            globalvariables.WIN.blit(clock_image, (20, 10))
            timer_box.drawBox()
            counting_time = pygame.time.get_ticks() - start_time
            timer_text.changeText(str( int(counting_time/1000) ).zfill(2)) #time is displayed
            if orientation == "right" and count < 5: #if the bowl is flipped to the right
                globalvariables.WIN.blit(image, (image_x, image_y)) #it is normal so display as normal
            elif orientation == "left" and count < 5: #if it's to the left
                image2 = pygame.transform.flip(image, True, False) #it needs to be flipped horizontally
                globalvariables.WIN.blit(image2, (image_x, image_y)) #it is drawn
            if 0 < time_elapsed < 0.30: #if the tipe between pressing the keys is less than 0.3 seconds
                toofast_box.drawBox()
                toofast_text.drawText()
                time_down = 0.0 #time reset
                time_elapsed = 0.0
                count = count + 1 #count is incremented to represet the no. of times they went too fast

        rate.tick()

        clock.tick(globalvariables.FPS)
        pygame.display.update()

    if spilled:
        mixingScore = -40
    return start_time, counting_time, mixingScore
        
def seasoning(seasoning, image, image_x, image_y, image_width, image_height, seasoning_type, colours, start_time, counting_time, timer_text, timer_box, themeSelected):
    
    #variables that are needed
    clock = pygame.time.Clock()
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

    if themeSelected == "theme1":
        gameBg_image = game1Bg_image #determines which background to use based on the theme
    elif themeSelected == "theme2":
        gameBg_image = game2Bg_image

    instruction_box = classes.Box(0, 550, 40, 430, colours[2], False)

    while seasoning: #while running

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break
        
        mouse_x, mouse_y = pygame.mouse.get_pos() #get the x and y coordinate of the position of the mouse
        mouse_y_position.append(mouse_y) #put the y coordinate into the array
        globalvariables.WIN.blit(gameBg_image, bgPosition) #display image
        instruction_box.drawBox()
        seasoninginstruction_text.drawText()
        globalvariables.WIN.blit(clock_image, (20, 10))
        timer_box.drawBox()
        counting_time = pygame.time.get_ticks() - start_time
        timer_text.changeText(str( int(counting_time/1000) ).zfill(2)) #displays the time spent on this step of the recipe
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

        clock.tick(globalvariables.FPS)
        pygame.display.update()
    return start_time, counting_time

def burgerGame(value, stack, visitedNodes, score, burgerScore, colours, ingredients, startingScreen, themeSelected):

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
    start_time = pygame.time.get_ticks() #used to calculate the time within the game
    clock = pygame.time.Clock()
    counting_time = 0

    cut = 0 #variables initialised for the steps in the recipe
    fry = 0
    mix = 0

    #determining the background image based on the theme
    if themeSelected == "theme1":
        gameBg_image = game1Bg_image
    elif themeSelected == "theme2":
        gameBg_image = game2Bg_image

    #text object
    timer_text = classes.Text(162, 47, "00.00", (255, 255, 255), 24) #displays the time
    instruction_box = classes.Box(0, 550, 40, 380, colours[2], False) #background box for the instructions

    #box objects
    timer_box = classes.Box(150, 45, 30, 60, colours[5], False) #background box for the timer
    ingredient_box = classes.Box(300, 100, 40, 350, colours[2], False) #background box for displaying ingredients
    ingredien2_box = classes.Box(700, 100, 40, 350, colours[2], False)

    #button objects
    onioncut2_1_button = classes.ImageButton(340, 210, onions[2], 1)
    onioncut3_button = classes.ImageButton(340, 210, onions[3], 1)
    onioncut4_9_button = classes.ImageButton(340, 210, onions[13], 1)
    dicedonion_button = classes.ImageButton(340, 210, onions[14], 1)
    dicedonion2_button = classes.ImageButton(200, 230, onions[14], 1)
    oilBottle_button = classes.ImageButton(720, 280, oilBottle_image, 2.5)
    offbutton_button = classes.ImageButton(760, 280, offbutton_image, 0.4)
    burgerPatty_button = classes.ImageButton(150, 350, burgerPatty_image, 1)
    cookedPatty_button = classes.ImageButton(250, 300, cookedPatty_image, 1)

    while frying:
        for event in pygame.event.get(): #allows user to quit the window
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break
            if event.type == pygame.MOUSEBUTTONDOWN: #if the mouse has been pressed
                onioncut2_1Pressed = onioncut2_1_button.checkPressed(pygame.mouse.get_pos()) #check if first onion button is pressed
                if onioncut2_1Pressed and cut == 2: #if its on cut 2 and has been pressed
                    cut = cut + 1 #increment cut
                onioncut3Pressed = onioncut3_button.checkPressed(pygame.mouse.get_pos()) #check if next onion button is pressed
                if onioncut3Pressed and cut == 3: #if it is on this cut stage
                    cut = cut + 1 #increment cut
                onioncut4_9Pressed = onioncut4_9_button.checkPressed(pygame.mouse.get_pos())
                onioncut4_9Active = onioncut4_9_button.getActive()
                if onioncut4_9Pressed and cut == 13 and onioncut4_9Active == False: #if the button has been pressed and it is not active (the default state)
                    cut = cut + 1 #increment cut
                    onioncut4_9_button.setActive() #set to active so if it were to be pressed again, nothing will occur
                dicedonionPressed = dicedonion_button.checkPressed(pygame.mouse.get_pos()) #if the diced onion button has been pressed
                dicedonionActive = dicedonion_button.getActive()
                if dicedonionPressed == True and cut == 14 and onioncut4_9Active == True: 
                    #checks if all these conditions are true to ensure the user is at a specific point in the minigame
                    fry = fry + 1 #increment fry, will move on to the frying stage
                    value, stack, visitedNodes = treeTraversal("burger", stack, visitedNodes) #traverse to the next node in the tree
                    cut = cut + 1 #increment cut
                if dicedonionPressed == True and value == "Frying 3" and dicedonionActive == False:
                    fry = fry + 1
                    start_ticks = pygame.time.get_ticks() #starts timer for 10 seconds
                    value, stack, visitedNodes = treeTraversal("burger", stack, visitedNodes) #goes to next node
                    dicedonion_button.setActive()
                oilBottlePressed = oilBottle_button.checkPressed(pygame.mouse.get_pos())
                oilBottleActive = oilBottle_button.getActive()
                if oilBottlePressed and oilBottleActive == False: #checks if oil button is pressed and not acitve
                    fry = fry + 1 #increments fry
                    value, stack, visitedNodes = treeTraversal("burger", stack, visitedNodes) #goes to next node in tree
                    start_ticks = pygame.time.get_ticks() #starts the timer for the 7 seconds
                    oilBottle_button.setActive() #set it to active so it can't accidently be pressed again
                offbuttonPressed = offbutton_button.checkPressed(pygame.mouse.get_pos())
                if offbuttonPressed == True and value == "Frying 4" and dicedonionActive == True:
                    frying = False #ends the frying stage
        
        globalvariables.WIN.blit(gameBg_image, bgPosition)
        globalvariables.WIN.blit(clock_image, (20, 10))
        timer_box.drawBox()
        counting_time = pygame.time.get_ticks() - start_time #calculates the current time
        timer_text.changeText(str( int(counting_time/1000) ).zfill(2)) #converts it to seconds and displays

        if value == "Frying 1": #if the current node in the tree is "Frying 1"
            globalvariables.WIN.blit(cuttingBoard_image, (100, 170)) #display the cutting board
            if cut == 0: #if cut is 0 then..
                ingredient_box.drawBox() #display the ingredient box to tell the user the measurements
                ingredients[2].changePosition(305, 103)
                globalvariables.WIN.blit(onions[0], (340, 210)) #display the first onion image
                instruction_box.drawBox() #display the instructions
                draw1instruction_text.drawText()
                globalvariables.WIN.blit(arrow2_image, (370, 215)) #display the arrow that the user will have to trace
                start_time, counting_time = draw(True, 282.0, 412.0, 436.0, 377.0, 465.0, 412.0, 435.0, 459.0, 5, 10.0, start_time, counting_time, timer_text, timer_box, colours)
                #call the subroutine to draw, and will only exit the subroutine once the arrow has been traced (the user has drawn on the given coordinates)
                cut = cut + 1 #increment cut
            elif cut == 1: #once the first cut has occured
                globalvariables.WIN.blit(onions[1], (340, 210))
                globalvariables.WIN.blit(arrow3_image, (390, 295)) #display the next onion and arrow
                start_time, counting_time = draw(True, 349.0, 562.0, 392.0, 587.0, 431.0, 561.0, 387.0, 407.0, 5, 10.0, start_time, counting_time, timer_text, timer_box, colours)
                cut = cut + 1 #increment cut once the arrow has been traced
            elif cut == 2: #when cut is 2
                instruction_box.drawBox() #display the instructions
                clickinstruction_text.drawText()
                onioncut2_1_button.draw() #draw the button to be clicked
            elif cut == 3:
                instruction_box.drawBox() #display the instructions
                clickinstruction_text.drawText()
                onioncut3_button.draw()
            elif cut == 4:
                globalvariables.WIN.blit(onions[4], (340, 210))
                globalvariables.WIN.blit(pygame.transform.scale(arrow3_image, (200, 300)), (305, 215))
                start_time, counting_time = draw(True, 263.0, 565.0, 307.0, 608.0, 350.0, 565.0, 303.0, 332.0, 5, 10.0, start_time, counting_time, timer_text, timer_box, colours)
                cut = cut + 1
            elif cut == 5:
                globalvariables.WIN.blit(onions[5], (340, 210))
                globalvariables.WIN.blit(pygame.transform.scale(arrow3_image, (200, 300)), (345, 215))
                start_time, counting_time = draw(True, 344.0, 610.0, 305.0, 567.0, 384.0, 564.0, 344.0, 333.0, 5, 10.0, start_time, counting_time, timer_text, timer_box, colours)
                cut = cut + 1
            elif cut == 6:
                globalvariables.WIN.blit(onions[6], (340, 210))
                globalvariables.WIN.blit(pygame.transform.scale(arrow3_image, (200, 300)), (390, 215))
                start_time, counting_time = draw(True, 352.0, 567.0, 387.0, 609.0, 433.0, 561.0, 387.0, 335.0, 5, 10.0, start_time, counting_time, timer_text, timer_box, colours)
                cut = cut + 1
            elif cut == 7:
                globalvariables.WIN.blit(onions[7], (340, 210))
                globalvariables.WIN.blit(pygame.transform.scale(arrow3_image, (200, 300)), (420, 215))
                start_time, counting_time = draw(True, 418.0, 334.0, 375.0, 561.0, 423.0, 611.0, 469.0, 561.0, 5, 10.0, start_time, counting_time, timer_text, timer_box, colours)
                cut = cut + 1
            elif cut == 8:
                globalvariables.WIN.blit(onions[8], (340, 210))
                globalvariables.WIN.blit(pygame.transform.scale(arrow3_image, (200, 300)), (460, 215))
                start_time, counting_time = draw(True, 419.0, 565.0, 460.0, 607.0, 507.0, 561.0, 455.0, 330.0, 5, 10.0, start_time, counting_time, timer_text, timer_box, colours)
                cut = cut + 1
            elif cut == 9:
                globalvariables.WIN.blit(onions[9], (340, 210))
                globalvariables.WIN.blit(pygame.transform.scale(arrow3_image, (200, 300)), (433, 215))
                start_time, counting_time = draw(True, 394.0, 565.0, 434.0, 605.0, 478.0, 561.0, 430.0, 334.0, 5, 10.0, start_time, counting_time, timer_text, timer_box, colours)
                cut = cut + 1
            elif cut == 10:
                globalvariables.WIN.blit(onions[10], (340, 210))
                globalvariables.WIN.blit(pygame.transform.scale(arrow2_image, (310, 200)), (330, 315))
                start_time, counting_time = draw(True, 487.0, 555.0, 492.0, 472.0, 533.0, 516.0, 240.0, 517.0, 5, 10.0, start_time, counting_time, timer_text, timer_box, colours)
                cut = cut + 1
            elif cut == 11:
                globalvariables.WIN.blit(onions[11], (340, 210))
                globalvariables.WIN.blit(pygame.transform.scale(arrow2_image, (310, 200)), (330, 270))
                start_time, counting_time = draw(True, 248.0, 473.0, 489.0, 511.0, 485.0, 429.0, 531.0, 470.0, 5, 10.0, start_time, counting_time, timer_text, timer_box, colours)
                cut = cut + 1
            elif cut == 12:
                globalvariables.WIN.blit(onions[12], (340, 210))
                globalvariables.WIN.blit(pygame.transform.scale(arrow2_image, (310, 200)), (330, 215))
                start_time, counting_time = draw(True, 489.0, 451.0, 245.0, 413.0, 480.0, 372.0, 529.0, 417.0, 5, 10.0, start_time, counting_time, timer_text, timer_box, colours)
                cut = cut + 1
            elif cut == 13:
                instruction_box.drawBox() #display the instructions
                clickinstruction_text.drawText()
                onioncut4_9_button.draw()
            elif cut == 14:
                instruction_box.drawBox() #display the instructions
                clickinstruction_text.drawText()
                dicedonion_button.draw()
        
        if value == "Frying 2":
            globalvariables.WIN.blit(cooker_image, (180, 190)) #displays the cooker
            if fry == 1: #if fry is 1
                globalvariables.WIN.blit(fryingPan_image, (-50, 60)) #displays frying pan
                ingredient_box.drawBox() #the ingredient box
                ingredients[1].changePosition(305, 103) #ingredient text for oil
                oilBottle_button.draw() #draw the oil button
                instruction_box.drawBox() #display the instructions
                clickinstruction_text.drawText()
            elif fry == 2: #when fry is 2 (when the button is pressed)
                globalvariables.WIN.blit(fryingPanOil_image, (-50, 60)) #display the oil in the frying pan
        
        if value == "Frying 3":
            globalvariables.WIN.blit(cooker_image, (180, 190))
            globalvariables.WIN.blit(fryingPanOil_image, (-50, 60))
            if fry == 2:
                instruction_box.drawBox() #display the instructions
                waitinstruction_text.drawText() #tells the user that they have to wait
                seconds = ((pygame.time.get_ticks() - start_ticks) / 1000)
                if seconds > 7.0: #after 7 seconds
                    dicedonion_button.changePosition(720, 280) #the onion button will appear 
                    instruction_box.drawBox() #display the instructions
                    clickinstruction_text.drawText()
        
        if value == "Frying 4": #after the onion button has been clicked
            globalvariables.WIN.blit(cooker_image, (180, 190))
            globalvariables.WIN.blit(fryingPanOil_image, (-50, 60))
            dicedonion2_button.draw()
            if fry == 3:
                instruction_box.drawBox() #display the instructions
                waitinstruction_text.drawText()
                seconds = ((pygame.time.get_ticks() - start_ticks) / 1000)
                if seconds > 10.0: #after 10 seconds
                    instruction_box.drawBox() #display the instructions
                    click2instruction_text.drawText()
                    offbutton_button.draw() #an off button will appear
        
        clock.tick(globalvariables.FPS)

        pygame.display.update()
    
    if value == "Frying 4":
        if int(counting_time / 1000) <= 90: #if the time is less than or equal to 90 seconds
            burgerScore.append(100) #gives the frying stage a score of 100
        elif 91 <= int(counting_time / 1000) <= 120: #if it is between 91 and 120 seconds then
            burgerScore.append(70) #give a score of 70
        elif int(counting_time / 1000) >= 150: #if the time is higher than 150 seconds
            burgerScore.append(50) #give a score of 50
        score = score + burgerScore[0] #add to total score

    #rects for dragging mechanic
    active_ingredient = False
    mince_rect = beefMince_image.get_rect()
    mince_rect.center = (150, 400)
    egg_rect = egg1_image.get_rect()
    egg_rect.center = (150, 420)
    onion_rect = dicedonion2_image.get_rect()
    onion_rect.center = (150, 400)
    rects = [mince_rect, egg_rect, onion_rect]

    while mixing:
        for event in pygame.event.get(): #allows user to quit the window
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break
            if event.type == pygame.MOUSEBUTTONDOWN: #if the mouse has been pressed
                if event.button == 1: #the left mouse button
                    if rects[mix].collidepoint(event.pos): #and the mouse is on top of a rect 
                        active_ingredient = True #then it needs to be dragged into the bowl
            if event.type == pygame.MOUSEBUTTONUP: #if the mouse is released
                if event.button == 1:
                    active_ingredient = False #we are no longer dragging into the bowl
            if event.type == pygame.MOUSEMOTION: #if the mouse is moving
                if active_ingredient: #and we are dragging into the bowl
                    rects[mix].move_ip(event.rel) #move the rect with the mouse
        
        globalvariables.WIN.blit(gameBg_image, bgPosition) #displays the background image
        globalvariables.WIN.blit(clock_image, (20, 10)) #displays the clock
        timer_box.drawBox()
        counting_time = pygame.time.get_ticks() - start_time
        timer_text.changeText(str( int(counting_time/1000) ).zfill(2)) #displays the time and the box behind it
        if value == "Mixing 1": #if the node is at "Mixing 1"
            ingredient_box.drawBox() #draw the ingredient box to show the user what is being used
            ingredients[3].changePosition(305, 103)
            ingredien2_box.drawBox()
            ingredients[4].changePosition(705, 103)
            start_time, counting_time = seasoning(True, beefMince_image, 300, 365, 300, 200, "herbs", colours, start_time, counting_time, timer_text, timer_box, themeSelected)
            #call the seasoning function to season the meat, which the image for has been passed through 
            value, stack, visitedNodes = treeTraversal("burger", stack, visitedNodes) #go to the next node

        if value == "Mixing 2" or value == "Mixing 3" or value == "Mixing 4" or value == "Mixing 5": #if the node is any of these values (the nodes that involve the bowl)
            globalvariables.WIN.blit(mixingBowl_image, (575, 265)) #display the bowl

        if value == "Mixing 2" or value == "Mixing 3" or value == "Mixing 4": #if the node is any of the values that involve putting the ingredient into the bowl
            if active_ingredient: #if this is true, it means we are adding ingredients into the bowl
                mx, my = pygame.mouse.get_pos() #gets the position of the mouse
                if 575 <= mx - 120 <= (575 + bowl_width) and 265 + 20 <= my - 120 <= (265 + bowl_height): #if the mouse is on the bowl

                    if value == "Mixing 2" or value == "Mixing 3": #if the node is these values
                        value, stack, visitedNodes = treeTraversal("burger", stack, visitedNodes) #traverse to next node
                        mix = mix + 1 #increment mix
                    else: #if not
                        value, stack, visitedNodes = treeTraversal("burger", stack, visitedNodes) #don't increment mix but traverse to next node

                    active_ingredient = False

        if value == "Mixing 2": #if at this node
            instruction_box.drawBox()
            drag1instruction_text.drawText()
            globalvariables.WIN.blit(beefMince_image, mince_rect) #then we are dragging the meat
        if value == "Mixing 3": #if at this node
            ingredient_box.drawBox()
            ingredients[5].changePosition(305, 103)
            globalvariables.WIN.blit(egg1_image, egg_rect) #then we're dragging the egg
        if value == "Mixing 4": #if at thise node
            globalvariables.WIN.blit(dicedonion2_image, onion_rect) #then we're dragging the onion
        if value == "Mixing 5": #if at this node
            start_time, counting_time, mixingScore = mixingBowl(True, mixingBowl_image, 300, 265, 300, 300, colours, start_time, counting_time, timer_text, timer_box, themeSelected)
            #we are no longer dragging, but instead mixing the ingredients using this subroutine
            mixing = False #mixing stage ends

        clock.tick(globalvariables.FPS)
        pygame.display.update()
    

    if value == "Mixing 5": #if at the end of the mixing stage
        if 0 <= int(counting_time / 1000) <= 60: #if the time is between 0 and 60 seconds
            burgerScore.append(100 + mixingScore) #the score is 100, but will be affected by the mixing score
        elif 61 <= int(counting_time / 1000) <= 90: #if the time is between 61 and 90 seconds
            burgerScore.append(70 + mixingScore) #the score is 70, but will be affected by the mixing score
        elif int(counting_time / 1000) >= 91: #if the time is more than 91 seconds
            burgerScore.append(50 + mixingScore) #the score is 50, but will be affected by the mixing score
        score = score + burgerScore[1] #adds to total score

    nextPatty = True 
    shaped = 0
    flippingScore = 0

    while shaping:

        for event in pygame.event.get(): #allows user to quit the window
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                burgerPattyPressed = burgerPatty_button.checkPressed(pygame.mouse.get_pos())
                if burgerPattyPressed: #if the shaped patty is pressed
                    nextPatty = True #move onto the next patty
                    shaped = shaped + 1
        
        globalvariables.WIN.blit(gameBg_image, bgPosition) #displays background image
        globalvariables.WIN.blit(clock_image, (20, 10))
        timer_box.drawBox()
        counting_time = pygame.time.get_ticks() - start_time
        timer_text.changeText(str( int(counting_time/1000) ).zfill(2)) #displays time and clock
        if value == "Shaping 1": #if the node is "Shaping 1"
            if nextPatty: #if this is true
                instruction_box.drawBox()
                flipinstruction_text.drawText() #display the instruction
                start_time, counting_time, flippingScore = flip(True, 400, 10, [beefMince_image], [(150, 350)], colours, start_time, counting_time, timer_text, timer_box, flippingScore, themeSelected)
                #calls the flip subroutine to mimic pressed down on the patty to flatten it
                nextPatty = False #sets to false so that the user moves on when..
            if nextPatty == False:
                instruction_box.drawBox() #display the instruction
                clickinstruction_text.drawText()
                burgerPatty_button.draw() #the user can shape the next patty once they click the patty that they've already shaped
            if shaped == 4: #total of 4 patties
                shaping = False #ends shaping stage
        
        clock.tick(globalvariables.FPS)
        pygame.display.update()

    if value == "Shaping 1":
        if 0 <= int(counting_time / 1000) <= 30: #if the time is between 0 and 30 seconds
            burgerScore.append(100 + flippingScore) #score is 100 and then changed depending on what the flipping score was
        elif 31 <= int(counting_time / 1000) <= 60: #if the time is between 31 and 60 seconds
            burgerScore.append(70 + flippingScore)  #score is 70 and then changed depending on what the flipping score was
        elif int(counting_time / 1000) >= 60: #if the time is more than 60 seconds
            burgerScore.append(50 + flippingScore)  #score is 500 and then changed depending on what the flipping score was
        score = score + burgerScore[2] #added to total score for burger
    
    grilled = 0
    
    while grilling:
        for event in pygame.event.get(): #allows user to quit the window
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                burgerPattyPressed = burgerPatty_button.checkPressed(pygame.mouse.get_pos())
                if burgerPattyPressed: #if the patty is pressed
                    nextPatty = True #move onto the next patty
                cookedPattyPressed = cookedPatty_button.checkPressed(pygame.mouse.get_pos())
                if cookedPattyPressed: 
                    nextPatty = True
                    grilled = grilled + 1
        
        globalvariables.WIN.blit(gameBg_image, bgPosition)
        globalvariables.WIN.blit(clock_image, (20, 10))
        timer_box.drawBox()
        counting_time = pygame.time.get_ticks() - start_time
        timer_text.changeText(str( int(counting_time/1000) ).zfill(2)) #displays time, clock, background image
        if value == "Grilling 1": #if the node is "Grilling 1"
            if nextPatty: #and we are on the next patty
                start_time, counting_time, flippingScore = flip(True, 700, 10, [cooker_image, fryingPan_image, burgerPatty_image], [(180, 190), (-50, 60), (250, 300)], colours, start_time, counting_time, timer_text, timer_box, flippingScore, themeSelected)
                #call flipping function to flip the patties
                nextPatty = False
            if nextPatty == False: #if we are not on the next patty
                globalvariables.WIN.blit(cooker_image, (180, 190))
                globalvariables.WIN.blit(fryingPan_image, (-50, 60))
                cookedPatty_button.draw() #draw the cooked patty
            if grilled == 4: #once this has been done 4 times
                grilling = False #end grilling stage
        
        clock.tick(globalvariables.FPS)
        pygame.display.update()

    if value == "Grilling 1":
        if 0 <= int(counting_time / 1000) <= 30: #if the time is between 0 and 30 seconds
            burgerScore.append(100 + flippingScore) #score is 100 and then changed depending on what the flipping score was
        elif 31 <= int(counting_time / 1000) <= 60: #if the time is between 31 and 60 seconds
            burgerScore.append(70 + flippingScore)  #score is 70 and then changed depending on what the flipping score was
        elif int(counting_time / 1000) >= 60: #if the time is more than 60 seconds
            burgerScore.append(50 + flippingScore)  #score is 500 and then changed depending on what the flipping score was
        score = score + burgerScore[3] #added to total score for burger
    
    while assembly:

        for event in pygame.event.get(): #allows user to quit the window
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break
                
        if value == "Assembly 1": #if the node is on the assembly stage
            start_time, counting_time = recipeAssembly(True, "burger", colours, start_time, counting_time, timer_text, timer_box, themeSelected)
            #call the function to assemble the burger
            assembly = False #once this is complete then the assembly stage is done
        clock.tick(globalvariables.FPS)
        pygame.display.update()

    if value == "Assembly 1":
        if 0 <= int(counting_time / 1000) <= 90: #if time is between 0 and 90 seconds
            burgerScore.append(100) #score is 100
        elif 91 <= int(counting_time / 1000) <= 120:#if time is between 91 and 120 seconds
            burgerScore.append(70) #score is 70
        elif int(counting_time / 1000) >= 120: #if time is more than 120 seconds
            burgerScore.append(50) #score is 150
        score = ((score + burgerScore[4]) // 5) #add to total score and calculate the average score
        startingScreen = False #reached the end of burger game

    return value, stack, visitedNodes, burgerScore, score, startingScreen

def cakeGame(value, stack, visitedNodes, score, cakeScore, colours, ingredients, startingScreen, themeSelected):
    mixing = False
    baking = False
    frosting = False
    decorating = False

    if value == "Mixing": #depending on what node has been traversed, the loop for that step in the recipe will begin
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

    #images
    if themeSelected == "theme1":
        gameBg_image = game1Bg_image #background image will depend on the theme
    elif themeSelected == "theme2":
        gameBg_image = game2Bg_image
    
    ingredient_box = classes.Box(300, 100, 40, 350, colours[2], False) 
    instruction_box = classes.Box(0, 550, 40, 380, colours[2], False)

    timer_text = classes.Text(152, 47, "00.00", (255, 255, 255), 24)
    timer_box = classes.Box(150, 45, 30, 60, colours[5], False)
    start_time = pygame.time.get_ticks()
    clock = pygame.time.Clock()
    counting_time = 0
    
    #rects for mixing stage
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
    egg1_rect = egg1_image.get_rect()
    egg1_rect.center = (200, 500)
    egg2_rect = egg1_image.get_rect()
    egg2_rect.center = (200, 500)
    
    mixing_rects = [flour_rect, cake_flour_rect, sugar_rect, shaker_rect, bakingpowder_rect, bakingsoda_rect, butter_rect, egg1_rect, egg2_rect, yogurt_rect, milk_rect, vanilla_extract_rect]
    mix = 0

    while mixing: 
        for event in pygame.event.get(): #allows user to quit the window
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break
            if event.type == pygame.MOUSEBUTTONDOWN: #if mouse has been pressed
                if event.button == 1:
                    if mixing_rects[mix].collidepoint(event.pos): #check if the mouse is on the rect
                        active_ingredient = True #if it is, then the ingredient is active and needs to be dragged
            if event.type == pygame.MOUSEBUTTONUP: #if the mouse is released
                if event.button == 1:
                    active_ingredient = False #ingredient is no longer active, no longer being dragged
            if event.type == pygame.MOUSEMOTION: #if the mouse is moving..
                if active_ingredient: #and the ingredient is being dragged
                    mixing_rects[mix].move_ip(event.rel) #then move the rect with the mouse

        globalvariables.WIN.blit(gameBg_image, bgPosition)
        globalvariables.WIN.blit(clock_image, (20, 10))
        timer_box.drawBox()
        counting_time = pygame.time.get_ticks() - start_time
        timer_text.changeText(str( int(counting_time/1000) ).zfill(2)) #display time
        if value == "Mixing 1": #if on this node
            if mix <= 13: #if mix is less than or equal to 13 (the number of ingredients to be added in the bowl)
                globalvariables.WIN.blit(mixingBowl_image, (575, 265)) #display the bowl
                if active_ingredient: #if an ingredient is being dragged
                    mx, my = pygame.mouse.get_pos() #get the position of the mouse
                    if 575 <= mx - 120 <= (575 + bowl_width) and 265 + 20 <= my - 120 <= (265 + bowl_height): #if the mouse is on the bowl
                        mix = mix + 1 #increment mix
                        active_ingredient = False #ingredient no longer being dragged
            if mix == 0:
                instruction_box.drawBox() #display the instruction
                drag1instruction_text.drawText()
                ingredient_box.drawBox() #display the name and measurement of the ingredient
                ingredients[2].changePosition(305, 103)
                globalvariables.WIN.blit(flour_image, flour_rect) #flour
            if mix == 1:#if mix is 1, then cake flour
                ingredient_box.drawBox()
                ingredients[1].changePosition(305, 103)
                globalvariables.WIN.blit(cake_flour_image, cake_flour_rect)
            if mix == 2: #if mix is 2, then sugar
                ingredient_box.drawBox()
                ingredients[3].changePosition(305, 103)
                globalvariables.WIN.blit(sugar_image, sugar_rect)
            if mix == 3: #if mix is 3, then salt
                ingredient_box.drawBox()
                ingredients[6].changePosition(305, 103)
                globalvariables.WIN.blit(shaker_image, shaker_rect)
            if mix == 4: #if mix is 4, then baking powder
                ingredient_box.drawBox()
                ingredients[4].changePosition(305, 103)
                globalvariables.WIN.blit(bakingpowder_image, bakingpowder_rect)
            if mix == 5: #if mix is 5, then baking soda
                ingredient_box.drawBox()
                ingredients[5].changePosition(305, 103)
                globalvariables.WIN.blit(bakingsoda_image, bakingsoda_rect)
            if mix == 6: #if mix is 6, then butter
                ingredient_box.drawBox()
                ingredients[7].changePosition(305, 103)
                globalvariables.WIN.blit(butter_image, butter_rect)
            if mix == 7: #if mix is 7, then egg
                ingredient_box.drawBox()
                ingredients[8].changePosition(305, 103)
                globalvariables.WIN.blit(egg1_image, egg1_rect)
            if mix == 8: #if mix is 8, then egg
                globalvariables.WIN.blit(egg1_image, egg2_rect)
            if mix == 9: #if mix is 9, then yogurt
                ingredient_box.drawBox()
                ingredients[9].changePosition(305, 103)
                globalvariables.WIN.blit(yogurt_image, yogurt_rect)
            if mix == 10: #if mix is 10, then milk
                ingredient_box.drawBox()
                ingredients[11].changePosition(305, 103)
                globalvariables.WIN.blit(milk_image, milk_rect)
            if mix == 11: #if mix is 11, then vanilla extract
                ingredient_box.drawBox()
                ingredients[12].changePosition(305, 103)
                globalvariables.WIN.blit(vanilla_extract_image, vanilla_extract_rect)
            if mix == 12: #if mix is 12, then mix 
                instruction_box.drawBox()
                mixinstruction_text.drawText()
                start_time, counting_time, mixingScore = mixingBowl(True, mixingBowl_image, 350, 225, 300, 300, colours, start_time, counting_time, timer_text, timer_box, themeSelected)
                mixing = False

        clock.tick(globalvariables.FPS)
        pygame.display.update()
    
    if value == "Mixing 1":
        if 0 <= int(counting_time / 1000) <= 60: #if time is between 0 and 60 seconds
            cakeScore.append(100 + mixingScore) #score of 100 that is affected by mixing score
        elif 61 <= int(counting_time / 1000) <= 90: #if time is between 61 and 90 seconds
            cakeScore.append(70 + mixingScore) #score of 70 that is affected by mixing score
        elif int(counting_time / 1000) >= 90: #if time is more than 90 seconds
            cakeScore.append(50 + mixingScore) #score of 50 that is affected by mixing score
        score = score + cakeScore[0] #add to total score for cake minigame

    caketin_button = classes.ImageButton(300, 265, caketin_image, 1)
    oven_button = classes.ImageButton(530, 200, oven_image, 1)

    active_ingredient = False
    caketin_filled1_rect = caketin_filled_image.get_rect()
    caketin_filled2_rect = caketin_filled_image.get_rect()
    caketin_filled1_rect.center = (270, 450)
    caketin_filled2_rect.center = (270, 450)

    oven_rects = [caketin_filled1_rect, caketin_filled2_rect]

    oven = 0
    filling = 0
    bake = 0

    while baking:
        for event in pygame.event.get(): #allows user to quit the window
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                caketinPressed = caketin_button.checkPressed(pygame.mouse.get_pos())
                if caketinPressed: #if the caketin has been pressed
                    filling = filling + 1 #filling is incremented
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
        globalvariables.WIN.blit(clock_image, (20, 10))
        timer_box.drawBox()
        counting_time = pygame.time.get_ticks() - start_time
        timer_text.changeText(str( int(counting_time/1000) ).zfill(2)) #displays time
        
        if value == "Baking 1": #if node at "Baking 1"
            instruction_box.drawBox() #display the instructions
            clickinstruction_text.drawText()
            caketin_button.draw() #draw the button for the cake tin, and when it has been pressed..
            if filling == 1:
                start_time, counting_time, bakingScore = fill(True, cakebatter_colour, colours, start_time, counting_time, timer_text, timer_box, themeSelected)
                #call function for this stage in the recipe
                filling = filling + 1
            if filling == 2:
                instruction_box.drawBox() #display the instructions
                clickinstruction_text.drawText()
                caketin_button.draw() #the cake tin button will appear and will have to be clicked
            if filling == 3: #once filling is incremented
                start_time, counting_time, bakingScore = fill(True, cakebatter_colour, colours, start_time, counting_time, timer_text, timer_box, themeSelected)
                value, stack, visitedNodes = treeTraversal("cake", stack, visitedNodes)
                #fill the pan again and traverse the tree
                bake = bake + 1
        if value == "Baking 2" : #when the node is "Baking 2"
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
                        active_ingredient = False #allows the cake tins to be dragged into the oven

            if bake == 1:
                instruction_box.drawBox()
                drag1instruction_text.drawText()
                globalvariables.WIN.blit(caketin_filled_image, caketin_filled1_rect) #the first cake tin
            if bake == 2:
                globalvariables.WIN.blit(caketin_filled_image, caketin_filled2_rect) #the second cake tin
            if bake == 3:
                oven_button.setActive()
                instruction_box.drawBox() #display the instructions
                clickinstruction_text.drawText()
                oven_button.draw() #click the oven to continue

        clock.tick(globalvariables.FPS)
        pygame.display.update()

    if value == "Baking 2": #if the node is at the end of the baking step
        if 0 <= int(counting_time / 1000) <= 30: #when the time is between 0 and 30 seconds
            cakeScore.append(100 + bakingScore) #score is 100, and affected by baking score
        elif 31 <= int(counting_time / 1000) <= 60: #when the time is between 31 and 60 seconds
            cakeScore.append(70 + bakingScore) #score is 70, and affected by baking score
        elif int(counting_time / 1000) >= 90: #when the time is more than 90 seconds
            cakeScore.append(50 + bakingScore) #score is 500, and affected by baking score
        score = score + cakeScore[1] #add to total score
    
    #the rects for the frosting stage 
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
            globalvariables.WIN.blit(clock_image, (20, 10))
            timer_box.drawBox()
            counting_time = pygame.time.get_ticks() - start_time
            timer_text.changeText(str( int(counting_time/1000) ).zfill(2)) #time is displayed
            if value == "Frosting 1":
                if mix <= 4:
                    globalvariables.WIN.blit(mixingBowl_image, (575, 265))
                    if active_ingredient:
                        mx, my = pygame.mouse.get_pos()
                        if 575 <= mx - 120 <= (575 + bowl_width) and 265 + 20 <= my - 120 <= (265 + bowl_height):
                            mix = mix + 1
                            active_ingredient = False #the ingredients are dragged 
                if mix == 0:
                    ingredient_box.drawBox()
                    ingredients[14].changePosition(305, 103)
                    globalvariables.WIN.blit(butter_image, butter_rect)
                if mix == 1:
                    ingredient_box.drawBox()
                    ingredients[15].changePosition(305, 103)
                    globalvariables.WIN.blit(sugar_image, sugar_rect)
                if mix == 2:
                    ingredient_box.drawBox()
                    ingredients[17].changePosition(305, 103)
                    globalvariables.WIN.blit(vanilla_extract_image, vanilla_extract_rect)
                if mix == 3:
                    ingredient_box.drawBox()
                    ingredients[18].changePosition(305, 103)
                    globalvariables.WIN.blit(milk_image, milk_rect)
                if mix == 4:
                    start_time, counting_time, frostingScore = mixingBowl(True, mixingBowl_image, 350, 225, 300, 300, colours, start_time, counting_time, timer_text, timer_box, themeSelected)
                    frosting = False

            clock.tick(globalvariables.FPS)
            pygame.display.update()
    
    if value == "Frosting 1":
        if 0 <= int(counting_time / 1000) <= 30: #if time is between 0 and 30 seconds
            cakeScore.append(100 + frostingScore) #score is 100 that is affected by the frosting score 
        elif 31 <= int(counting_time / 1000) <= 60:#if time is between 31 and 60 seconds
            cakeScore.append(70 + frostingScore) #score is 70 that is affected by the frosting score 
        elif int(counting_time / 1000) >= 90:#if time is more than 90 seconds
            cakeScore.append(50 + frostingScore) #score is 50 that is affected by the frosting score 
        score = score + cakeScore[2] #add to total score

    while decorating:
        for event in pygame.event.get(): #allows user to quit the window
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break
        
        if value == "Decoration 1":
            start_time, counting_time = recipeAssembly(True, "cake", colours, start_time, counting_time, timer_text, timer_box, themeSelected)
            #the assembly subroutine is called to assemble 
            value, stack, visitedNodes = treeTraversal("cake", stack, visitedNodes)
            #the tree is then traversed
        if value == "Decoration 2":
            globalvariables.WIN.blit(gameBg_image, bgPosition)
            globalvariables.WIN.blit(clock_image, (20, 10)) 
            timer_box.drawBox()
            counting_time = pygame.time.get_ticks() - start_time
            timer_text.changeText(str( int(counting_time/1000) ).zfill(2)) #the time is displayed
            globalvariables.WIN.blit(assembledcake_image, (300, 200)) #the assembled cake is displayed
            instruction_box.drawBox()
            draw2instruction_text.drawText()
            start_time, counting_time = draw(True, 401.0, 656.0, 233.0, 521.0, 565.0, 518.0, 399.0, 329.0, 10, 10.0, start_time, counting_time, timer_text, timer_box, colours)
            #which is then "frosted" using the draw subroutine
            value, stack, visitedNodes = treeTraversal("cake", stack, visitedNodes)
            #the tree is traversed
        if value == "Decoration 3":
            globalvariables.WIN.blit(gameBg_image, bgPosition)
            globalvariables.WIN.blit(clock_image, (20, 10))
            timer_box.drawBox()
            counting_time = pygame.time.get_ticks() - start_time
            timer_text.changeText(str( int(counting_time/1000) ).zfill(2)) #time is displayed again
            globalvariables.WIN.blit(frostedcake_image, (300, 200))
            start_time, counting_time = seasoning(True, frostedcake_image, 300, 200, 400, 400, "sprinkles", colours, start_time, counting_time, timer_text, timer_box, themeSelected)
            #the sprinkles are added using the seasoning subroutine
            decorating = False #the step ends


        clock.tick(globalvariables.FPS)
        pygame.display.update()

    if value == "Decoration 3": #if the end of the decoration step has been reached
        if 0 <= int(counting_time / 1000) <= 60: #if time is between 0 and 60 seconds
            cakeScore.append(100) #add score of 100
        elif 61 <= int(counting_time / 1000) <= 90: #if time is between 61 and 90 seconds
            cakeScore.append(70) #add score of 70
        elif int(counting_time / 1000) >= 90: #if time is more than 90 seconds
            cakeScore.append(50) #add score of 50
        score = (score + cakeScore[3]) // 4 #add to total score and find average
        startingScreen = False #set to false so score screen will appear

    return value, stack, visitedNodes, cakeScore, score, startingScreen

def sushiGame(value, stack, visitedNodes, score, sushiScore, colours, ingredients, startingScreen, themeSelected):

    cooking = False
    assembly = False
    cutting = False

    if value == "Cooking": #if on this node
        cooking = True #allow this loop to run
        value, stack, visitedNodes = treeTraversal("sushi", stack, visitedNodes)
        #traverse the tree to go to the next node
    elif value == "Assembly":
        assembly = True
        value, stack, visitedNodes = treeTraversal("sushi", stack, visitedNodes)
    elif value == "Cutting":
        cutting = True
        value, stack, visitedNodes = treeTraversal("sushi", stack, visitedNodes)

    #images
    if themeSelected == "theme1":
        gameBg_image = game1Bg_image #displays correct background image based on theme
    elif themeSelected == "theme2":
        gameBg_image = game2Bg_image

    #box objects
    ingredient_box = classes.Box(300, 100, 40, 350, colours[2], False)
    instruction_box = classes.Box(0, 550, 40, 400, colours[2], False)

    #objects and variables for time
    timer_text = classes.Text(152, 47, "00.00", (255, 255, 255), 24)
    timer_box = classes.Box(150, 45, 30, 60, colours[5], False)
    start_time = pygame.time.get_ticks()
    clock = pygame.time.Clock()
    counting_time = 0

    cook = 0

    back_button = classes.Button(770, 500, 70, 100, colours[3], False)
    back_button.setUnactive()
    back_text = classes.Text(785, 503, "-->", (255, 255, 255), 50)

    active_ingredient = False

    #rects for cooking step
    rice_rect = rice_image.get_rect()
    rice_rect.center = (250, 450)
    sushiseasoning_rect = sushiseasoning_image.get_rect()
    sushiseasoning_rect.center = (250, 450)
    rects = [rice_rect, sushiseasoning_rect]

    while cooking:
        for event in pygame.event.get(): #allows user to quit the window
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break
        
            if event.type == pygame.MOUSEBUTTONDOWN: #if the mouse button is pressed down
                if event.button == 1:
                    if rects[cook].collidepoint(event.pos): #if the mouse is on top of a rect
                        active_ingredient = True #then the ingredient is being dragged
            if event.type == pygame.MOUSEBUTTONUP: #if the mouse is released
                if event.button == 1:
                    active_ingredient = False #then the ingredient is no longer being dragged
            if event.type == pygame.MOUSEMOTION: #if the mouse is moving
                if active_ingredient:#and an ingredient is being dragged
                    rects[cook].move_ip(event.rel) #move the ingredient with the mouse

        globalvariables.WIN.blit(gameBg_image, bgPosition)
        globalvariables.WIN.blit(clock_image, (20, 10))
        timer_box.drawBox()
        counting_time = pygame.time.get_ticks() - start_time
        timer_text.changeText(str( int(counting_time/1000) ).zfill(2)) #displays the time
        if value == "Cooking 1": #if at this node
            if cook <= 2: #if moving the ingredients into the rice cooker is still occuring
                globalvariables.WIN.blit(ricecooker_image, (525, 235)) #display the rice cooker
                if active_ingredient: #if an ingredient is being dragged
                    mx, my = pygame.mouse.get_pos() #get mouse position
                    if 525 <= mx - 190 <= (525 + ricecooker_width) and 235 + 20 <= my - 190 <= (235 + ricecooker_height): #check if its on the rice cooker
                        cook = cook + 1 #if it is then increment cook (allows the next ingredient to be added in)
                        active_ingredient = False #and set the current ingredient to no longer being dragged
            if cook == 0: #the first ingredient is rice
                instruction_box.drawBox()
                drag3instruction_text.drawText()
                ingredient_box.drawBox()
                ingredients[4].changePosition(335, 103)
                globalvariables.WIN.blit(rice_image, rice_rect)
            if cook == 1: #the second ingredient is the sushi seasoning
                ingredient_box.drawBox()
                ingredients[2].changePosition(365, 103)
                globalvariables.WIN.blit(sushiseasoning_image, sushiseasoning_rect)
            if cook == 2: #once they've been added, traverse the tree to go onto the next node
                value, stack, visitedNodes = treeTraversal("sushi", stack, visitedNodes)
        if value == "Cooking 2": #at the next node..
            instruction_box.drawBox()
            fillinstruction_text.drawText() 
            start_time, counting_time, cookingScore = fill(True, water_colour, colours, start_time, counting_time, timer_text, timer_box, themeSelected)
            #fill subroutine called to mimic filling the rice cooker with water
            cooking = False #once this has been completed, the cooking step is finished

        clock.tick(globalvariables.FPS)
        pygame.display.update()
    
    if value == "Cooking 2": #at the end of the cooking step
        if 0 <= int(counting_time / 1000) <= 20: #if the time is between 0 and 20 seconds
            sushiScore.append(100 + cookingScore) #score of 100, affected by cooking score
        elif 21 <= int(counting_time / 1000) <= 30: #if the time is between 21 and 30 seconds
            sushiScore.append(70 + cookingScore) #score of 70, affected by cooking score
        elif int(counting_time / 1000) >= 30: #if the time is more than 30 seconds
            sushiScore.append(50 + cookingScore) #score of 50, affected by cooking score
        score = score + sushiScore[0] # add to total score

    cut = 0
    assemble = 0
    addIngredient = 0

    #rects for assembly step
    slicedcucumber1_rect = slicedcucumber_image.get_rect()
    slicedcucumber1_rect.center = (870, 400)
    slicedcucumber2_rect = slicedcucumber_image.get_rect()
    slicedcucumber2_rect.center = (870, 400)
    slicedcucumber3_rect = slicedcucumber_image.get_rect()
    slicedcucumber3_rect.center = (870, 400)

    slicedavocado1_rect = slicedavocado_image.get_rect()
    slicedavocado1_rect.center = (870, 400)
    slicedavocado2_rect = slicedavocado_image.get_rect()
    slicedavocado2_rect.center = (870, 400)
    slicedavocado3_rect = slicedavocado_image.get_rect()
    slicedavocado3_rect.center = (870, 400)

    slicedsalmon1_rect = slicedsalmon_image.get_rect()
    slicedsalmon1_rect.center = (870, 400)
    slicedsalmon2_rect = slicedsalmon_image.get_rect()
    slicedsalmon2_rect.center = (870, 400)
    slicedsalmon3_rect = slicedsalmon_image.get_rect()
    slicedsalmon3_rect.center = (870, 400)

    ingredient_rects = [slicedcucumber1_rect, slicedcucumber2_rect, slicedcucumber3_rect, 
                        slicedavocado1_rect, slicedavocado2_rect, slicedavocado3_rect,
                        slicedsalmon1_rect, slicedsalmon2_rect, slicedsalmon3_rect]

    #buttons
    cucumber2_button = classes.ImageButton(350, 260, cucumbers[1], 0.7)
    cucumber5_button = classes.ImageButton(350, 260, cucumbers[4], 0.7)
    avocado1_button = classes.ImageButton(340, 215, avocados[0], 1)
    avocado3_button = classes.ImageButton(340, 215, avocados[2], 1)
    avocado7_button = classes.ImageButton(340, 215, avocados[6], 1)
    salmon3_button = classes.ImageButton(330, 200, salmon3_image, 1)

    while assembly:
        for event in pygame.event.get(): #allows user to quit the window
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break
        
            if event.type == pygame.MOUSEBUTTONDOWN:
                cucumber2Pressed = cucumber2_button.checkPressed(pygame.mouse.get_pos()) #checks if the cucumber has been pressed
                cucumber2Active = cucumber2_button.getActive()
                if cucumber2Pressed == True and cucumber2Active == True:
                    cut = cut + 1 #increments, so the next stage in assembly can occur
                    cucumber2_button.setUnactive() #can't be accidently pressed 
                cucumber5Pressed = cucumber5_button.checkPressed(pygame.mouse.get_pos())
                cucumber5Active = cucumber5_button.getActive()
                if cucumber5Pressed == True and cucumber5Active == True: #checks if cucumber has been pressded
                    cut = cut + 1 #increments cut if cucumber pressed
                    cucumber5_button.setUnactive() #sets to unactive so can't be accidently pressed
                    value, stack, visitedNodes = treeTraversal("sushi", stack, visitedNodes)
                avocado1Pressed = avocado1_button.checkPressed(pygame.mouse.get_pos())
                avocado1Active = avocado1_button.getActive()
                if avocado1Pressed == True and avocado1Active == True:
                    cut = cut + 1
                    avocado1_button.setUnactive()
                avocado3Pressed = avocado3_button.checkPressed(pygame.mouse.get_pos())
                avocado3Active = avocado3_button.getActive()
                if avocado3Pressed == True and avocado3Active == True:
                    cut = cut + 1
                    avocado3_button.setUnactive()
                avocado7Pressed = avocado7_button.checkPressed(pygame.mouse.get_pos())
                avocado7Active = avocado7_button.getActive()
                if avocado7Pressed == True and avocado7Active == True:
                    cut = cut + 1
                    avocado7_button.setUnactive()
                    value, stack, visitedNodes = treeTraversal("sushi", stack, visitedNodes)
                salmon3Pressed = salmon3_button.checkPressed(pygame.mouse.get_pos())
                salmon3Active = salmon3_button.getActive()
                if salmon3Pressed == True and salmon3Active == True:
                    assemble = assemble + 1
                    salmon3_button.setUnactive()
                    value, stack, visitedNodes = treeTraversal("sushi", stack, visitedNodes)
                backPressed = back_button.checkPressed(pygame.mouse.get_pos())
                backActive = back_button.getActive()
                if backPressed == True and backActive == False: #if the back button has been pressed
                    assembly = False #the assembly step in the recipe is finished
                    back_button.setActive()
                
                if event.button == 1 and backPressed == False:
                    if ingredient_rects[addIngredient].collidepoint(event.pos):
                        active_ingredient = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    active_ingredient = False
            if event.type == pygame.MOUSEMOTION:
                if active_ingredient:
                    ingredient_rects[addIngredient].move_ip(event.rel)
                
        
        globalvariables.WIN.blit(gameBg_image, bgPosition)
        globalvariables.WIN.blit(clock_image, (20, 10))
        timer_box.drawBox()
        counting_time = pygame.time.get_ticks() - start_time
        timer_text.changeText(str( int(counting_time/1000) ).zfill(2)) #displays the time

        if value == "Assembly 1": #if at the first node in the assembly step
            globalvariables.WIN.blit(cuttingBoard_image, (100, 170)) #display the cutting board
            if cut == 0: #if cut is 0
                ingredient_box.drawBox()
                ingredients[6].changePosition(385, 103) #draw the ingredient box which says what the ingredient is
                globalvariables.WIN.blit(cucumbers[0], (350, 280)) #display the first cucumber
                instruction_box.drawBox()
                draw1instruction_text.drawText() #display the instructions
                globalvariables.WIN.blit(pygame.transform.scale(arrow2_image, (300, 200)), (340, 250)) #draw the arrow to show where the user should cut
                start_time, counting_time = draw(True, 485.0, 407.0, 532.0, 454.0, 491.0, 493.0, 256.0, 449.0,  5, 5.0, start_time, counting_time, timer_text, timer_box, colours)
                #call the draw subroutine
                cut = cut + 1
            elif cut == 1:
                instruction_box.drawBox() #display the instructions
                clickinstruction_text.drawText()
                cucumber2_button.draw()
                cucumber2_button.setActive()
            elif cut == 2:
                globalvariables.WIN.blit(cucumbers[2], (350, 280))
                globalvariables.WIN.blit(pygame.transform.scale(arrow2_image, (300, 200)), (340, 270))
                #draws cucumber and arrow
                start_time, counting_time = draw(True, 529.0, 471.0, 487.0, 513.0, 491.0, 426.0, 259.0, 474.0, 5, 5.0, start_time, counting_time, timer_text, timer_box, colours)
                #calls draw subroutine so the arrow can be traced
                cut = cut + 1 #once this is complete, cut is incremented
            elif cut == 3:
                globalvariables.WIN.blit(cucumbers[3], (350, 280)) 
                globalvariables.WIN.blit(pygame.transform.scale(arrow2_image, (300, 200)), (340, 290))
                #draws the cucumber and arrow
                start_time, counting_time = draw(True, 262.0, 489.0, 488.0, 535.0, 485.0, 447.0, 527.0, 493.0, 5, 5.0,  start_time, counting_time, timer_text, timer_box, colours)
                #calls draw subroutine so the arrow can be traced
                cut = cut + 1 #once this is complete, cut is incremented
            elif cut == 4:
                instruction_box.drawBox() #display the instructions
                clickinstruction_text.drawText()
                cucumber5_button.draw() #button drawn so the cucumber can be clicked
                cucumber5_button.setActive()
        if value == "Assembly 2": #moves onto cutting the avocado
            globalvariables.WIN.blit(cuttingBoard_image, (100, 170))
            if cut == 5:
                ingredient_box.drawBox()
                ingredients[7].changePosition(385, 103)
                instruction_box.drawBox() #display the instructions
                clickinstruction_text.drawText()
                avocado1_button.draw()
                avocado1_button.setActive()
            elif cut == 6:
                globalvariables.WIN.blit(avocados[1], (360, 210))
                globalvariables.WIN.blit(pygame.transform.scale(arrow3_image, (200, 300)), (395, 220))
                start_time, counting_time = draw(True, 352.0, 570.0, 393.0, 609.0, 441.0, 569.0, 390.0, 337.0, 5, 5.0,  start_time, counting_time, timer_text, timer_box, colours)
                cut = cut + 1
            elif cut == 7:
                instruction_box.drawBox() #display the instructions
                clickinstruction_text.drawText()
                avocado3_button.draw()
                avocado3_button.setActive()
            elif cut == 8:
                globalvariables.WIN.blit(avocados[3], (330, 220))
                globalvariables.WIN.blit(pygame.transform.scale(arrow3_image, (200, 300)), (325, 230))
                start_time, counting_time = draw(True, 283.0, 583.0, 329.0, 621.0, 370.0, 579.0, 321.0, 348.0, 5, 5.0,  start_time, counting_time, timer_text, timer_box, colours)
                cut = cut + 1
            elif cut == 9:
                globalvariables.WIN.blit(avocados[4], (330, 220))
                globalvariables.WIN.blit(pygame.transform.scale(arrow3_image, (200, 300)), (315, 230))
                start_time, counting_time = draw(True, 314.0, 347.0, 277.0, 581.0, 316.0, 619.0, 363.0, 575.0, 5, 5.0,  start_time, counting_time, timer_text, timer_box, colours)
                cut = cut + 1
            elif cut == 10:
                globalvariables.WIN.blit(avocados[5], (330, 220))
                globalvariables.WIN.blit(pygame.transform.scale(arrow3_image, (200, 300)), (285, 230))
                start_time, counting_time = draw(True, 281.0, 347.0, 243.0, 580.0, 285.0, 619.0, 329.0, 578.0, 5, 5.0,  start_time, counting_time, timer_text, timer_box, colours)
                cut = cut + 1
            elif cut == 11:
                instruction_box.drawBox() #display the instructions
                clickinstruction_text.drawText()
                avocado7_button.draw()
                avocado7_button.setActive()
        if value == "Assembly 3":
            globalvariables.WIN.blit(cuttingBoard_image, (100, 170))
            if cut == 12:
                ingredient_box.drawBox()
                ingredients[5].changePosition(385, 103)
                globalvariables.WIN.blit(salmon1_image, (330, 200))
                globalvariables.WIN.blit(pygame.transform.scale(arrow3_image, (200, 300)), (345, 210))
                start_time, counting_time = draw(True, 343.0, 329.0, 391.0, 556.0, 348.0, 605.0, 303.0, 558.0, 5, 5.0,  start_time, counting_time, timer_text, timer_box, colours)
                cut = cut + 1
            elif cut == 13:
                globalvariables.WIN.blit(salmon2_image, (330, 200))
                globalvariables.WIN.blit(pygame.transform.scale(arrow3_image, (200, 300)), (405, 210))
                start_time, counting_time = draw(True, 403.0, 329.0, 365.0, 559.0, 448.0, 559.0, 404.0, 601.0, 5, 5.0,  start_time, counting_time, timer_text, timer_box, colours)
                cut = cut + 1
            elif cut == 14:
                instruction_box.drawBox() #display the instructions
                clickinstruction_text.drawText()
                salmon3_button.draw()
                salmon3_button.setActive()
        if value == "Assembly 4":
            if assemble == 1: #the first part in assembling the sushi roll is to add the rice
                ingredient_box.changeY(60)
                ingredient_box.drawBox() #displays the ingredient of the seaweed
                ingredients[1].changePosition(335, 63)
                globalvariables.WIN.blit(seaweeds[0], (200, 100))
                instruction_box.drawBox()
                draw3instruction_text.drawText() #displays the instruction of "drawing" on the rice
                start_time, counting_time = draw(True, 537.0, 643.0, 167.0, 645.0, 539.0, 309.0, 166.0, 309.0, 10, 10.0,  start_time, counting_time, timer_text, timer_box, colours)
                #the draw subroutine is called
                assemble = assemble + 1 #once the rice has been added, rice is incremented
            elif assemble == 2: #after the rice is added
                if addIngredient <= 9: #while the toppings for the sushi is still being added
                    if active_ingredient: #if an ingredient / topping is being dragged
                        mx, my = pygame.mouse.get_pos() #get the position of the mouse
                        if 200 <= mx + 190 <= (200 + seaweed_width) and 100 + 50 <= my + 190 <= (100 + seaweed_height): #checks if the mouse is on the seaweed
                            addIngredient = addIngredient + 1 #if it is then increment so the next ingredient can be added onto the seaweed
                            active_ingredient = False #the current ingredient is no longer being dragged

                if addIngredient == 0:
                    globalvariables.WIN.blit(seaweeds[1], (200, 100)) #the seaweed with just the rice
                    globalvariables.WIN.blit(slicedcucumber_image, slicedcucumber1_rect)
                elif addIngredient == 1:
                    globalvariables.WIN.blit(seaweeds[2], (200, 100)) #the seaweed with one cucumber
                    globalvariables.WIN.blit(slicedcucumber_image, slicedcucumber2_rect)
                elif addIngredient == 2:
                    globalvariables.WIN.blit(seaweeds[3], (200, 100)) #the seaweed with two cucumbers
                    globalvariables.WIN.blit(slicedcucumber_image, slicedcucumber3_rect)

                elif addIngredient == 3:
                    globalvariables.WIN.blit(seaweeds[4], (200, 100)) #the seaweed with three cucumbers
                    globalvariables.WIN.blit(slicedavocado_image, slicedavocado1_rect)
                elif addIngredient == 4:
                    globalvariables.WIN.blit(seaweeds[5], (200, 100)) #the seaweed with three cucumbers + one avocado...
                    globalvariables.WIN.blit(slicedavocado_image, slicedavocado2_rect)
                elif addIngredient == 5:
                    globalvariables.WIN.blit(seaweeds[6], (200, 100))
                    globalvariables.WIN.blit(slicedavocado_image, slicedavocado3_rect)

                elif addIngredient == 6:
                    globalvariables.WIN.blit(seaweeds[7], (200, 100))
                    globalvariables.WIN.blit(slicedsalmon_image, slicedsalmon1_rect)
                elif addIngredient == 7:
                    globalvariables.WIN.blit(seaweeds[8], (200, 100))
                    globalvariables.WIN.blit(slicedsalmon_image, slicedsalmon2_rect)
                elif addIngredient == 8:
                    globalvariables.WIN.blit(seaweeds[9], (200, 100))
                    globalvariables.WIN.blit(slicedsalmon_image, slicedsalmon3_rect)
                
                elif addIngredient == 9:
                    globalvariables.WIN.blit(seaweeds[10], (200, 100))
                    back_button.drawBox()
                    back_text.drawText()
                
        clock.tick(globalvariables.FPS)
        pygame.display.update()
    
    if value == "Assembly 4": #if the node is at the end of the assembly step
        if 0 <= int(counting_time / 1000) <= 90: #if the time is between 0 and 90 seconds
            sushiScore.append(100) #the score is 100
        elif 21 <= int(counting_time / 1000) <= 120: #if the time is between 21 and 120 seconds
            sushiScore.append(70) #the score is 70
        elif int(counting_time / 1000) >= 150: #if the time is more than 150 seconds
            sushiScore.append(50) #the score is 50
        score = score + sushiScore[1] #added to the total score for the sushi recipe

    while cutting:
        for event in pygame.event.get(): #allows user to quit the window
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                backPressed = back_button.checkPressed(pygame.mouse.get_pos())
                backActive = back_button.getActive()
                if backPressed == True and backActive == False: #checks if the back button is pressed
                    cutting = False #if it has been pressed, then the cutting stage is finished
                    back_button.setActive() #makes sure it can't be pressed again
        
        globalvariables.WIN.blit(gameBg_image, bgPosition)
        globalvariables.WIN.blit(clock_image, (20, 10))
        timer_box.drawBox()
        counting_time = pygame.time.get_ticks() - start_time
        timer_text.changeText(str( int(counting_time/1000) ).zfill(2)) #the time is displayed
        
        if value == "Cutting 1": #if at the first node of the cutting step
            globalvariables.WIN.blit(pygame.transform.scale(cuttingBoard_image, (1100, 400)), (-200, 150)) #display the cutting board, which has been transformed
            if cut == 0: #for the first cut
                draw1instruction_text.drawText()
                globalvariables.WIN.blit(sushirolls[0], (130, 280)) #display the first sushi roll
                globalvariables.WIN.blit(pygame.transform.scale(arrow3_image, (200, 250)), (510, 230)) #display the arrow
                start_time, counting_time = draw(True, 508.0, 344.0, 551.0, 536.0, 509.0, 573.0, 467.0, 537.0, 5, 5.0,  start_time, counting_time, timer_text, timer_box, colours)
                #call the draw subroutine to allow the user to trace the arrow to be able to cut the sushi roll
                cut = cut + 1 #increment cut, so that the rest of the sushi roll can be cut
            elif cut == 1: #for the second cut
                globalvariables.WIN.blit(sushirolls[1], (130, 280)) #display the second roll
                globalvariables.WIN.blit(pygame.transform.scale(arrow3_image, (200, 250)), (560, 230)) #display the arrow
                start_time, counting_time = draw(True, 559.0, 345.0, 605.0, 539.0, 558.0, 574.0, 517.0, 538.0, 5, 5.0,  start_time, counting_time, timer_text, timer_box, colours)
                #call the draw subroutine to allow the user to trace the arrow to be able to cut the sushi roll
                cut = cut + 1 #increment cut so the rest of the sushi roll can be cut
            elif cut == 2:
                globalvariables.WIN.blit(sushirolls[2], (130, 280))
                globalvariables.WIN.blit(pygame.transform.scale(arrow3_image, (200, 250)), (610, 230))
                start_time, counting_time = draw(True, 607.0, 349.0, 653.0, 535.0, 573.0, 543.0, 605.0, 567.0, 5, 5.0,  start_time, counting_time, timer_text, timer_box, colours)
                cut = cut + 1
            elif cut == 3:
                globalvariables.WIN.blit(sushirolls[3], (130, 280))
                globalvariables.WIN.blit(pygame.transform.scale(arrow3_image, (200, 250)), (640, 230))
                start_time, counting_time = draw(True, 638.0, 351.0, 686.0, 535.0, 638.0, 572.0, 599.0, 539.0, 5, 5.0,  start_time, counting_time, timer_text, timer_box, colours)
                cut = cut + 1
            elif cut == 4:
                globalvariables.WIN.blit(sushirolls[4], (130, 280))
                globalvariables.WIN.blit(pygame.transform.scale(arrow3_image, (200, 250)), (670, 230))
                start_time, counting_time = draw(True, 667.0, 339.0, 711.0, 540.0, 665.0, 575.0, 629.0, 537.0, 5, 5.0,  start_time, counting_time, timer_text, timer_box, colours)
                cut = cut + 1
            elif cut == 5:
                globalvariables.WIN.blit(sushirolls[5], (130, 280))
                globalvariables.WIN.blit(pygame.transform.scale(arrow3_image, (200, 250)), (700, 230))
                start_time, counting_time = draw(True, 699.0, 344.0, 745.0, 537.0, 699.0, 573.0, 657.0, 537.0, 5, 5.0,  start_time, counting_time, timer_text, timer_box, colours)
                cut = cut + 1
            elif cut == 6:
                globalvariables.WIN.blit(sushirolls[6], (130, 280))
                back_button.drawBox()
                back_text.drawText()
        
        clock.tick(globalvariables.FPS)
        pygame.display.update()
    
    if value == "Cutting 1": #once the cutting stage is completed
        if 0 <= int(counting_time / 1000) <= 30: #if the time is between 0 and 30 seconds
            sushiScore.append(100) #the score is 100
        elif 21 <= int(counting_time / 1000) <= 40: #if the time is between 21 and 40 seconds
            sushiScore.append(70) #the score is 70
        elif int(counting_time / 1000) >= 60: #if the time is more than 60 seconds
            sushiScore.append(50) #the score is 50
        score = (score + sushiScore[2]) // 3 #add to the total score and find the average
        startingScreen = False #starting screen set to false as the recipe has been completed so the screen with the scores will be displayed instead

    return value, stack, visitedNodes, sushiScore, score, startingScreen
