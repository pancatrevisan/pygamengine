import pygame
from PeixeBetta import *
pygame.init()
tamanhoJanela = [ 800, 600]
janela = pygame.display.set_mode(tamanhoJanela)
pygame.display.set_caption("Eventos de Teclado")

sair = False
#definindo a cor
BRANCO = (255,255,255)

#cria um objeto do jogo.

peixe = PeixeBetta()

clock = pygame.time.Clock()


while not sair:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair = True
    dt = clock.tick(30)    
    #limpeza
    janela.fill(BRANCO)
    #atualização dos estados...
    peixe.update(dt/1000.0)
    #desenho
    peixe.render(janela)
    pygame.display.flip()
    
pygame.quit()  