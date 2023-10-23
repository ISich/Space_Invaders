import random

from Enemy import Enemy
import pygame


class Army:
    def __init__(self, x_start, y_start, x_count, y_count, x_jump, y_jump,
                 enemy_width, enemy_height, player):
        self.x_count = x_count
        self.y_count = y_count
        self.step_down_count = 5
        self.curr_step_down = 0
        self.direction = 0
        self.army = []
        self.sprites = pygame.sprite.Group()
        self.player = player
        for y in range(y_count):
            line = []
            for x in range(x_count):
                enemy = Enemy(x_start+x*(x_jump+enemy_width), y_start+y*(y_jump+enemy_height),
                              enemy_width, enemy_height)
                line.append(enemy)
                self.sprites.add(enemy)
            self.army.append(line)

    def check_x_border_right(self, distance, x_border):
        for column in range(self.x_count-1, -1, -1):
            for enemy in range(self.y_count):
                if self.army[enemy][column] != -1:
                    return self.army[enemy][column].check_x_border_right(distance, x_border)

    def move_right(self, distance, x_border):
        if self.check_x_border_right(distance, x_border):
            for enemy_line in self.army:
                for enemy in enemy_line:
                    if enemy != -1:
                        enemy.move_right(distance)
        else:
            self.direction = 1

    def check_x_border_left(self, distance, x_border):
        for column in range(self.x_count):
            for enemy in range(self.y_count):
                if self.army[enemy][column] != -1:
                    return self.army[enemy][column].check_x_border_left(distance, x_border)

    def move_left(self, distance, x_border):
        if self.check_x_border_left(distance, x_border):
            for enemy_line in self.army:
                for enemy in enemy_line:
                    if enemy != -1:
                        enemy.move_left(distance)
        else:
            self.direction = 3

    def check_player_border(self, distance, player_border):
        for line in self.army[::-1]:
            for enemy in line:
                if enemy != -1:
                    return enemy.check_player_border(distance, player_border)

    def move_down(self, distance, player_border):
        if not self.check_player_border(distance, player_border):
            self.player.hp = 0
        for enemy_line in self.army:
            for enemy in enemy_line:
                if enemy != -1:
                    enemy.move_down(distance)
        self.curr_step_down += 1
        if self.curr_step_down == self.step_down_count:
            self.curr_step_down = 0
            if self.direction == 1:
                self.direction = 2
            else:
                self.direction = 0

    def move(self, distance, x_border_left, x_border_right, player_bord):
        if self.direction == 0:
            self.move_right(distance, x_border_right)
        elif self.direction == 1:
            self.move_down(distance, player_bord)
        elif self.direction == 2:
            self.move_left(distance, x_border_left)
        elif self.direction == 3:
            self.move_down(distance, player_bord)

    def check_bullets(self, bullets):
        for line in range(self.y_count):
            for enemy in range(self.x_count):
                for bullet in range(len(bullets)):
                    if bullets[bullet].check_enemy(self.army[line][enemy]):
                        del bullets[bullet]
                        self.army[line][enemy].kill()
                        self.army[line][enemy] = -1
                        break

    def choose_random_enemy(self):
        column = random.randint(0, self.x_count - 1)
        for line in range(self.y_count-1, -1, -1):
            if self.army[line][column] != -1:
                enemy = self.army[line][column]
                return [enemy.x + enemy.width // 2, self.army[line][column].y + enemy.height + 5]
        return self.choose_random_enemy()

    def check_death(self):
        for line in self.army:
            for enemy in line:
                if enemy != -1:
                    return True
        return False
