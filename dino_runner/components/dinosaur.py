import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import RUNNING
from dino_runner.utils.constants import JUMPING
from dino_runner.utils.constants import DUCKING

class Dinosaur(Sprite):
    X_POS    =  80
    Y_POS    = 310
    JUMP_VEL =   8.5
    
    def __init__(self):
        self.image          = RUNNING[0]
        self.dino_rect      = self.image.get_rect()
        self.dino_rect.x    = self.X_POS
        self.dino_rect.y    = self.Y_POS
        self.step_index     = 0
        self.dino_run       = True
        self.dino_jum       = False
        self.dino_duck      = False
        self.dino_jump_duck = False
        self.jump_vel       = self.JUMP_VEL
    
    def update(self,user_imput):
        
        if self.dino_run:
            self.run()
        elif self.dino_jum:
            self.jump()
        elif self.dino_duck:
            self.duck()
        
        if user_imput[pygame.K_UP ] or user_imput[pygame.K_SPACE] and not self.dino_jum:
            self.dino_jum  = True
            self.dino_run  = False
        elif not self.dino_jum:
            self.dino_jum  = False
            self.dino_run  = True
        
        if user_imput[pygame.K_DOWN] and not self.dino_jum :
            self.dino_duck = True
            self.dino_run  = False
        elif not self.dino_duck:
            self.dino_duck = False
            self.dino_run  = True

        if self.step_index >= 10:
            self.step_index = 0
    
    def jump(self):
        self.image = JUMPING
        
        if  self.dino_jum:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
          
        if self.jump_vel < -self.JUMP_VEL:
            self.dino_rect.y = self.Y_POS
            self.dino_jum = False
            self.jump_vel = self.JUMP_VEL
        
    def duck(self):
        self.image = DUCKING[0] if self.step_index < 5 else DUCKING[1]
        self.dino_rect   = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS + 30
        self.step_index += 1
        
    def run(self):
        self.image = RUNNING[0] if  self.step_index < 5 else RUNNING[1]
        self.dino_rect   = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS 
        self.step_index += 1

    def draw(self,screen:pygame.Surface):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
