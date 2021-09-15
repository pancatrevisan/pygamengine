import pygame
class GameObject:
    def __init__(self, position = [0,0]):
        #posição do personagem. Parte inferior, centralizada no sprite.
        #
        # ---------
        # |        |
        # |        |
        # |____P___|
        self.position = position#posicao no mundo.
        self.animations ={} #animações. um dicionário
        self.currentAnimation = None

    def getCurrentCollisionBox(self):
        return self.currentAnimation.getCurrentSprite().getCollisionBox()

    def onScreen(self):
        return False

    def collides(self, anotherObject):
        myColl = self.getCurrentCollisionBox().computeTranslated()
        aoColl = anotherObject.getCurrentCollisionBox().computeTranslated()
        print(myColl)
        print(aoColl)
        return myColl.collides(aoColl)

     def checkCollision(self, anotherObject):
        anotherBoxColl = anotherObject.getCurrentCollisionBox().computeTranslated()
        myColl = self.getCurrentCollisionBox().computeTranslated()
        coltype = myColl.collisionType(anotherBoxColl)
        
        return coltype



    #método de atualização, para ser sobrescrito em subclasses.
    def update(self, dt):
        raise Exception("Implemente o método de atualização :)")
    
    def render(self, dest):
        if self.currentAnimation != None:
            #TODO: 600 vai ser trocado pela altura do mapa.
            print('-------------------------')
            print("pos: " + str(self.position))
            print("algn: " +str(self.currentAnimation.getCurrentSprite().getAlign()))
            
            worldToScreen = [self.position[0] - self.currentAnimation.getCurrentSprite().getAlign()[0], 0]
            worldToScreen[1] = self.position[1]+self.currentAnimation.getCurrentSprite().getHeight()
            worldToScreen[1] = 600 - worldToScreen[1]
            worldToScreen = [int(worldToScreen[0]), worldToScreen[1]]
            self.currentAnimation.render(dest, worldToScreen)

            print("scr: " +str(worldToScreen))
            posToScreen = [int(self.position[0]), int(600 - self.position[1])]
            pygame.draw.circle(dest,(0,0,0),posToScreen,3)
    def addAnimation(self, animation):
        animation.setOwner(self)
        self.animation[animation.name] = animation