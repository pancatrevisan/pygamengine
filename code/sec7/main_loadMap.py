import pygame
import math
from SFXManager import *

pygame.init()
tamanhoJanela = [ 800, 600]
resolucaoInterna = [400, 300]
telaParaDesenhar = pygame.Surface((resolucaoInterna[0],resolucaoInterna[1]))

sfxManager = SFXManager()

#https://freesound.org/people/dtrostli/sounds/316874/
sfxManager.add('cymball',pygame.mixer.Sound('sfx/316874__dtrostli__tr-dhita-cymbal02.wav'))
janela = pygame.display.set_mode(tamanhoJanela)
pygame.display.set_caption("Sons")

sair = False
#definindo a cor
BRANCO = (255,255,255)

#cria um objeto do jogo.
clock = pygame.time.Clock()

center = [200,200]
radius = 100
cymbal_img = pygame.image.load('cymball.png')
def clicouCirculo(raio, centro, p):
    v = [p[0]-centro[0], p[1]-centro[1]]

    d = math.sqrt(v[0]*v[0] + v[1]*v[1]) 
    if d <= raio:
        return True
    else:
        return False
    
while not sair:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sair = True
        elif event.type == pygame.KEYUP:
            pass
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if(clicouCirculo(radius,center, pos)):
                sfxManager.play('cymball')

    dt = clock.tick(60)    
    #limpeza
    janela.fill(BRANCO)
    telaParaDesenhar.fill(BRANCO)
    #atualização dos estados...
    
    #desenho
    janela.blit(cymbal_img, [int(center[0]-center[0]/2), int(center[1]-center[1]/2)])
    #pygame.draw.circle(janela, (122,0,0),center,radius)
    
    
    

    pygame.display.flip()
    
pygame.quit()  