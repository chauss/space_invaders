import pygame


class Player:
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.image = pygame.image.load("assets/space_ship.png")
        self.positionX = self.screen.get_rect()[2] / 2 - self.image.get_width() / 2
        self.positionY = 480
        self.speedX = 0
        self.speedY = 0

    @property
    def position(self):
        return self.positionX, self.positionY

    @property
    def speed_x(self):
        return self.speedX

    @speed_x.setter
    def speed_x(self, speed_x):
        self.speedX = speed_x

    @property
    def speed_y(self):
        return self.speedY

    @speed_y.setter
    def speed_y(self, speed_y):
        self.speedY = speed_y

    def move(self):
        new_player_x = self.positionX + self.speed_x
        self.positionX = min(max(new_player_x, 50), self.screen.get_rect()[2] - 50 - self.image.get_width())

        new_player_y = self.positionY + self.speed_y
        self.positionY = min(max(new_player_y, self.screen.get_rect()[3] * 2 / 3), self.screen.get_rect()[3] - 80)

    def draw(self):
        self.screen.blit(self.image, (self.positionX, self.positionY))
