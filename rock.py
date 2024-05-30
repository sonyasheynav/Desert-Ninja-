import pygame

class Rock:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("images/rock.png")
        self.rescale_image(self.image)
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = 6
        self.up = True

    def rescale_image(self, image):
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * .2, self.image_size[1] * .2)
        self.image = pygame.transform.scale(self.image, scale_size)

    def move_rock(self):
        self.x = self.x - self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
