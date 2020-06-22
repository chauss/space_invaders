import pygame
from moving_object import MovingObject
from edge_insets import EdgeInsets


class Enemy(MovingObject):
    def __init__(self, pos_x=400, pos_y=300):
        MovingObject.__init__(self, image_name="enemy.png", start_pos_x=pos_x, start_pos_y=pos_y)
        self.screen_borders = EdgeInsets(left=10, right=10)
