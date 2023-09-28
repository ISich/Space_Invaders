import pygame
from Army import Army
from Bullet import Bullet
from Player import Player


class GraphicalInterface:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((500, 500))
        pygame.display.set_caption("Space invaders")

        self.player = Player(50, 400, 40, 60)
        self.army = Army(10, 10, 5, 4, 20, 20, 30, 30, (0, 255, 0))
        self.bullets = []
        self.shoot_delay = 0

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
            self.player.update()
            if keys[pygame.K_SPACE] and self.shoot_delay == 0:
                self.bullets.append(Bullet(self.player.rect.x + self.player.rect.width // 2, self.player.rect.y,
                                           5, 5, 1, (255, 255, 255), 5))
                shoot_delay = 1

            shoot_delay = (self.shoot_delay + (self.shoot_delay != 0)) % 7

            self.window.fill((0, 0, 0))
            self.draw_army()
            self.draw_bullets()

            self.army.move(self.player.speed, 20, 500 - 20, self.player.rect.y)
            self.move_bullets()

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
