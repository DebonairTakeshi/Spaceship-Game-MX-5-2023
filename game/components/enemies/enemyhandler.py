from game.components.enemies.Lytos import Lytos
from game.components.enemies.k57 import K57
from game.components.enemies.cucarachon import Cucarachon


class EnemyHandler:
    def __init__(self):
        self.enemies = []
        self.number_enemies_destroyed = 0

    def update(self, bullet_handler):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update(bullet_handler)
            if enemy.is_destroyed:
                self.number_enemies_destroyed += 1
            if not enemy.is_alive:
                self.remove_enemy(enemy)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        if len(self.enemies) < 1:
            self.enemies.append(Lytos())
            self.enemies.append(K57())
            self.enemies.append(Cucarachon())

    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)
        
    def reset(self):
        self.enemies = []
        self.number_enemies_destroyed = 0