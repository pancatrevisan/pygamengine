from GameMap import *
from Background import *
from BackgroundLayer import *

class Mapa360(GameMap):
    def __init__(self, bkgFile):
        GameMap.__init__(self, None)
        self.background = pygame.image.load(bkgFile)
        
        self.velocidade = 200 #pixels/s
        
        self.widthPixels = self.background.get_width()
        self.heigthPixels = self.background.get_height()

        self.rotateDir = 'N'
    
    
    def render(self, dest):
        #dest.blit(self.background, [0,0])
        
        dest.blit(self.background, [self.window[0] * -1,0])
        dest.blit(self.background, [self.window[0] * -1 + self.background.get_width(),0])
        

    def rotate(self, dir):
        self.rotateDir = dir

    def update(self, dt):
        
        if self.rotateDir == 'N':
            return
        elif self.rotateDir == 'L':
            self.window[0] -= int(dt*self.velocidade)
            if self.window[0] < 0:
                self.window[0] = self.widthPixels -1 - int(dt*self.velocidade)
        elif self.rotateDir == 'R':
            self.window[0] += int(dt*self.velocidade)
            if(self.window[0]> self.widthPixels):
                self.window[0] = self.window[0] // self.widthPixels
        #print(self.window)

