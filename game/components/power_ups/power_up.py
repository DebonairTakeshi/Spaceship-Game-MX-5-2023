import pygame, random
from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT



class PowerUp:
    WIDTH = 30
    HEIGHT = 30
    POS_Y = 0
    SPEED = 5
    
    
    
    def __init__(self, image):
        self.image = image
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        self.rect = self.image.get_rect()
        self.rec.x = random.randint(120, SCREEN_WIDTH - 120)
        self.rect.y = self.POS_Y
        self.is_alive = True
        self.is_used = False
        
    def update(self, player):
        self.rect.y += self.SPEED
        if self.rect.y >= SCREEN_HEIGHT:
            self.is_alive = False
        if self.rect.colliderect(player.rect):
            self.is_alive = False
            self.is_used = True
        
        
    
    def draw (self, screen):
        screen.blit(self.image, self.rect)