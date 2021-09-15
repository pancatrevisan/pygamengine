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

    #desenhar uma parte da imagem: subsurface(inicioX, inicioY, largura, altura)
    janela.blit(imagem.subsurface(10,10,50,50),[100,100])
    pygame.display.flip()
pygame.quit()  