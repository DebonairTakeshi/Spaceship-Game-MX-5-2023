import pygame
from game.components.bullets.laser import Laser
from game.utils.constants import BULLET_PLAYER_LASER

class BulletSpaceship(Laser):
    WIDTH = 10
    HEIGHT = 20
    SPEED = 10
    
    
    def __init__(self, center):
        self.image = BULLET_PLAYER_LASER
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image, center)
        
    def update(self, enemy):
        self.rect.y -= self.SPEED
        super().update(enemy)
        