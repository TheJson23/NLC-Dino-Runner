from dino_runner.components.obstacles.obstacle import Obstaculo
import random
class Cactus(Obstaculo):
    def __init__(self, image):
        self.type = random.randint(0,2)
        self.randoms = random.randint(0,1)
        super().__init__(image,self.type,self.randoms)
        self.rect.y = 325 
    def pos_y(self,resta):
        self.rect.y = 325 - resta
