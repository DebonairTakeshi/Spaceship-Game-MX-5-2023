import pygame
import os

# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 60
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))


SPACE_INVADERS = pygame.image.load(os.path.join(IMG_DIR, 'Other/title.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = 'default'
SHIELD_TYPE = 'shield'

SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))

BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
BOSS = pygame.image.load(os.path.join(IMG_DIR, "Enemy/miniboss.png"))
CUCARACHON = pygame.image.load(os.path.join(IMG_DIR, "Enemy/cucarachon.png"))
LASER_PLAYER = pygame.image.load(os.path.join (IMG_DIR, "Bullet/laser.gif"))
LASER_PLAYER2 = pygame.image.load(os.path.join (IMG_DIR, "Bullet/pulse2.png"))
LASER_PLAYER3 = pygame.image.load(os.path.join (IMG_DIR, "Bullet/pulse3.png"))
LASER_PLAYER4 = pygame.image.load(os.path.join (IMG_DIR, "Bullet/pulse4.png"))
##pygame.image.load(os.path.join(IMG_DIR, "Bullet/blue/pulse1.png"))
##pygame.image.load("back.png")

FONT_STYLE = 'freesansbold.ttf'
BLACK_COLOR = (0, 0, 0)
WHITE_COLOR = (255, 255, 255)




BULLET_ENEMY_TYPE = 'enemy'
BULLET_PLAYER_TYPE = 'player'
BULLET_SPACESHIP_TYPE = 'spaceship'
BULLET_SPACESHIP_TYPE2 = 'laser'

LEFT = 'left'
RIGHT = 'right'
