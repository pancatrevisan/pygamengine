import pygame
pygame.init()
import math
tamanhoJanela = [ 800, 600]
janela = pygame.display.set_mode(tamanhoJanela)
pygame.display.set_caption("Eventos de Teclado")

sair = False
#definindo a cor
BRANCO = (255,255,255)

class Raptor:
    def __init__(self):
        self.imagem = pygame.image.load('raptor.png')
        self.posicao = [10.0,10.0]
        self.andaDireita = False
        self.velocidade = 60 #por segundo
    def atualiza(self, dt):
        if(self.andaDireita):
            self.posicao[0] += self.velocidade * dt
    def desenha(self, destino):
        pos = [int(self.posicao[0]), int(self.posicao[1])]
        destino.blit(self.imagem, pos)

raptor = Raptor()
clock = pygame.time.Clock()
while not sair:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sair = True
            elif event.key == pygame.K_RIGHT:
                raptor.andaDireita = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                raptor.andaDireita = False
    #limpeza
    janela.fill(BRANCO)
    dt = clock.tick(180)
    print(dt)
    #atualização dos estados...
    raptor.atualiza(dt/1000.0)
    #desenho
    raptor.desenha(janela)


    
    pygame.display.flip()
    
pygame.quit()  