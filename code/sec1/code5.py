import pygame
pygame.init()
import math
tamanhoJanela = [ 800, 600]
janela = pygame.display.set_mode(tamanhoJanela)
pygame.display.set_caption("Titulo da Janela")

sair = False
#definindo a cor
BRANCO = (255,255,255)
while not sair:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair = True
    #limpeza
    janela.fill(BRANCO)
    #atualização dos estados...
    #desenho

    #desenha uma elipse
    e_cor = (255,0,0)
    #surface, cor, RECT
    pygame.draw.ellipse(janela, e_cor,[350,300,100,50])

    #desenhar uma linha
    l_cor =(127,127,0)
    #suface, cor, pos inicial, pos final, largura
    pygame.draw.line(janela, l_cor, [10,10], [750, 550], 10)

    #desenhar um arco. math.pi = 180
    a_cor = (255,0,255)
    #surface, cor, RECT, angulo inicial, angulo final
    pygame.draw.arc(janela, a_cor, [20,200,100,100], math.pi, math.pi *2, 4)
    pygame.display.flip()
pygame.quit()  