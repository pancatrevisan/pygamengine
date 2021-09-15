import pygame
pygame.init()
import math
tamanhoJanela = [ 800, 600]
janela = pygame.display.set_mode(tamanhoJanela)
pygame.display.set_caption("Eventos de Teclado")

sair = False
#definindo a cor
BRANCO = (255,255,255)

pontos = []
while not sair:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: #esquerdo
                pontos.append(event.pos)
            
    #limpeza
    janela.fill(BRANCO)
    #atualização dos estados...
    #desenho
    c_cor = (255,0,0)
    for p in pontos:
        pygame.draw.circle(janela, c_cor, p, 10)
    
    pygame.display.flip()
pygame.quit()  