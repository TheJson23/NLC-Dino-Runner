from dino_runner.components.obstacles.obstacle import Obstaculo
import random
class Cactus(Obstaculo):
    def __init__(self, image):
        self.type = random.randint(0,2)
        super().__init__(image,self.type)
        self.rect.y = 325