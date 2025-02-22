from game.utils.constants import BULLET_ENEMY_TYPE, BULLET_SPACESHIP_TYPE, BULLET_SPACESHIP_TYPE2, SHIELD_TYPE
from game.components.bullets.bullet_enemy import BulletEnemy
from game.components.bullets.bullet_spaceship import BulletSpaceship
from game.components.bullets.laser_spaceship import LaserSpaceship
from game.components.bullets.shield_spaceship import ShieldSpaceship
class BulletHandler:
    def __init__(self):
        self.bullets = []
        

    def update(self, player, enemies):
        for bullet in self.bullets:
            if type(bullet) is BulletEnemy:
                bullet.update(player)
            elif type(bullet) is BulletSpaceship:
                for enemy in enemies:
                    bullet.update(enemy)
            elif type(bullet) is LaserSpaceship:
                for enemy in enemies:
                    bullet.update(enemy)
            if not bullet.is_alive:
                self.remove_bullet(bullet)

    def draw(self, screen):
        for bullet in self.bullets:
            bullet.draw(screen)

    def add_bullet(self, type, center):
        if type == BULLET_ENEMY_TYPE:
            self.bullets.append(BulletEnemy(center))
        elif type == BULLET_SPACESHIP_TYPE:
            self.bullets.append(BulletSpaceship(center))
        elif type == BULLET_SPACESHIP_TYPE2:
            self.bullets.append(LaserSpaceship(center))
        elif type == SHIELD_TYPE:
            self.bullets.append(ShieldSpaceship(center))

    def remove_bullet(self, bullet):
        self.bullets.remove(bullet)
        
    def reset(self):
        self.bullets = []
       
