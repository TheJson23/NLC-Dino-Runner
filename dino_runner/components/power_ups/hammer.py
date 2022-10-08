from dino_runner.components.power_ups.poer_up import PowerUp
from dino_runner.utils.constants import HAMMER,HAMMER_TYPE
from dino_runner.utils.constants import SCREEN_WIDTH
class Hammer(PowerUp):
    X_POS    =  80
    Y_POS    = 320
    RUN_VEL =   8.5
    
    def __init__(self):
        self.image = HAMMER
        self.type = HAMMER_TYPE
        self.rect = self.image.get_rect()
        self.rect.y  = self.Y_POS
        self.rect.x = SCREEN_WIDTH
        #self.throw_hammer = THROW_HAMMER

        super().__init__(self.image, self.type)

    def set_pos(self, rect_dino):
        self.rect = rect_dino
        return self

    def move_hammer(self, screen):
        self.rect.x += 25
        print(self.rect.x)
        screen.blit(self.image, self.rect)
