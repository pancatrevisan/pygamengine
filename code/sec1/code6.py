import pygame
pygame.init()
import math
tamanhoJanela = [ 800, 600]
janela = pygame.display.set_mode(tamanhoJanela)
pygame.display.set_caption("Titulo da Janela")

sair = False
#definindo a cor
BRANCO = (255,255,255)

#cria uma fonte
fonte = pygame.font.Font(None, 24)

while not sair:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair = True
    #limpeza
    janela.fill(BRANCO)
    #atualização dos estados...
    #desenho

    t_cor = (0,127,50)
    texto = fonte.render("Meu Texto", True, t_cor)
    #blit desenha uma imagem em outra. 
    #A janela é uma imagem para o pygame. o texto também.
    janela.blit(texto, [50,50]) 
    pygame.display.flip()
pygame.quit()  