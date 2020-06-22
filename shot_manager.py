import random
from shot import Shot


class ShotManager:
    def __init__(self, speed=10):
        self.shotSpeed = speed
        self.shots = []

    def add_shot(self, for_player):
        shot_left = bool(random.getrandbits(1))

        pos_x = for_player.position_x
        if shot_left:
            pos_x += (for_player.image.get_width() / 2)

        pos_y = for_player.position_y
        new_shot = Shot(start_pos_x=pos_x, start_pos_y=pos_y)
        new_shot.speed_y = -self.shotSpeed
        self.shots.append(new_shot)

    def move(self):
        for shot in self.shots:
            shot.move()
        self.shots = [shot for shot in self.shots if shot.position_y + shot.image.get_height() > 0]

    def draw(self):
        for shot in self.shots:
            shot.draw()

