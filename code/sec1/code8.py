import pygame
pygame.init()
import math
tamanhoJanela = [ 800, 600]
janela = pygame.display.set_mode(tamanhoJanela)
pygame.display.set_caption("Titulo da Janela")

sair = False
#definindo a cor
BRANCO = (255,255,255)

#carrega uma imagem de um arquivo
imagem = pygame.image.load("raptor.png")
while not sair:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair = True
    #limpeza
    janela.fill(BRANCO)
    #atualização dos estados...
    #desenho

    #desenha imagem
    janela.blit(imagem,[20,20])

    #new recebe a 'imagem' rotacionada em 45deg
    new = pygame.transform.rotate(imagem, 45)
    #desenha a imagem rotacionada
    janela.blit(new,[100,100])
    pygame.display.flip()
pygame.quit()  