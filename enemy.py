import pygame


class Enemy:
    def __init__(self, pos_x=400, pos_y=300):
        self.screen = pygame.display.get_surface()
        self.image = pygame.image.load("assets/enemy.png")
        self.positionX = pos_x
        self.positionY = pos_y
        self.speedX = 0
        self.speedY = 0

    @property
    def position(self):
        return self.positionX, self.positionY

    def draw(self):
        self.screen.blit(self.image, (self.positionX, self.positionY))
