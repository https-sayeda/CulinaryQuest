# Imports
import sys
import pygame
import random
import os

#website where drawing thing came from :
#https://thepythoncode.com/article/make-a-drawing-program-with-python#:~:text=In%20this%20tutorial%2C%20we%20will%20make%20a%20simple,feature.%20As%20always%2C%20we%20start%20with%20the%20imports.
def draw(WIN, draw, x1, y1, x2, y2, x3, y3, x4, y4):

    flag1 = False
    flag2 = False
    flag3 = False
    flag4 = False
    # the colour and size of the brush
    drawColour = [0, 0, 255]
    brushSize = 10
    canvasSize = [800, 800]

    # Canvas
    canvas = pygame.Surface((canvasSize),pygame.SRCALPHA)
    canvas.set_alpha(200)

    while draw:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break
        # Draw the Canvas at the center of the screen
        x, y = WIN.get_size()
        WIN.blit(canvas, [x/2 - canvasSize[0]/2, y/2 - canvasSize[1]/2])
        if flag1 == True and flag2 == True and flag3 == True and flag4 == True:
            draw = False
            pygame.display.update()

        position = "nothing"
        dx = 0
        dy = 0
        # Drawing with the mouse
        if pygame.mouse.get_pressed()[0]:
            mx, my = pygame.mouse.get_pos()

            # Calculate Position on the Canvas
            dx = mx - x/2 + canvasSize[0]/2
            dy = my - y/2 + canvasSize[1]/2

            pygame.draw.circle(canvas, drawColour,[dx, dy], brushSize)

        if (x1-5.0) <= dx <= (x1+5.0) and (y1-5.0) <= dy <= (y1+5.0):
            flag1 = True
        if (x2-5.0) <= dx <= (x2+5.0) and (y2-5.0) <= dy <= (y2+5.0):
            flag2 = True
        if (x3-5.0) <= dx <= (x3+5.0) and (y3-5.0) <= dy <= (y3+5.0):
            flag3 = True
        if (x4-5.0) <= dx <= (x4+5.0) and (y4-5.0) <= dy <= (y4+5.0):
            flag4 = True

        pygame.display.update()
    WIN.blit(canvas, [x/2 - canvasSize[0]/2, y/2 - canvasSize[1]/2])
    pygame.display.update()
      
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
        hand_rect = WIN.blit(hand_image, (hand_x, hand_y))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break

        keys = pygame.key.get_pressed()

        if len(burgerLayer_order) != 0:
            hand_x = layer_x
            for i in range(len(burgerLayer_order)):
                WIN.blit(burgerLayer_order[i], (layer_x, hand_y - (10*(i+1))))
            if keys[pygame.K_LEFT] == True or keys[pygame.K_a] == True:
                layer_x -= hand_speed
            if keys[pygame.K_RIGHT] == True or keys[pygame.K_d] == True:
                layer_x += hand_speed
        
        if keys[pygame.K_LEFT] == True or keys[pygame.K_a] == True:
            hand_x -= hand_speed
        if keys[pygame.K_RIGHT] == True or keys[pygame.K_d] == True:
            hand_x += hand_speed
            
        if hand_x <= 0:
            hand_x = 0
        elif hand_x >= (window_x - hand_width):
            hand_x = (window_x - hand_width)
        
        component_y += component_speed

        if component_y > window_y:
            component_x = random.randint(0, window_x - component_width)
            component_y = 0
        elif hand_rect.colliderect(component_rect):
            burgerLayer_order.append(burgerLayer_images[count])
            component_x = random.randint(0, window_x - component_width)
            component_y = 0
            if count != 7:
                count = count + 1

        pygame.display.update()
    
        if count == 7:
            assembly = False

    return assembly