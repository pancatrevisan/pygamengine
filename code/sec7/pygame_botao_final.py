import pygame
pygame.init()
tamJanela = (800,600)
janela = pygame.display.set_mode(tamJanela)
pygame.display.set_caption("Minha Janela Pygame")
clock = pygame.time.Clock()
sair = False


class Botao:
    __tamImagem = []
    def __init__(self,pos, imagem):
        self.pos = pos
        self.imagem = imagem
        self.__tamImagem= [self.imagem.get_width(), self.imagem.get_height()]

    def click(self, mousePos):
        if(mousePos[0] >=self.pos[0] and mousePos[0] < self.pos[0] + self.__tamImagem[0]):
            if(mousePos[1] >= self.pos[1] and mousePos[1] < self.pos[1] + self.__tamImagem[1]):
                return True
        return False


botaoPlay = Botao([20,20],pygame.image.load("media/botaoPlay.png"))
botaoPause = Botao([20 + botaoPlay.imagem.get_width(),20],pygame.image.load("media/botaoPause.png"))
pygame.mixer.music.load("media/Overworld.ogg")

while not sair:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            sair = True
        if(event.type == pygame.MOUSEBUTTONDOWN):
            pos = pygame.mouse.get_pos()
            if(botaoPlay.click(pos)):
                pygame.mixer.music.play()
            elif botaoPause.click(pos):
                pygame.mixer.music.stop()



    #atualiza a lógica do jogo

    #desenha
    janela.fill((0,0,0))
    janela.blit(botaoPlay.imagem,botaoPlay.pos)
    janela.blit(botaoPause.imagem,botaoPause.pos)
    clock.tick(40)#automaticamente controla o FPS

    #atualiza a tela
    pygame.display.flip()#desenah a tela
pygame.quit()#finaliza ao sair do loop