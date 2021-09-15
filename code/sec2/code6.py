import pygame
pygame.init()
import math
tamanhoJanela = [ 800, 600]
janela = pygame.display.set_mode(tamanhoJanela)
pygame.display.set_caption("Eventos de Teclado")

sair = False
#definindo a cor
BRANCO = (255,255,255)

clicado = False
raptor = {
    "imagem": pygame.image.load('raptor.png'),
    "posicao": [10,10]
}

while not sair:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: #esquerdo
                clicado = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1: #esquerdo
                clicado = False
        elif event.type == pygame.MOUSEMOTION:
            if(clicado):
                raptor['posicao'] = event.pos
    
    #limpeza
    janela.fill(BRANCO)
    #atualização dos estados...
    #desenho
    janela.blit(raptor['imagem'],raptor['posicao'])
    
    pygame.display.flip()
pygame.quit()  