import pygame
from player import Player
from enemy_wave import EnemyWave

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

pygame.display.set_caption("Chris Space Invaders")
icon = pygame.image.load("assets/space_ship.png")
pygame.display.set_icon(icon)

player = Player()
move_speed = 10

enemyWave = EnemyWave()

running = True
while running:
    pygame.time.delay(100)
    screen.fill((0, 0, 0))
    dt = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.speed_x = -move_speed
            elif event.key == pygame.K_RIGHT:
                player.speed_x = move_speed
            elif event.key == pygame.K_UP:
                player.speed_y = -move_speed
            elif event.key == pygame.K_DOWN:
                player.speed_y = move_speed
        elif event.type == pygame.KEYUP:
            if (event.key == pygame.K_LEFT and player.speed_x < 0)\
                    or (event.key == pygame.K_RIGHT and player.speed_x > 0):
                player.speed_x = 0
            elif (event.key == pygame.K_UP and player.speed_y < 0)\
                    or (event.key == pygame.K_DOWN and player.speed_y > 0):
                player.speed_y = 0

    player.move()
    player.draw()
    enemyWave.draw()
    pygame.display.update()

pygame.quit()
