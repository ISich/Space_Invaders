from Enemy import Enemy
import pygame


class Army:
    def __init__(self, x_start, y_start, x_count, y_count, x_jump, y_jump,
                 enemy_width, enemy_height, enemy_color):
        self.x_start = x_start
        self.y_start = y_start
        self.x_count = x_count
        self.y_count = y_count
        self.x_jump = x_jump
        self.y_jump = y_jump
        self.enemy_width = enemy_width
        self.enemy_height = enemy_height
        self.enemy_color = enemy_color
        self.last_in_line = y_count - 1 #in which line last
        self.first_in_line = 0 #in which line first
        self.last_in_column = x_count - 1 #in which column last
        self.step_down_count = 5
        self.curr_step_down = 0
        self.direction = 0
        self.army = []
        self.sprites = pygame.sprite.Group()
        for y in range(y_count):
            line = []
            for x in range(x_count):
                enemy = Enemy(x_start+x*(x_jump+enemy_width), y_start+y*(y_jump+enemy_height),
                                  enemy_width, enemy_height)
                line.append(enemy)
                self.sprites.add(enemy)
            self.army.append(line)

    def check_x_border_right(self, distance, x_border):
        return self.army[self.last_in_line][-1].check_x_border_right(distance, x_border)

    def move_right(self, distance, x_border):
        if self.check_x_border_right(distance, x_border):
            for enemy_line in self.army:
                for enemy in enemy_line:
                    enemy.move_right(distance)
        else:
            self.direction = 1

    def check_x_border_left(self, distance, x_border):
        return self.army[self.first_in_line][0].check_x_border_left(distance, x_border)

    def move_left(self, distance, x_border):
        if self.check_x_border_left(distance, x_border):
            for enemy_line in self.army:
                for enemy in enemy_line:
                    enemy.move_left(distance)
        else:
            self.direction = 3

    def check_player_border(self, distance, player_border):
        return self.army[-1][self.last_in_column].check_player_border(distance, player_border)

    def move_down(self, distance, player_border):
        if not self.check_player_border(distance, player_border):
            exit()
        for enemy_line in self.army:
            for enemy in enemy_line:
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