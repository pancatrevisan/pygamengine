import pygame
from Mapa360 import *
from AlvoMovel import *
pygame.init()


tamanhoJanela = [ 800, 600]
janela = pygame.display.set_mode(tamanhoJanela)
pygame.display.set_caption("Eventos de Teclado")


resolucaoInterna = [640, 480]
telaParaDesenhar = pygame.Surface((resolucaoInterna[0],resolucaoInterna[1]))

cenario = Mapa360('shootgame/fundo_cenario.png')
cenario.setWindow([0,0,resolucaoInterna[0],resolucaoInterna[1]])

#objetos
pistoleiro_1 = AlvoMovel('shootgame/pistoleiro1_normal.png','shootgame/pistoleiro1_acertado.png')
pistoleiro_1.setMap(cenario)


sair = False
#definindo a cor
BRANCO = (255,255,255)

#cria um objeto do jogo.
clock = pygame.time.Clock()

while not sair:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sair = True
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                cenario.rotate('R')
            elif event.key == pygame.K_LEFT or event.key==pygame.K_a:
                cenario.rotate('L')

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                cenario.rotate('N')
            elif event.key == pygame.K_LEFT or event.key==pygame.K_a:
                cenario.rotate('N')
            
    
    #limpeza
    janela.fill(BRANCO)
    telaParaDesenhar.fill(BRANCO)
    dt = clock.tick(30)    
    #limpeza
    janela.fill(BRANCO)
    #atualização dos estados...
    
    cenario.update(dt/1000.0)
    pistoleiro_1.update(dt/1000.0)

    #desenho
    cenario.render(telaParaDesenhar)
    pistoleiro_1.render(telaParaDesenhar)

    #redimensiona a tela de desenho para caber na tela.
    redim = pygame.transform.scale(telaParaDesenhar, (tamanhoJanela[0],tamanhoJanela[1]))    
    janela.blit(redim,[0,0])

    pygame.display.flip()
    
pygame.quit()  