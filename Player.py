import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, win_width):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("player.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.width = width
        self.hp = 3
        self.hearts = []
        self.height = height
        self.win_width = win_width
        self.speed = 5
        self.sprite = pygame.sprite.Group()
        self.sprite.add(self)

    def draw_hearts(self, window):
        x = 50
        y = 525
        for i in range(self.hp):
            heart = pygame.image.load("heart.png")
            now_x = x
            x += 150
            self.hearts.append(heart)
            window.blit(heart, (now_x, y))

    def damage(self):
        self.hp -= 1
        heart = self.hearts.pop(0)
        del heart

    def check_death(self):
        return self.hp != 0

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x = max(self.rect.x - self.speed, 0)
        if keys[pygame.K_RIGHT]:
            self.rect.x = min(self.rect.x + self.speed, self.win_width)
