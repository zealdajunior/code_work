import pygame
pygame.init() #initialising the pygame

screen = pygame.display.set_mode((800,600),0,32) #create screen


pygame.display.set_caption("Space invaders")
icon = pygame.image.load('z.png')
pygame.display.set_icon(icon) #To ensure the image is effectively loaded
#game loop, makes sure the window always stays on screen

#player
playerImg = pygame.image.load('fifapc.ico')
playerX = 400
playerY = 500
playerX_change = 0

def player(x,y):
    screen.blit(playerImg,(x, y))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0,0,0)) #RBG
    # if keystrock is pressed check if its left or right
    if event.type == pygame.KEYDOWN:
        
        if event.key == pygame.K_LEFT:
            playerX_change =  -0.5
          
        if event.key == pygame.K_RIGHT:
            playerX_change =  0.5
            
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerX_change = 0
            
    
    playerX += playerX_change
    player(playerX,playerY)
    pygame.display.update()
                  

