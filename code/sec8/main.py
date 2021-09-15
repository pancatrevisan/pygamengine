
import pygame
from PeixeBetta import *
from Worm import *
pygame.init()
tamanhoJanela = [ 800, 600]
janela = pygame.display.set_mode(tamanhoJanela)
pygame.display.set_caption("Eventos de Teclado")

sair = False
#definindo a cor
BRANCO = (255,255,255)

#cria um objeto do jogo.

peixe = PeixeBetta()
worm = Worm()
worm.position = [740, 0]

clock = pygame.time.Clock()


while not sair:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair = True
        elif event.type == pygame.KEYDOWN:
            if(event.key == pygame.K_ESCAPE):
                sair = True
    dt = clock.tick(30)    
    #limpeza
    janela.fill(BRANCO)
    #atualização dos estados...

    peixe.checkCollision(worm)

    peixe.update(dt/1000.0)
    #coltype = peixe.checkCollision(worm)
    #if(coltype['ME']!="NONE" or coltype['OTHER']!='NONE'):
    #    worm.alive = False
    if peixe.collides(worm):
        worm.alive = False
    #desenho
    peixe.render(janela)
    worm.render(janela)
    pygame.display.flip()
    
pygame.quit()  