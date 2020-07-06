import pygame
from player import Player
from enemy_wave import EnemyWave
from shot_manager import ShotManager

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

pygame.display.set_caption("Chris Space Invaders")
icon = pygame.image.load("assets/space_ship.png")
font = pygame.font.Font('assets/Formigas-Regular.otf', 30)
pygame.display.set_icon(icon)

player_move_speed = 10
enemy_move_speed_x = 6
enemy_move_speed_y = 0.5

player = Player()
enemyWave = EnemyWave()
shotManager = ShotManager()
lost = False
won = False


def reset():
    global lost, won, player, enemyWave, shotManager, player_move_speed

    lost = False
    won = False
    player = Player()
    enemyWave = EnemyWave(number_of_enemies=30)
    enemyWave.speed_x = enemy_move_speed_x
    enemyWave.speed_y = enemy_move_speed_y
    shotManager = ShotManager(speed=8, max_shots=8)
    player_move_speed = 10


reset()
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
                if not lost:
                    shotManager.add_shot(for_player=player)
            elif event.key == pygame.K_r:
                reset()
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

    collided_shots = []
    for shot in shotManager.shots:
        did_collide = enemyWave.check_bullet_collision(shot)
        if did_collide:
            collided_shots.append(shot)
    shotManager.remove(collided_shots)
    enemyWave.remove_dead_enemies()

    if len(enemyWave.enemies) == 0:
        won = True
    elif enemyWave.has_player_collision(player=player):
        lost = True
        enemyWave.speed_y = 0
        enemyWave.speed_x = 0
        player_move_speed = 0

    if won:
        won_text = font.render('You won!', True, (161, 220, 43))
        screen.blit(won_text, (((screen.get_width() - won_text.get_width()) / 2),
                               (screen.get_height() - won_text.get_height()) / 2))
    elif lost:
        won_text = font.render('You lost! :(', True, (219, 66, 43))
        screen.blit(won_text, (((screen.get_width() - won_text.get_width()) / 2),
                               (screen.get_height() - won_text.get_height()) / 2))

    player.draw()
    enemyWave.draw()
    shotManager.draw()
    pygame.display.update()

pygame.quit()
