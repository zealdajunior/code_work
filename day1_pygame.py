# pygame.display, pygame.draw, pygame.event, pygame.image, pygame.key, pygame.mouse, pygame.sprite, pygame.time, pygame.transform
# pygame.mixer, pygame.font, pygame.color, pygame.joystick, pygame.mask, pygame.math, pygame.mixer_music, pygame.scrap, pygame.surface

background_image = "C:/Users/GSI/Desktop/IMG_20250115_142403.jpg"
mouse_image = "C:/Users/GSI/Desktop/IMG_20250115_091632.jpg"

import pygame
from pygame.locals import *
from sys import exit

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)
pygame.display.set_caption("DZELD GAME")
background = pygame.image.load(background_image).convert()
mouse_cursor = pygame.image.load(mouse_image).convert_alpha()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    
    screen.blit(background, (0, 0))
    x, y = pygame.mouse.get_pos()
    x -= mouse_cursor.get_width() / 2
    y -= mouse_cursor.get_height() / 2
    screen.blit(mouse_cursor, (x, y))
    
    pygame.display.update()