import pygame
from enemy import Enemy


class EnemyWave:
    def __init__(self, number_of_enemies=30):
        self.enemies = []
        self.screen = pygame.display.get_surface()

        border_padding = (50, 50)
        enemies_per_line, spacing = self._calc_number_of_enemies_per_line(border_padding=border_padding,
                                                                          enemy_min_spacing=40)

        for idx in range(1, number_of_enemies + 1):
            new_enemy = Enemy()
            enemies_before_on_same_line = ((idx - 1) % enemies_per_line)
            spaced_enemy_width = new_enemy.image.get_width() + spacing
            new_enemy.positionX = border_padding[0] + spaced_enemy_width * enemies_before_on_same_line

            enemy_lines_before = int((idx - 1) / enemies_per_line)
            spaced_enemy_height = new_enemy.image.get_height() + spacing
            new_enemy.positionY = border_padding[1] + spaced_enemy_height * enemy_lines_before

            self.enemies.append(new_enemy)

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

    def draw(self):
        for enemy in self.enemies:
            enemy.draw()
