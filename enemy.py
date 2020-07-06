import pygame
from moving_object import MovingObject
from edge_insets import EdgeInsets
from threading import Timer
from pygame import mixer


class Enemy(MovingObject):
    def __init__(self, pos_x=400, pos_y=300):
        MovingObject.__init__(self, image_name="enemy.png", start_pos_x=pos_x, start_pos_y=pos_y)
        self.screen_borders = EdgeInsets(left=10, right=10)
        self.state = "alive"
        self.explosionSound = mixer.Sound("assets/explosion.wav")
        self.explosionSound.set_volume(0.04)

    def has_collision_with_bullet(self, bullet):
        return self.has_collision_with(bullet, offset=10)

    def kill(self):
        self.state = "dead"

    def explode(self):
        if not (self.state == "dead" and self.state == "exploding"):
            self.state = "exploding"
            self.explosionSound.play()
            self.image = pygame.image.load("assets/explosion.png")
            Timer(0.3, self.kill).start()
