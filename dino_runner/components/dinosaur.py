
import pygame

from pygame.sprite import Sprite
from dino_runner.utils.constants import RUNNING,JUMPING,DUCKING,DEATH,HAMMER_TYPE,RUNNING_HAMMER,JUMPING_HAMMER,DUCKING_HAMMER
from dino_runner.utils.constants import DUCKING_SHIELD,RUNNING_SHIELD,JUMPING_SHIELD,DEFAULT_TYPE,SHIELD_TYPE

DUCK_IMG = {DEFAULT_TYPE :  DUCKING,  SHIELD_TYPE : DUCKING_SHIELD, HAMMER_TYPE: DUCKING_HAMMER}
JUMP_IMG = {DEFAULT_TYPE :  JUMPING,  SHIELD_TYPE : JUMPING_SHIELD, HAMMER_TYPE: JUMPING_HAMMER}
RUN_IMG  = {DEFAULT_TYPE :  RUNNING,  SHIELD_TYPE : RUNNING_SHIELD, HAMMER_TYPE: RUNNING_HAMMER}


class Dinosaur(Sprite):
    X_POS    =  80
    Y_POS    = 310
    JUMP_VEL =   8.5
    
    def __init__(self):
        self.type           = DEFAULT_TYPE
        self.image          = RUN_IMG[self.type][0]
        self.dino_rect      = self.image.get_rect()
        self.dino_rect.x    = self.X_POS
        self.dino_rect.y    = self.Y_POS
        self.step_index     = 0
        self.dino_run       = True
        self.dino_jum       = False
        self.dino_duck      = False
        self.jump_vel       = self.JUMP_VEL
        self.dino_death     = False
        self.hammer_power   = False
        self.setup_states()

    def setup_states(self):
        self.has_power_up   = False
        self.shield         = False
        self.show_text      = False
        self.shield_time_up = 0
    
    def events(self):
        if self.dino_run:
            self.run()
        elif self.dino_jum:
            self.jump()
        elif self.dino_duck:
            self.duck()
        elif self.dino_death:
            self.death()

        if self.hammer_power:
            self.throw_hammer()
    
    def update(self,user_imput):
        
        self.events()
        
        if user_imput[pygame.K_UP ]  and not self.dino_jum:
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
        
        elif self.type == "hammer" and user_imput[pygame.K_b]:
            self.hammer_power = True
            
        if self.step_index >= 10:
            self.step_index = 0
        
    
    def jump(self):
        self.image = JUMP_IMG[self.type]
        
        if  self.dino_jum:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel    -= 0.8
          
        if self.jump_vel < -self.JUMP_VEL:
            self.dino_rect.y = self.Y_POS
            self.dino_jum    = False
            self.jump_vel    = self.JUMP_VEL
        
    def duck(self):
        self.image       = DUCK_IMG[self.type][self.step_index // 5]
        self.dino_rect   = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS + 30
        self.step_index += 1
        
    def run(self):
        self.image       = RUN_IMG[self.type][self.step_index // 5]
        self.dino_rect   = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS 
        self.step_index += 1
    
    def dance(self):
        self.imagen = JUMPING
    
    def draw(self,screen:pygame.Surface):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))            
    
    def check_invicibility(self,screen):
        if self.shield == True:
            time_to_show = round((self.shield_time_up - pygame.time.get_ticks()) / 100, 2)
            if time_to_show >= 0 and self.show_text:
                font = pygame.font.Font("freesansbold.ttf",30)
                text = font.render(f"power: {time_to_show}",True,(0,0,0))
                text_rect = text.get_rect()
                text_rect.center = (600, 50)
                screen.blit(text,text_rect)
            else:
                self.has_power_up   = False
                self.shield         = False
                self.show_text      = False
                self.type           = DEFAULT_TYPE

    def death(self):
        self.image = DEATH
    
    def throw_hammer(self):
        self.type           = DEFAULT_TYPE
        self.image          = RUN_IMG[self.type][0]
        #self.hammer_power = False

