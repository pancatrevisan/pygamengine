from GameObject import *
from Animation import *
from Sprite import *
#object to be inserted in an GameMap360.
class GameObject360(GameObject):
    def __init__(self):
        GameObject.__init__(self)       
        
    def render(self, dest):
        if self.currentAnimation != None:
            bb = self.currentAnimation.getCurrentSprite().getCollisionBox()
            
            mapWindow = self.map.window 
            if (mapWindow[0] + mapWindow[2]) > self.map.widthPixels-1:
                #will draw the end and beginning.
                offset = self.map.widthPixels -1 -mapWindow[0]
                end = (mapWindow[0] + mapWindow[2])%self.map.widthPixels
                
                posToScreen = [int(abs(offset)) + self.position[0], int(self.map.window[3] - self.position[1])]
                pygame.draw.circle(dest,(0,0,0),posToScreen,3)

                worldToScreen = [posToScreen[0] - self.currentAnimation.getCurrentSprite().getAlign()[0], 0]
                worldToScreen[1] = self.position[1]+self.currentAnimation.getCurrentSprite().getHeight()
                worldToScreen[1] = self.map.window[3] - worldToScreen[1]
                worldToScreen = [int(worldToScreen[0]), worldToScreen[1]]
                self.currentAnimation.render(dest, worldToScreen)

                Box on Screen não está em coordenada de tela
                print("colbox: " + str(self.currentAnimation.getCurrentSprite().getCollisionBox().computeOnScreen()))

            else:
                
                    
                worldToScreen = [self.position[0] - self.currentAnimation.getCurrentSprite().getAlign()[0] - self.map.getWindow()[0], 0]
                worldToScreen[1] = self.position[1]+self.currentAnimation.getCurrentSprite().getHeight()
                worldToScreen[1] = self.map.window[3] - worldToScreen[1]
                worldToScreen = [int(worldToScreen[0]), worldToScreen[1]]
                self.currentAnimation.render(dest, worldToScreen)
                    
                #desenha o ponto da posição na tela...
                posToScreen = [int(self.position[0] - self.map.getWindow()[0]), int(self.map.window[3] - self.position[1])]
                pygame.draw.circle(dest,(0,0,0),posToScreen,3)
                print(self.currentAnimation.getCurrentSprite().getCollisionBox().computeOnScreen())