import time
from tkinter import *
import pygame
from Army import Army
from Bullet import Bullet
from Player import Player


class GraphicalInterface:
    def __init__(self, enemy_count, borders_count, level, choose_options):
        pygame.init()
        self.win_width = 500
        self.win_height = 650
        self.borders = borders_count
        self.level = level
        self.choose_options = choose_options
        self.window = pygame.display.set_mode((self.win_width, self.win_height))
        pygame.display.set_caption("Space invaders")

        x_player, y_player, width_player, height_player = 50, self.win_height-200, 40, 60
        x_army, y_army, x_count_army, y_count_army = 20, 20, 5, enemy_count // 5
        x_army_jump, y_army_jump, width_enemy, height_army = 20, 20, 30, 30
        self.shoot_delay = 0

        self.player = Player(x_player, y_player, width_player, height_player, self.win_width)
        self.army = Army(x_army, y_army, x_count_army, y_count_army, x_army_jump, y_army_jump,
                         width_enemy, height_army, self.player)
        self.bullets = []

        self.shoot_delay_cur = 0
        self.shoot_enemy = 0
        self.shoot_delay = 7
        self.shoot_enemy_delay = 10
        self.run = True
        self.time = 100
        self.start_time = time.time()

    def start(self):
        while self.run:
            pygame.time.delay(self.time)
            keys = pygame.key.get_pressed()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

            if keys[pygame.K_SPACE] and self.shoot_delay_cur == 0:
                self.bullets.append(Bullet(self.player.rect.x + self.player.rect.width // 2, self.player.rect.y,
                                           5, 5, 1, (0, 255, 0), 5, self.win_height))
                self.shoot_delay_cur = 1

            self.shoot_delay_cur = (self.shoot_delay_cur + (self.shoot_delay_cur != 0)) \
                                   % self.shoot_delay

            self.shoot_enemy = (self.shoot_enemy + 1) % self.shoot_enemy_delay
            if self.shoot_enemy == 0:
                point = self.army.choose_random_enemy()
                self.bullets.append(Bullet(point[0], point[1],
                                           5, 5, -1, (255, 0, 0), 5, self.win_height))

            self.window.fill((0, 0, 0))
            pygame.draw.rect(self.window, (0, 100, 230), pygame.Rect(0, 500, 500, 150))
            self.player.draw_hearts(self.window)
            self.player.update()
            self.player.sprite.draw(self.window)

            self.army.move(self.player.speed, 20, 500 - 20, self.player.rect.y)
            self.check_army()
            self.check_player()
            self.draw_army()
            self.draw_bullets()
            self.move_bullets()
            self.del_leave_bullets()

            pygame.display.update()

        pygame.quit()
        self.show_result_window()

    def draw_army(self):
        self.army.sprites.draw(self.window)

    def draw_bullets(self):
        for bullet in self.bullets:
            bullet.draw(self.window)

    def move_bullets(self):
        for bullet in self.bullets:
            bullet.fly()

    def check_army(self):
        self.army.check_bullets(self.bullets)
        self.run = self.army.check_death()

    def check_player(self):
        if self.run:
            self.run = self.player.check_death()

    def del_leave_bullets(self):
        for bullet in range(len(self.bullets)):
            if not self.bullets[bullet].is_bullet_inside():
                del self.bullets[bullet]
                break

    def show_result_window(self):
        finish_time = time.time() - self.start_time
        res_window = Tk()
        res_window.resizable(False, False)
        res_window.geometry("300x150")
        res_window.grab_set()

        text = "Вы выиграли!" if not self.army.check_death() > 0 else "Вы проиграли :("
        result_label = Label(res_window, text=text, font=("Roboto", 20, "bold"))
        result_label.pack(side=TOP, pady=10)

        return_button = Button(res_window, text="Вернуться в меню", font=("Roboto", 14), width=16,
                               command=lambda: self.return_to_menu(finish_time, res_window))
        return_button.pack(side=TOP, pady=10)

    def return_to_menu(self, finish_time, window):
        window.destroy()
        if self.player.hp > 0:
            self.choose_options.check_new_record(self.level, finish_time)
        self.choose_options.make_options_menu()
