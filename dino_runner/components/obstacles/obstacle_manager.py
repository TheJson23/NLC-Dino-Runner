import pygame
from dino_runner.components.obstacles.cactus import Cactus

from dino_runner.utils.constants import SMALL_CACTUS
from dino_runner.utils.constants import LARGE_CACTUS
import random


class ObstacleManger:
    
    def __init__(self):
        self.obstacles = []
        self.resta = 0
        
        
    def update(self,game):
        if len(self.obstacles,) == 0:
            
            random_1 = random.randint(0,1)
            if random_1 == 0:
                self.resta = 30
                large_cactus = Cactus(LARGE_CACTUS)
                self.obstacles.append(large_cactus)
                large_cactus.pos_y(self.resta)
            else: 
                small_cactus = Cactus(SMALL_CACTUS)
                self.obstacles.append(small_cactus)
                self.resta = 0
                small_cactus.pos_y(self.resta)
                
            
            
        
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed,self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(1000)
                game.playing = False
        
    
    def draw(self,screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen,)
    
    
    def reset_obstacles(self):
        self.obstacles = []


        