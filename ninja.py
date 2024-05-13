import pygame
class Ninja:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        # add jump sprite too
        self.image_list = ["images/Run__000.png", "images/Run__004.png", "images/Jump__002.png", "images/Jump__008.png"]
        self.image = pygame.image.load(self.image_list[0])
        self.rescale_image(self.image)
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = 3
        self.up = True

    def rescale_image(self, image):
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * .34, self.image_size[1] * .34)
        self.image = pygame.transform.scale(self.image, scale_size)

    def move_ninja(self,direction):
        if direction == "down":
            self.y = self.y + self.delta + 1
        if direction == "up":
            self.y = self.y - self.delta
    #make it not be able to go below the floor
        self.x = self.x + self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])


    def switch_image(self):
        image_number = 0
        if not self.up:
            image_number = 1
        if self.up:
            image_number = 2
        self.image = pygame.image.load(self.image_list[image_number])
        self.rescale_image(self.image)
        self.image_size = self.image.get_size()
        self.up = not self.up


