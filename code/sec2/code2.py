import pygame
pygame.init()
import math
tamanhoJanela = [ 800, 600]
janela = pygame.display.set_mode(tamanhoJanela)
pygame.display.set_caption("Eventos de Teclado")

sair = False
#definindo a cor
BRANCO = (255,255,255)

raptor = {
    "imagem": pygame.image.load('raptor.png'),
    "posicao": [10,10]
}

while not sair:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sair = True

    #limpeza
    janela.fill(BRANCO)
    #atualização dos estados...
    #desenho
    pygame.display.flip()
pygame.quit()  