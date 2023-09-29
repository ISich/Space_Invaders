import pygame


class Bullet(object):
    def __init__(self, x, y, width, height, direction, color, step, win_height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.direction = direction
        self.color = color
        self.step = step
        self.win_height = win_height

    def fly(self):
        self.y -= self.direction * self.step

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))

    def check_enemy(self, enemy):
        if enemy == -1:
            return False
        if self.x <= enemy.rect.x+enemy.width and self.x + self.width >= enemy.rect.x:
            if self.y <= enemy.rect.y + enemy.height and self.y + self.height >= enemy.rect.y:
                return True
        return False

    def is_bullet_inside(self):
        return 0 <= self.y + self.height and self.y <= self.win_height
