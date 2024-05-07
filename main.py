import pygame
import random
from ninja import Ninja


# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 20)
pygame.display.set_caption("Desert Ninja")


# set up variables for the display
size = (800, 600)
screen = pygame.display.set_mode(size)
BIRD_START_X = 500

bg = pygame.image.load("desert-background.png")
cactus = pygame.image.load("cactus.png")
cactus_pair = pygame.image.load("cactus_pair.png")


ninja= Ninja(BIRD_START_X, 250)



INITIAL_CACTUS_X = random.randint(0,600)
INITIAL_CACTUS_PAIR_X = random.randint(0,600)
cactus_x = INITIAL_CACTUS_X
cactus_pair_x = INITIAL_CACTUS_PAIR_X


# render the text for later

# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True
# -------- Main Program Loop -----------
clock = pygame.time.Clock()
frame = 0
while run:
    # --- Main event loop
    clock.tick(60)
    if frame % 30 == 0:
        ninja.switch_image()

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False

    screen.blit(bg, (0, 0))
    screen.blit(cactus, (house_x, 360))
    screen.blit(tree, (tree_x, 360))
    screen.blit(bird.image, bird.rect)
    screen.blit(b.image, b.rect)
    pygame.display.update()

    frame += 1

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()

