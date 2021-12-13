from GameObject360 import *
from Animation import *
from Sprite import *

class AlvoMovel(GameObject360):
    def __init__(self, spr1, spr2, refem=False):
        GameObject.__init__(self)       
        normal = Animation("normal")
        normal.setOwner(self)
        normal.addSprite(Sprite(spr1,200/1000.0,self, normal))

        acertado = Animation("acertado")
        acertado.setOwner(self)
        acertado.addSprite(Sprite(spr2,200/1000.0,self, normal))

        self.MAX_H = 245 #altura maxima
        self.O_POS = 14 #posicao inicial
        self.position = [100, self.O_POS]
        self.EXPOSED_TIME = 2 #5 segundos?
        self.HIDDEN_TIME = 2 #2segundos?

        self.animations[normal.name] = normal
        self.animations[acertado.name] = acertado

        self.currentAnimation = normal


        self.velocidade = 100 #100px/s
        self.tempoExposto = 0 #2 segundos parados após subir
        self.tempoOculto = 0
        self.direcao = 'C' # 'C'ima, 'B'aixo, 'P'arado, 'O'culto

    def update(self, dt):
        newPos = [self.position[0], self.position[1]]

        if(self.direcao == 'C'):
            newPos[1] = newPos[1] + self.velocidade * dt #sobe um pouco
            if newPos[1] >= self.MAX_H:
                newPos[1] = self.MAX_H 
                self.direcao = 'P'
        elif self.direcao == 'B':
            newPos[1] = newPos[1] - self.velocidade * dt #desce um pouco
            if newPos[1] <= self.O_POS:
                self.direcao = 'O'
        elif self.direcao == 'P':
            self.tempoExposto += dt 
            if self.tempoExposto >= self.EXPOSED_TIME:
                self.tempoExposto = 0
                self.direcao = 'B'
        elif self.direcao == 'O':
            self.tempoOculto += dt 
            if self.tempoOculto >= self.HIDDEN_TIME:
                self.tempoOculto = 0
                self.direcao = 'C'
        self.position = newPos
        
    