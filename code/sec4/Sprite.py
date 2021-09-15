import pygame
class Sprite:
    def __init__(self, imageFile, displayTime, owner = None, animation = None):
        self.image = pygame.image.load(imageFile)
        self.displayTime = displayTime
        self.animation = animation
        #posicao que será usada para desenhar o sprite.
        #por padrão, o meio do sprite
        self.alignPosition = [int(self.image.get_width()/2), int(self.image.get_height())]
        
    def getAlign(self):
        return self.alignPosition
    def setAnimation(self, animation):
        self.animation = animation
    def getWidth(self):
        return self.image.get_width()
    def getHeight(self):
        return self.image.get_height()
    
    #desenha o sprite na posicao (na surface) informada (onscreenPosition)
    def render(self, dest, onScreenPosition):
        dest.blit(self.image, onScreenPosition)


    

