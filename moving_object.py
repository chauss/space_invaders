import pygame
from edge_insets import EdgeInsets


class MovingObject:
    def __init__(self, image_name, screen_borders=EdgeInsets(), start_pos_x=0, start_pos_y=0):
        self.screen = pygame.display.get_surface()
        self.image = pygame.image.load("assets/" + image_name)
        self._screenBorders = screen_borders
        self._positionX = start_pos_x
        self._positionY = start_pos_y
        self._speedX = 0
        self._speedY = 0

    @property
    def position_x(self):
        return self._positionX

    @position_x.setter
    def position_x(self, position_x):
        self._positionX = position_x

    @property
    def position_y(self):
        return self._positionY

    @position_y.setter
    def position_y(self, position_y):
        self._positionY = position_y

    @property
    def screen_borders(self):
        return self._screenBorders

    @screen_borders.setter
    def screen_borders(self, screen_borders):
        self._screenBorders = screen_borders

    @property
    def speed_x(self):
        return self._speedX

    @speed_x.setter
    def speed_x(self, speed_x):
        self._speedX = speed_x

    @property
    def speed_y(self):
        return self._speedY

    @speed_y.setter
    def speed_y(self, speed_y):
        self._speedY = speed_y

    def move(self):
        new_player_x = self._positionX + self._speedX
        self._positionX = min(max(new_player_x, self._screenBorders.left), self.screen.get_rect()[2] -
                              self._screenBorders.right - self.image.get_width())

        new_player_y = self._positionY + self._speedY
        self._positionY = min(max(new_player_y, self._screenBorders.top), self.screen.get_rect()[3] -
                              self._screenBorders.bottom)

    def draw(self):
        self.screen.blit(self.image, (self.position_x, self.position_y))

    def has_left_wall_collision(self):
        return self._positionX <= self._screenBorders.left

    def has_right_wall_collision(self):
        return self._positionX >= self.screen.get_rect()[2] - self._screenBorders.right - self.image.get_width()
