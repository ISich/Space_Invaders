import random

import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.image.load("enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self, new_x, new_y):
        self.rect.center = [new_x, new_y]
        self.x = new_x
        self.y = new_y

    def check_x_border_right(self, distance, x_border):
        return self.rect.x + self.rect.width + distance <= x_border

    def move_right(self, distance):
        self.update(self.x + distance, self.y)

    def check_x_border_left(self, distance, x_border):
        return self.rect.x - distance >= x_border

    def move_left(self, distance):
        self.update(self.x - distance, self.y)

    def check_player_border(self, distance, player_border):
        return self.rect.y + self.rect.height + distance <= player_border

    def move_down(self, distance):
        self.update(self.x, self.y + distance )