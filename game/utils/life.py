import pygame
from game.utils.constants import HEART




class life:
    WIDTH = 10
    HEIGHT = 10
    X_POS = 0
    Y_POS = 0
    
def __init__(self):
    self.image = HEART
    self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
    