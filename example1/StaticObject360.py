from GameObject360 import *
from Animation import *
from Sprite import *

class StaticObject360(GameObject360):
    def __init__(self, spr):
        GameObject.__init__(self)       
        normal = Animation("normal")
        normal.setOwner(self)
        normal.addSprite(Sprite(spr,200/1000.0,self, normal))


        self.animations[normal.name] = normal


        self.currentAnimation = normal




    def update(self, dt):
        return

        
        
    