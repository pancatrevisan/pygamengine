import pygame
from GameMap import *
from Tileset import *

t = Tileset('tileset_jungle.png',32)
map = GameMap(t)
map.setSize(20,20)

map.setCell(1,0, t.getTile("t_0"))
map.setCell(1,1, t.getTile("t_1"))
map.setCell(1,2, t.getTile("t_1"))
map.setCell(1,3, t.getTile("t_1"))
map.setCell(1,4, t.getTile("t_1"))
map.setCell(1,5, t.getTile("t_2"))



map.setCell(0,0, t.getTile("t_3"))
map.setCell(0,1, t.getTile("t_4"))
map.setCell(0,2, t.getTile("t_4"))
map.setCell(0,3, t.getTile("t_4"))
map.setCell(0,4, t.getTile("t_4"))
map.setCell(0,5, t.getTile("t_5"))


print(t.tiles)
pygame.init()
tamanhoJanela = [ 800, 600]
resolucaoInterna = [400, 300]

telaParaDesenhar = pygame.Surface((resolucaoInterna[0],resolucaoInterna[1]))


janela = pygame.display.set_mode(tamanhoJanela)
pygame.display.set_caption("Eventos de Teclado")

sair = False
#definindo a cor
BRANCO = (255,255,255)

#cria um objeto do jogo.
clock = pygame.time.Clock()


while not sair:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair = True
    dt = clock.tick(30)    
    #limpeza
    janela.fill(BRANCO)
    telaParaDesenhar.fill(BRANCO)
    #atualização dos estados...
    
    #desenho
    map.render(telaParaDesenhar)


    #redimensiona a tela de desenho para caber na tela.
    redim = pygame.transform.scale(telaParaDesenhar, (tamanhoJanela[0],tamanhoJanela[1]))    
    janela.blit(redim,[0,0])

    pygame.display.flip()
    
pygame.quit()  