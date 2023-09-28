import pygame


class Bullet(object):
    def __init__(self, x, y, width, height, direction, color, step):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.direction = direction
        self.color = color
        self.step = step

    def fly(self):
        self.y -= self.direction * self.step

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))
