import pygame
import random
from ninja import Ninja


# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 20)
pygame.display.set_caption("Desert Ninja")


def next(house_x, tree_x):
    distance = tree_x - house_x
    if distance < 0:
        distance = house_x - tree_x
    if distance >= 0 and distance <= 100:
        return True
    else:
        return False


# set up variables for the display
size = (900, 800)
screen = pygame.display.set_mode(size)

bg_size= (900,800)
bg = pygame.image.load("images/desert-background.png")
bg= pygame.transform.scale(bg, bg_size)
bg_position = (0,0)
cactus_size= (100,200)
cactus= pygame.image.load("images/cactus.png")
cactus= pygame.transform.scale(cactus, cactus_size)
cactus_pair = pygame.image.load("images/cactus_pair.png")
cactus_pair_size= (200,200)
cactus_pair = pygame.transform.scale(cactus_pair, cactus_pair_size)

ninja_x = 100
ninja = Ninja(100, 560)



INITIAL_CACTUS_X = random.randint(200,600)
INITIAL_CACTUS_PAIR_X = random.randint(200,600)
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
    if ninja_x <= 0 and ninja_x >= 900:
        cactus_x  = 600
    if ninja_x <= 0:
        cactus_pair_x = 600
    next_to_each_other = next(cactus_x, cactus_pair_x)
    if next_to_each_other:
        INITIAL_CACTUS_X = random.randint(0, 500)
    cactus_pair_x = cactus_pair_x - 5
    cactus_x = cactus_x - 5
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        ninja.move_ninja("up")
    else:
        ninja.move_ninja("down")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If user clicked close
            run = False
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False

    screen.blit(bg, bg_position)
    screen.blit(cactus, (cactus_x, 560))
    screen.blit(cactus_pair, (cactus_pair_x, 560))
    screen.blit(ninja.image, ninja.rect)
    pygame.display.update()

    frame += 1

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()
