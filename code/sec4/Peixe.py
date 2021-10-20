from GameObject import *
from Animation import *
from Sprite import *
class Peixe(GameObject):
    def __init__(self):
        GameObject.__init__(self)        
        
        #Cria animacao...
        nadaDireita = Animation("nadaDireita")
        nadaDireita.setOwner(self)
        nadaDireita.addSprite(Sprite('betaFish/1.png',200/1000.0,self, nadaDireita))
        nadaDireita.addSprite(Sprite('betaFish/2.png',200/1000.0,self, nadaDireita))
        nadaDireita.addSprite(Sprite('betaFish/3.png',200/1000.0,self, nadaDireita))
        nadaDireita.addSprite(Sprite('betaFish/4.png',200/1000.0,self, nadaDireita))
        nadaDireita.addSprite(Sprite('betaFish/5.png',200/1000.0,self, nadaDireita))
        nadaDireita.addSprite(Sprite('betaFish/6.png',200/1000.0,self, nadaDireita))
        nadaDireita.addSprite(Sprite('betaFish/7.png',200/1000.0,self, nadaDireita))
        nadaDireita.addSprite(Sprite('betaFish/8.png',200/1000.0,self, nadaDireita))

        #adiciona às animações do Objeto
        self.animations[nadaDireita.name] = nadaDireita
        self.currentAnimation = nadaDireita
        self.velocidade = 100 #100px/s

    
    def update(self, dt):
        self.currentAnimation.update(dt)
        print("inc: " +str(self.velocidade * dt))
        self.position[0] += self.velocidade * dt
        