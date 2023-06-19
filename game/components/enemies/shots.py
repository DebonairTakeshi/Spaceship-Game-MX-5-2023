import pygame

BALAS = pygame.sprite.Group()
class Disparos(pygame.sprite.Sprite):



 def __init__(self, x, y):
  super().__init__()
  self.image = pygame.transform.scale(pygame.image.load("Bullet/bullet_1.png").convert(),(10,20))
  self.rect = self.image.get_rect()
  self.rect.bottom = y
  self.rect.centerx = x
  balas = pygame.sprite.Group()
  def draw (self, screen):
        screen.blit(self.image, self.rect)
  BALAS.update()
  BALAS.draw(self.screen)
