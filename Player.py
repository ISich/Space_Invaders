import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, win_width):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("player.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.width = width
        self.height = height
        self.win_width = win_width
        self.speed = 5
        self.sprite = pygame.sprite.Group()
        self.sprite.add(self)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x = max(self.rect.x - self.speed, 0)
        if keys[pygame.K_RIGHT]:
            self.rect.x = min(self.rect.x + self.speed, self.win_width)
