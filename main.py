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

bg_size= (800,600)
bg = pygame.image.load("images/desert-background.png")
bg= pygame.transform.scale(bg, bg_size)
bg_position = (0,0)
cactus_size= (100,350)
cactus = pygame.image.load("images/cactus.png")
cactus= pygame.transform.scale(cactus, cactus_size)
cactus_pair = pygame.image.load("images/cactus_pair.png")


ninja =  Ninja(100, 350)




INITIAL_CACTUS_X = random.randint(0,600)
INITIAL_CACTUS_Y = random.randint(500,600)
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
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        ninja.move_ninja("right")
    if keys[pygame.K_w]:
        ninja.move_ninja("up")
    else:
        ninja.move_ninja("down")
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False

    screen.blit(bg, bg_position)
    screen.blit(cactus, (cactus_x, 200))
    screen.blit(ninja.image, ninja.rect)
    pygame.display.update()

    frame += 1

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()

