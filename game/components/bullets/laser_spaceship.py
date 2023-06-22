import pygame
from game.components.bullets.bullet import Bullet
from game.utils.constants import LASER_PLAYER

class LaserSpaceship(Bullet):
    WIDTH = 10
    HEIGHT = 100
    SPEED = 10
    
    
    def __init__(self, center):
        self.image = LASER_PLAYER
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image, center)
        
    def update(self, enemy):
        self.rect.y -= self.SPEED
        super().update(enemy)
        if not enemy.is_alive:
            enemy.is_destroyed = True