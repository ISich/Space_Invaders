import pygame


class Arrow(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.sprite = pygame.sprite.Group()
        self.sprite.add(self)
        self.image = pygame.image.load("arrow_up.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.arrows = [pygame.image.load("arrow_right.png"), pygame.image.load("arrow_up.png"),
                       pygame.image.load("arrow_left.png")]

    def rotate(self, arrow):
        self.image = self.arrows[arrow]
