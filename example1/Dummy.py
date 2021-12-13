from GameObject import *
from Animation import *
from Sprite import *
class Dummy(GameObject):
    def __init__(self, spr):
        GameObject.__init__(self)       
        normal = Animation("dummy_iddle")
        normal.setOwner(self)
        normal.addSprite(Sprite(spr,200/1000.0,self, normal))
        self.animations[normal.name] = normal
        self.currentAnimation = normal

    def update(self):
        pass