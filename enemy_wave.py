import pygame
from enemy import Enemy


class EnemyWave:
    def __init__(self, number_of_enemies=30):
        self.downMovement = 4
        self.enemies = []
        self.screen = pygame.display.get_surface()
        self.speedX = 0
        self.speedY = 0

        border_padding = (50, 50)
        enemies_per_line, spacing = self._calc_number_of_enemies_per_line(border_padding=border_padding,
                                                                          enemy_min_spacing=40)

        for idx in range(1, number_of_enemies + 1):
            new_enemy = Enemy()
            enemies_before_on_same_line = ((idx - 1) % enemies_per_line)
            spaced_enemy_width = new_enemy.image.get_width() + spacing
            new_enemy.position_x = border_padding[0] + spaced_enemy_width * enemies_before_on_same_line

            enemy_lines_before = int((idx - 1) / enemies_per_line)
            spaced_enemy_height = new_enemy.image.get_height() + spacing
            new_enemy.position_y = border_padding[1] + spaced_enemy_height * enemy_lines_before

            self.enemies.append(new_enemy)

    @property
    def speed_x(self):
        return self.speedX

    @speed_x.setter
    def speed_x(self, speed_x):
        self.speedX = speed_x
        for enemy in self.enemies:
            enemy.speed_x = speed_x

    @property
    def speed_y(self):
        return self.speedY

    @speed_y.setter
    def speed_y(self, speed_y):
        self.speedY = speed_y
        for enemy in self.enemies:
            enemy.speed_y = speed_y

    def move(self):
        for enemy in self.enemies:
            enemy.move()

    def has_left_wall_collision(self):
        for enemy in self.enemies:
            if enemy.has_left_wall_collision():
                return True
        return False

    def has_right_wall_collision(self):
        for enemy in self.enemies:
            if enemy.has_right_wall_collision():
                return True
        return False

    def move_down(self):
        for enemy in self.enemies:
            enemy.position_y += self.downMovement

    def draw(self):
        for enemy in self.enemies:
            enemy.draw()

    def check_bullet_collision(self, bullet):
        bullet_did_collide = False
        for enemy in self.enemies:
            if enemy.has_collision_with_bullet(bullet=bullet):
                enemy.explode()
                bullet_did_collide = True

        return bullet_did_collide

    def has_player_collision(self, player):
        lowest_enemy_y = 0
        for enemy in self.enemies:
            lowest_enemy_y = enemy.position_y + enemy.height

        return lowest_enemy_y - 10 >= player.position_y

    def remove_dead_enemies(self):
        dead_enemies = []
        for enemy in self.enemies:
            if enemy.state == "dead":
                dead_enemies.append(enemy)

        for enemy in dead_enemies:
            self.enemies.remove(enemy)

    def _calc_number_of_enemies_per_line(self, border_padding, enemy_min_spacing):
        enemy_width = Enemy().image.get_width()
        screen_width = self.screen.get_rect()[2]
        space_for_enemies = screen_width - 2 * border_padding[0]

        enemies_per_line = 1
        while True:
            if (enemies_per_line + 1) * (enemy_width + enemy_min_spacing) < space_for_enemies:
                enemies_per_line += 1
            elif (enemies_per_line + 1) * enemy_width < screen_width - 2 * border_padding[0]:
                enemies_per_line += 1
                break
            else:
                break

        spacing = (space_for_enemies - enemies_per_line * enemy_width) / (enemies_per_line - 1)

        return enemies_per_line, spacing
