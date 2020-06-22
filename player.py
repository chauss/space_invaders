import pygame
from moving_object import MovingObject
from edge_insets import EdgeInsets


class Player(MovingObject):
    def __init__(self):
        MovingObject.__init__(self, image_name="space_ship.png")
        self.screen_borders = EdgeInsets(top=self.screen.get_rect()[3] * 2 / 3, left=50, right=50, bottom=80)
        self.position_x = self.screen.get_rect()[2] / 2 - self.image.get_width() / 2
        self.position_y = 480
