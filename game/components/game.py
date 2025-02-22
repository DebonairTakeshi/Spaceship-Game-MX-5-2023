import pygame

from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, WHITE_COLOR, SPACE_INVADERS, HEART
from game.components.spaceship import Spaceship
from game.components.enemies.enemyhandler import EnemyHandler
from game.components.bullets.bullet_handler import BulletHandler
from game.components.power_ups.power_up_handler import PowerUpHandler
from game.utils.constants import BULLET_PLAYER_TYPE
from game.utils.life import Life
from game.utils import text_utils


class Game:
    WIDTH = 50
    HEIGHT = 50
    
    
    
    
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = Spaceship()
        self.enemy_handler = EnemyHandler()
        self.bullet_handler = BulletHandler()
        self.power_up_handler = PowerUpHandler()
        self.lives = Life
        self.number_death = 3
        self.score = 0
        
        
        

    def run(self):
        # Game loop: events - update - draw
        self.running = True
        while self.running:
            self.events()
            self.update()
            self.draw()
        pygame.display.quit()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
            elif event.type == pygame.KEYDOWN and not self.playing:
                self.playing = True
                self.reset()
        
            

    def update(self):
        if self.playing:
            user_input = pygame.key.get_pressed()
            self.player.update(user_input, self.bullet_handler)
            self.enemy_handler.update(self.bullet_handler)
            self.bullet_handler.update(self.player, self.enemy_handler.enemies)
            self.power_up_handler.update(self.player)
            self.score = self.enemy_handler.number_enemies_destroyed
            
            if not self.player.is_alive:
                ##pygame.time.delay(300)
                
                self.number_death -= 1
                self.reset()
            elif self.number_death < 1:
                self.playing = False
                self.reset()
                

    def draw(self):
        self.draw_background()
        if self.playing:
            self.clock.tick(FPS)
            self.player.draw(self.screen)
            self.enemy_handler.draw(self.screen)
            self.bullet_handler.draw(self.screen)
            self.power_up_handler.draw(self.screen)
           
            self.draw_score()
            self.draw_deaths()
        else:
            self.draw_menu()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed
    
    def draw_menu(self):
        
        if self.number_death == 3:
            
            
            
            text, text_rect = text_utils.get_message('Press any Key to Start', 30, WHITE_COLOR)
            tutorial, tutorial_rect = text_utils.get_message('Use SPACE to shoot', 20, WHITE_COLOR, height=SCREEN_HEIGHT//2 + 50)
            tutorial2, tutorial2_rect = text_utils.get_message('Use ARROWS to move', 20, WHITE_COLOR, height=SCREEN_HEIGHT//2 + 80)
            tutorial3, tutorial3_rect = text_utils.get_message('Use S for special attack', 20, WHITE_COLOR, height=SCREEN_HEIGHT//2 + 110)
            
            
            self.screen.blit(text, text_rect)
            self.screen.blit(tutorial, tutorial_rect)
            self.screen.blit(tutorial2, tutorial2_rect)
            self.screen.blit(tutorial3, tutorial3_rect)
            
        else:
            text, text_rect = text_utils.get_message('Press any Key to Restart', 30, WHITE_COLOR)
            score, score_rect = text_utils.get_message(f'Your score is: {self.score}', 30, WHITE_COLOR, height=SCREEN_HEIGHT//2 + 50)
            self.screen.blit(text, text_rect)
            self.screen.blit(score, score_rect)
            
    def draw_score(self):
        score, score_rect = text_utils.get_message(f'Your score is:{self.score}', 20, WHITE_COLOR, 1000, 40)
        self.screen.blit(score, score_rect)
        
    def draw_deaths(self):
        deaths, death_rect = text_utils.get_message(f'Lifes: {self.number_death}', 20, WHITE_COLOR, 100, 40)
        self.screen.blit(deaths, death_rect)
        
        
    def reset(self):
        self.player.reset()
        self.enemy_handler.reset()
        self.bullet_handler.reset()
        self.power_up_handler.reset()
        self.number_death == 3
        
    