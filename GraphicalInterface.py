import pygame
from Army import Army
from Bullet import Bullet
from Player import Player


class GraphicalInterface:
    def __init__(self, enemy_count, borders_count):
        pygame.init()
        self.win_width = 500
        self.win_height = 650
        self.window = pygame.display.set_mode((self.win_width, self.win_height))
        pygame.display.set_caption("Space invaders")

        x_player, y_player, width_player, height_player = 50, self.win_height-200, 40, 60
        x_army, y_army, x_count_army, y_count_army = 20, 20, 5, enemy_count // 5
        x_army_jump, y_army_jump, width_enemy, height_army = 20, 20, 30, 30
        self.shoot_delay = 0

        self.player = Player(x_player, y_player, width_player, height_player, self.win_width)
        self.army = Army(x_army, y_army, x_count_army, y_count_army, x_army_jump, y_army_jump,
                         width_enemy, height_army)
        self.bullets = []

        self.shoot_delay_cur = 0
        self.shoot_delay = 7
        self.run = True
        self.time = 100
        self.start()

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

            self.shoot_delay_cur = (self.shoot_delay_cur + (self.shoot_delay_cur != 0)) % self.shoot_delay

            self.window.fill((0, 0, 0))
            pygame.draw.rect(self.window, (0, 100, 230), pygame.Rect(0, 500, 500, 150))
            self.player.draw_hearts(self.window)
            self.check_army()
            self.draw_army()
            self.draw_bullets()

            self.army.move(self.player.speed, 20, 500 - 20, self.player.rect.y)
            self.move_bullets()
            self.del_leave_bullets()

            self.player.update()
            self.player.sprite.draw(self.window)
            pygame.display.update()

        pygame.quit()

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

    def del_leave_bullets(self):
        for bullet in range(len(self.bullets)):
            if not self.bullets[bullet].is_bullet_inside():
                del self.bullets[bullet]
                break
