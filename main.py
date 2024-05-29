import pygame
import random
from ninja import Ninja
from cactus import Cactus
from cactus_pair import Cactus_Pair
from tumbleweed import Tumbleweed
from rock import Rock

pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 20)
pygame.display.set_caption("Desert Ninja")
size = (1050, 1000)
screen = pygame.display.set_mode(size)
bg_size= (1050,1000)
bg = pygame.image.load("images/desert-background.png")
bg= pygame.transform.scale(bg, bg_size)
bg_position = (0,0)
cactus_size= (100,200)
ninja_x = 100
ninja = Ninja(100, 800)
cactus = Cactus(800,750)
cactus_pair = Cactus_Pair(800,750)
tumbleweed = Tumbleweed(800,750)
rock = Rock(800,750)


INITIAL_CACTUS_X = 900
INITIAL_CACTUS_PAIR_X = 900
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
    if keys[pygame.K_SPACE]:
        ninja.move_ninja("up")
    else:
        ninja.move_ninja("down")
    cactus.move_cactus()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If user clicked close
            run = False
    screen.blit(bg, bg_position)
    screen.blit(cactus.image, cactus.rect)
    if cactus.x < 0:
        screen.blit(cactus_pair.image, cactus_pair.rect)
        cactus_pair.move_cactus_pair()
    screen.blit(ninja.image, ninja.rect)
    pygame.display.update()
    frame += 1