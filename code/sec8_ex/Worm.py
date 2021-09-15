
from GameObject import *
from Animation import *
from Sprite import *
class Worm(GameObject):
    def __init__(self):
        GameObject.__init__(self)        
        
        #Cria animacao...
        parado = Animation("parado")
        parado.setOwner(self)
        parado.addSprite(Sprite('worm.png',200/1000.0,self, parado))

        #adiciona às animações do Objeto
        self.animations[parado.name] = parado
        self.currentAnimation = parado
        self.velocidade = 100 #100px/s
        self.position = [750,0]
        self.alive = True
    
    def update(self, dt):
        self.currentAnimation.update(dt)
        self.position[0] += self.velocidade * dt
    
    def render(self, dest):
        if(self.alive):
            GameObject.render(self,dest)
        
        