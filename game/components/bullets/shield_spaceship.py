import pygame
from game.components.bullets.bullet import Bullet
from game.utils.constants import SHIELD

class ShieldSpaceship(Bullet):
    WIDTH = 100
    HEIGHT = 60
    
    
    def __init__(self, center):
        self.image = SHIELD
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image, center)
        
    def update(self, enemy):
        super().update(enemy)
        if not enemy.is_alive:
            enemy.is_destroyed = True