import pygame
from game.utils.constants import SPACESHIP, SCREEN_WIDTH
from game.utils.constants import BULLET_SPACESHIP_TYPE
from game.components.bullets.bullet_handler import BulletHandler

class Spaceship:
    WIDTH = 40
    HEIGTH = 60
    X_POS = (SCREEN_WIDTH // 2) - WIDTH
    Y_POS = 500
    SHOOTING_TIME = 30

    def __init__(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGTH))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.is_alive = True

    def update(self, user_input, bullet_handler):
        if user_input[pygame.K_LEFT]:
            self.move_left()
        elif user_input[pygame.K_RIGHT]:
            self.move_right()
        elif user_input[pygame.K_UP]:
            self.move_up()
        elif user_input[pygame.K_DOWN]:
            self.move_down()
        elif user_input[pygame.K_SPACE]:
            self.shoot(bullet_handler)
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move_left(self):
        if self.rect.left > 0:
            self.rect.x -= 10
    def move_right(self):
        if self.rect.right < 1100:
            self.rect.x += 10
    def move_down(self):
        if self.rect.bottom < 600:
            self.rect.y += 10
    def move_up(self):
        if self.rect.top > 0:
            self.rect.y -= 10
        
    def shoot(self, bullet_handler):
        bullet_handler.add_bullet(BULLET_SPACESHIP_TYPE, self.rect.center)