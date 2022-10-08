from dino_runner.components.power_ups.poer_up import PowerUp
from dino_runner.utils.constants import HAMMER,HAMMER_TYPE
class Hammer(PowerUp):
    
    def __init__(self, image, type):
        self.image = HAMMER
        self.type = HAMMER_TYPE

        super().__init__(image, type)