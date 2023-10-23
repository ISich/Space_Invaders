import pygame


class Block(object):
    def __init__(self, x, y, width, height, hp, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hp = hp
        self.colors = [(65, 65, 65), (135, 135, 135), (255, 255, 255)]
        self.color = color

    def damage(self):
        self.hp -= 1
        self.color = self.colors[self.hp - 1]

    def check_death(self):
        return self.hp != 0

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))
