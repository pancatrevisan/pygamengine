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
        self.andaBaixo = False
        self.andaEsquerda = False
        self.andaCima = False
        self.velocidade = 60 #por segundo
    def atualiza(self, dt):
        if(self.andaDireita):
            self.posicao[0] += self.velocidade * dt
        if(self.andaEsquerda):
            self.posicao[0] -= self.velocidade * dt
        if(self.andaCima):
            self.posicao[1] -= self.velocidade * dt
        if(self.andaBaixo):
            self.posicao[1] += self.velocidade * dt

    def desenha(self, destino):
        pos = [int(self.posicao[0]), int(self.posicao[1])]
        destino.blit(self.imagem, pos)

class Inimigo:
    def __init__(self):
        self.velocidade = 120
        self.posicao = [0, -30]
        self.imagem = pygame.image.load("inimigo.png")
        self.tempoParaSpawnar = 4 #4 segundos... 
        self.tempoEsperando = 0
        self.ativo = False
    def atualiza(self, dt):
        if self.ativo:
            self.posicao[1] += self.velocidade * dt
            if(self.posicao[1] > 600):
                self.ativo = False
        else:
            self.tempoEsperando += dt
            if(self.tempoEsperando >= self.tempoParaSpawnar):
                self.tempoEsperando = 0
                self.ativo = True
    def desenha(self, destino):
        if(self.ativo):
            pos = [int(self.posicao[0]), int(self.posicao[1])]
            destino.blit(self.imagem, pos)

raptor = Raptor()
i = Inimigo()
clock = pygame.time.Clock()
while not sair:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sair = True
            if event.key == pygame.K_ESCAPE:
                sair = True
            elif event.key == pygame.K_RIGHT:
                raptor.andaDireita = True
            elif event.key == pygame.K_LEFT:
                raptor.andaEsquerda = True
            elif event.key == pygame.K_UP:
                raptor.andaCima = True
            elif event.key == pygame.K_DOWN:
                raptor.andaBaixo = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                raptor.andaDireita = False
            elif event.key == pygame.K_LEFT:
                raptor.andaEsquerda = False
            elif event.key == pygame.K_UP:
                raptor.andaCima = False
            elif event.key == pygame.K_DOWN:
                raptor.andaBaixo = False
            
    #limpeza
    janela.fill(BRANCO)
    dt = clock.tick(180)
    print(dt)
    #atualização dos estados...
    raptor.atualiza(dt/1000.0)
    i.atualiza(dt/1000.0)
    #desenho
    raptor.desenha(janela)
    i.desenha(janela)
    pygame.display.flip()
    
pygame.quit()  