import pygame
from player import Player
from enemy_wave import EnemyWave
from shot_manager import ShotManager

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

pygame.display.set_caption("Chris Space Invaders")
icon = pygame.image.load("assets/space_ship.png")
pygame.display.set_icon(icon)

player = Player()
player_move_speed = 10
enemy_move_speed_x = 3
enemy_move_speed_y = 2

enemyWave = EnemyWave()
enemyWave.speed_x = enemy_move_speed_x

shotManager = ShotManager()

running = True
while running:
    pygame.time.delay(100)
    screen.fill((0, 0, 0))
    dt = clock.tick(60)

    if enemyWave.has_right_wall_collision():
        enemyWave.speed_x = -enemy_move_speed_x
        enemyWave.move_down()
    elif enemyWave.has_left_wall_collision():
        enemyWave.speed_x = enemy_move_speed_x
        enemyWave.move_down()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.speed_x = -player_move_speed
            elif event.key == pygame.K_RIGHT:
                player.speed_x = player_move_speed
            elif event.key == pygame.K_UP:
                player.speed_y = -player_move_speed
            elif event.key == pygame.K_DOWN:
                player.speed_y = player_move_speed
            elif event.key == pygame.K_SPACE:
                shotManager.add_shot(for_player=player)
        elif event.type == pygame.KEYUP:
            if (event.key == pygame.K_LEFT and player.speed_x < 0)\
                    or (event.key == pygame.K_RIGHT and player.speed_x > 0):
                player.speed_x = 0
            elif (event.key == pygame.K_UP and player.speed_y < 0)\
                    or (event.key == pygame.K_DOWN and player.speed_y > 0):
                player.speed_y = 0

    player.move()
    enemyWave.move()
    shotManager.move()

    player.draw()
    enemyWave.draw()
    shotManager.draw()
    pygame.display.update()

pygame.quit()
