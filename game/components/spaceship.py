import pygame
from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SPACESHIP_SHIELD
from game.utils.constants import BULLET_SPACESHIP_TYPE, BULLET_SPACESHIP_TYPE2, SHIELD_TYPE
from game.components.bullets.bullet_handler import BulletHandler
from game.components.power_ups.shield import Shield
from os import path



class Spaceship:
    WIDTH = 40
    HEIGTH = 60
    X_POS = (SCREEN_WIDTH // 2) - WIDTH
    Y_POS = 500
    SHOOTING_TIME = 30
    LIFES = 3
    pygame.mixer.init()

    def __init__(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGTH))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.is_alive = True
        self.has_shield = False
        self.time_up = 0
        
        self.sound_shoot = pygame.mixer.Sound('shoot.wav')
        self.sound_laser = pygame.mixer.Sound('laser.wav')
        self.sound_power_up = pygame.mixer.Sound('pickup.wav')

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
        elif user_input[pygame.K_s]:
            self.shoot_special(bullet_handler)
        elif user_input[pygame.K_d]:
            self.activate_shield(bullet_handler)
        
        if self.has_shield:
            time_to_show = round((self.time_up - pygame.time.get_ticks())/1000, 2)
            if time_to_show < 0:
                self.deactivate_power_up()
        
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
        self.sound_shoot.play()
        
        
    def shoot_special(self, bullet_handler):
        bullet_handler.add_bullet(BULLET_SPACESHIP_TYPE2, self.rect.center)
        self.sound_laser.play()
    
    def activate_shield(self, bullet_handler):
        bullet_handler.add_bullet(SHIELD_TYPE, self.rect.center)
        
    def activate_power_up(self, power_up):
        self.time_up = power_up.time_up
        if type(power_up) == Shield:
            self.has_shield = True
            self.image = SPACESHIP_SHIELD
            self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGTH + 2))
            self.sound_power_up.play()
    
    def deactivate_power_up(self):
        self.has_shield = False
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGTH))
    
    
    def reset(self):
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.is_alive = True