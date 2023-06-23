import pygame
from game.utils.constants import HEART
from game.utils.constants import SCREEN_WIDTH




class Life:
    WIDTH = 10
    HEIGHT = 10
    X_POS = (SCREEN_WIDTH // 2) - WIDTH
    Y_POS = 500
    

    def __init__(self):
        self.image = HEART
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    
    
        