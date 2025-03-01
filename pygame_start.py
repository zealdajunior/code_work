import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Basket dimensions
BASKET_WIDTH = 100
BASKET_HEIGHT = 20

# Object dimensions
OBJECT_WIDTH = 20
OBJECT_HEIGHT = 20

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Catch the Falling Objects")

# Basket class
class Basket(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([BASKET_WIDTH, BASKET_HEIGHT])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH // 2 - BASKET_WIDTH // 2
        self.rect.y = SCREEN_HEIGHT - BASKET_HEIGHT - 10

    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0] - BASKET_WIDTH // 2

# Object class
class FallingObject(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([OBJECT_WIDTH, OBJECT_HEIGHT])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - OBJECT_WIDTH)
        self.rect.y = -OBJECT_HEIGHT

    def update(self):
        self.rect.y += 5
        if self.rect.y > SCREEN_HEIGHT:
            self.rect.y = -OBJECT_HEIGHT
            self.rect.x = random.randint(0, SCREEN_WIDTH - OBJECT_WIDTH)

# Create sprite groups
all_sprites = pygame.sprite.Group()
falling_objects = pygame.sprite.Group()

# Create basket
basket = Basket()
all_sprites.add(basket)

# Create falling objects
for i in range(10):
    obj = FallingObject()
    all_sprites.add(obj)
    falling_objects.add(obj)

# Main game loop
running = True
clock = pygame.time.Clock()
score = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update sprites
    all_sprites.update()

    # Check for collisions
    collisions = pygame.sprite.spritecollide(basket, falling_objects, True)
    for collision in collisions:
        score += 1
        obj = FallingObject()
        all_sprites.add(obj)
        falling_objects.add(obj)

    # Clear the screen
    screen.fill(WHITE)

    # Draw sprites
    all_sprites.draw(screen)

    # Draw score
    font = pygame.font.SysFont(None, 36)
    text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()