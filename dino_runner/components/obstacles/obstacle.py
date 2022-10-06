from pygame.sprite import Sprite
import random

from dino_runner.utils.constants import SCREEN_WIDTH

class Obstaculo(Sprite):
    def __init__(self,image,type,type_2):
        self.image = image
        self.type = type
        self.type_2 = type_2
        
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()
    

    def draw(self,screen):
        
        screen.blit(self.image[self.type],self.rect)