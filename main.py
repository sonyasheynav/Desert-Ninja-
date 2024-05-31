import pygame
import random
from ninja import Ninja
from cactus import Cactus
from cactus_pair import Cactus_Pair
from tumbleweed import Tumbleweed
from rock import Rock
from obstacle import Obstacle

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
cactus = Obstacle(800,770, "cactus")
#tumbleweed = Obstacle(800,770, "tumbleweed")
# tumbleweed = Tumbleweed(900,920)
# rock = Rock(900,920)
points = 5
#put them into a list and iterate through the list and move them by selecting randomly and then once that object is off you pick the next one and this goes one while run
obstacles = [ cactus, ]

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
    #if ninja.rect.collidepoint(cactus) or ninja.rect.collidepoint(cactus_pair) or ninja.rect.collidepoint(rock) or ninja.rect.collidepoint(tumbleweed):
        #points = points - 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If user clicked close
            run = False


    screen.blit(bg, bg_position)
    for i in obstacles:
            screen.blit(i.image, i.rect)
            i.move_obstacle(i)
            if i.x < 0:
                screen.blit(i.image, (880,800))
                i.move_obstacle(i)
    screen.blit(ninja.image, ninja.rect)
    pygame.display.update()
    frame += 1



    #if cactus.x < 0:
        #screen.blit(cactus_pair.image, cactus_pair.rect)
        #cactus_pair.move_cactus_pair()
        #if cactus_pair.x < 0:
            #screen.blit(rock.image, rock.rect)
            #rock.move_rock()
            #if rock.x < 0:
                #screen.blit(tumbleweed.image, tumbleweed.rect)
                #tumbleweed.move_tumbleweed()