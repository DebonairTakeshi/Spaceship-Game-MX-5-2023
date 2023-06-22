import pygame
from game.components.enemies.enemy import Enemy


from game.utils.constants import CUCARACHON


class Cucarachon(Enemy):
    WIDTH = 200
    HEIGHT = 200
    SHOOTING_TIME = 10
    INTERVAL = 200
    

    def __init__(self):
        self.image = CUCARACHON
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image)