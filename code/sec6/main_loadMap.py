import pygame
from GameMap import *
from Tileset import *
from Background import *
from BackgroundLayer import *

mapa = GameMap(None)
mapa.loadFromFile('map.json')


bkg = Background()
#bkgl = BackgroundLayer('jpbkg.png','REPEAT-X')
bkgl = BackgroundLayer('jpbkg.png','MOVE',[-90,0])
bkg.addLayer(bkgl)
mapa.setBackground(bkg)


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

andaCima = False
andaDireita = False
andaBaixo = False
andaEsquerda = False
while not sair:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sair = True
            elif event.key == pygame.K_RIGHT:
                andaDireita = True
            elif event.key == pygame.K_LEFT:
                andaEsquerda = True
            elif event.key == pygame.K_UP:
                andaCima = True
            elif event.key == pygame.K_DOWN:
                andaBaixo = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                andaDireita = False
            elif event.key == pygame.K_LEFT:
                andaEsquerda = False
            elif event.key == pygame.K_UP:
                andaCima = False
            elif event.key == pygame.K_DOWN:
                andaBaixo = False
    dt = clock.tick(60)    
    #limpeza
    janela.fill(BRANCO)
    telaParaDesenhar.fill(BRANCO)
    #atualização dos estados...
    d =[0,0]
    step =  100.0 * (dt/1000.0)
    
    if(andaEsquerda):
        d[0] = -step
    elif andaDireita:
        d[0] = step
    
    if(andaCima):
        d[1] = step
    elif andaBaixo:
        d[1] = -step
    mapa.update(dt/1000.0)
    mapa.moveWindow(d)

    #desenho
    mapa.render(telaParaDesenhar)


    #redimensiona a tela de desenho para caber na tela.
    redim = pygame.transform.scale(telaParaDesenhar, (tamanhoJanela[0],tamanhoJanela[1]))    
    janela.blit(redim,[0,0])

    pygame.display.flip()
    
pygame.quit()  