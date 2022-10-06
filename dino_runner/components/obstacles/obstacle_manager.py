import pygame
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS
from dino_runner.utils.constants import LARGE_CACTUS


class ObstacleManger:
    
    def __init__(self):
        self.obstacles = []
        
        
    def update(self,game,ramdons):
        if len(self.obstacles,) == 0:
            if ramdons == 0:
                large_cactus = Cactus(LARGE_CACTUS)
                self.obstacles.append(large_cactus) 
            else:
                small_cactus = Cactus(SMALL_CACTUS)
                self.obstacles.append(small_cactus)
            
            
        
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed,self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(1000)
                game.playing = False
        
    
    def draw(self,screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
    
    def reset_obstacles(self):
        self.obstacles = []


        