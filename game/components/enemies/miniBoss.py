import pygame
from game.components.enemies.enemy import Enemy


from game.utils.constants import BOSS


class Boss(Enemy):
    WIDTH = 200
    HEIGHT = 200


    def __init__(self):
        self.image = BOSS
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image)