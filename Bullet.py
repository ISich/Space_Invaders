import pygame


class Bullet(object):
    def __init__(self, x, y, width, height, direction, color, step, win_height, health_bar_border):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.direction = direction
        self.color = color
        self.step = step
        self.win_height = win_height
        self.health_bar_border = health_bar_border

    def fly(self):
        self.y -= self.direction * self.step

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))

    def check_enemy(self, enemy):
        if enemy == -1:
            return False
        if self.x < enemy.rect.x+enemy.width and self.x + self.width > enemy.rect.x:
            if self.y < enemy.rect.y + enemy.height and self.y + self.height > enemy.rect.y:
                return True
        return False

    def check_player(self, player):
        if self.x < player.rect.x + player.width and self.x + self.width > player.rect.x:
            if self.y < player.rect.y + player.height and self.y + self.height > player.rect.y:
                return True
        return False

    def check_block(self, block):
        if self.x < block.x + block.width and self.x + self.width > block.x:
            if self.y < block.y + block.height and self.y + self.height > block.y:
                return True
        return False

    def is_bullet_inside(self):
        return 0 <= self.y + self.height and self.y <= self.health_bar_border - self.height
