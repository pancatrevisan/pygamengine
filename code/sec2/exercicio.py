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
    "posicao": [10,10],
    "andaDireita": False,
    "andaEsquerda": False,
    "andaCima":False,
    "andaBaixo":False
}
clock = pygame.time.Clock()
while not sair:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sair = True
            elif event.key == pygame.K_RIGHT:
                raptor['andaDireita'] = True
            elif event.key == pygame.K_LEFT:
                raptor['andaEsquerda'] = True
            elif event.key == pygame.K_UP:
                raptor['andaCima'] = True
            elif event.key == pygame.K_DOWN:
                raptor['andaBaixo'] = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                raptor['andaDireita'] = False
            elif event.key == pygame.K_LEFT:
                raptor['andaEsquerda'] = False
            elif event.key == pygame.K_UP:
                raptor['andaCima'] = False
            elif event.key == pygame.K_DOWN:
                raptor['andaBaixo'] = False
    #limpeza
    janela.fill(BRANCO)
    #atualização dos estados...
    if raptor['andaDireita']:
        raptor['posicao'][0]+= 2
    if(raptor['andaEsquerda']):
        raptor['posicao'][0]-= 2
    if(raptor['andaCima']):
        raptor['posicao'][1]-= 2
    if(raptor['andaBaixo']):
        raptor['posicao'][1]+= 2
    #desenho
    janela.blit(raptor['imagem'],raptor['posicao'])


    clock.tick(30)
    pygame.display.flip()
    
pygame.quit()  