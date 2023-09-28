import pygame
from Classes import *


def draw_enemy(enemy):
    global win
    pygame.draw.rect(win, enemy.color, (enemy.x, enemy.y, enemy.width, enemy.height))


def draw_army(army):
    global win
    for enemy_line in army.army:
        for enemy in enemy_line:
            draw_enemy(enemy)


def draw_bullets(bullets):
    global win
    for bullet in bullets:
        pygame.draw.rect(win, bullet.color, (bullet.x, bullet.y, bullet.wigth, bullet.height))


def move_bullets(bullets):
    for bullet in bullets:
        bullet.fly()


pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Space invaders")

x_player, y_player = 50, 400
width_player, height_player = 40, 60
army1 = Army(10, 10, 5, 4, 20, 20, 30, 30, (0, 255, 0))
bullets = []
speed = 5
shoot_delay = 0

run = True
time = 100
while run:
    pygame.time.delay(time)
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if keys[pygame.K_LEFT]:
        x_player -= speed
    if keys[pygame.K_RIGHT]:
        x_player += speed
    if keys[pygame.K_SPACE] and shoot_delay == 0:
        bullets.append(Bullet(x_player+width_player//2, y_player, 5, 5, 1, (255, 255, 255), 5))
        shoot_delay = 1

    shoot_delay = (shoot_delay + (shoot_delay != 0)) % 7

    win.fill((0, 0, 0))
    draw_army(army1)
    draw_bullets(bullets)

    army1.move(speed, 20, 500-20, y_player)
    move_bullets(bullets)

    pygame.draw.rect(win, (0, 0, 225), (x_player, y_player, width_player, height_player))
    pygame.display.update()

pygame.quit()