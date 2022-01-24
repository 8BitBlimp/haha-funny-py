# imports and stuff
import random
import pygame
pygame.init()


# stuff to change freely
fps = 60
clock = pygame.time.Clock()



# screen
sizeX = 1920
sizeY = 1080
screen = pygame.display.set_mode([sizeX, sizeY])
# backgrounds
start = pygame.image.load('./textures/start.jpg')
death = pygame.image.load('./textures/bg_dead.png')
survive = pygame.image.load('./textures/alive.jpg')
buttonBG = pygame.image.load('./textures/button-bg.png')

# list in charge of chances, change freely
dead = 'You shot yourself! Good job!'
alive = 'You survive another round!'
fuck = [dead, dead, dead, alive, dead, dead]

# font and text
nFont = pygame.font.SysFont('Corbel', 40)
text = nFont.render('Try your luck.', True, (255,0,0))
hSizeX = sizeX / 2
hSizeY = sizeY / 2
button = pygame.Rect(810, 490, 300, 100)
button2 = pygame.Rect(1770, 0, 150, 50)

deadText = nFont.render(dead, True, (255,0,0))
returnText = nFont.render('Return', True, (0,0,0))


sceneS = True
sceneD = False
sceneA = False

running = True
while running == True:
    
    screen.fill(0)
    if sceneS == True:
        screen.blit(start, (0,0))
        ahh = pygame.draw.rect(screen, (51, 153, 255), button)
        screen.blit(buttonBG, (810,490))
        screen.blit(text, (hSizeX - 100 , hSizeY - 20))
        
        
    
    if sceneD == True:
        screen.blit(death, (0,0))
        ahhh = pygame.draw.rect(screen, (255,0,0), button2)
        screen.blit(returnText, (1780,8))


    if sceneA == True:
        screen.blit(survive, (0,0))
        ahhh = pygame.draw.rect(screen, (255,255,255), button2)
        screen.blit(returnText, (1780,8))

        
    

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            
            if sceneS == True:
                if button.collidepoint(mouse_pos):
                    pain = random.choice(fuck)
                    if pain == dead:
                        sceneS = False
                        sceneA = False
                        sceneD = True
                        screen.blit(death, (0,0))
                    if pain == alive:
                        sceneS = False
                        sceneD = False
                        sceneA = True
                        screen.blit(survive, (0,0))
            if sceneA or sceneD == True:
                if button2.collidepoint(mouse_pos):
                        sceneS = True
                        sceneA = False
                        sceneD = False
                

    
    
    
    
    pygame.display.update()
    clock.tick(fps)

    


    