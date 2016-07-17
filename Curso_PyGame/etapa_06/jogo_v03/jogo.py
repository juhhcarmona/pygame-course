 #!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

#
#  Copylefth (c) 2009, Grudejo:
#    Aline Grazielle Silva Reis
#    Julia Carmona Almeida Chaves
#    Luziany Maria de Oliveira
#    Joyce Karoline Dare
#    Prof. Douglas Machado Tavares
#

import pygame
from ator import Ator
from menu import Menu
from menu_creditos import Menu_Creditos
from pygame.constants import *


class Jogo:
    """ Classe Jogo """

    def __init__(self):
        """ Construtor:  __init__() -> instancia de jogo """
        pygame.init()
        self.tela = pygame.display.set_mode((800, 600), FULLSCREEN)
        self.fim_jogo = False


    def criar_atores(self):
        """ Cria os atores """
        self.beneton = Ator(0, 250)
        self.beneton.inserir_estado("ED")
        for x in range(1, 5):
            self.beneton.inserir_pose("dados/imagens/beneton_ED_%02i.png" % x)
        self.grupo_atores = pygame.sprite.RenderPlain((self.beneton))


    def atualizar_atores(self):
        """ Atualiza os atores """
        ret_tela = self.tela.get_rect()
        if (self.beneton.rect.x < ret_tela.width - self.beneton.rect.width):
            self.beneton.rect.x += 8
        else:
            self.fim_jogo = True


    def repintar_tela(self):
        """ Repinta a tela """
        self.tela.fill((230, 230, 230))
        self.grupo_atores.update()
        self.grupo_atores.draw(self.tela)
        pygame.display.flip()


    def tratar_eventos_teclado(self, evento):
        """ Observa e trata os eventos """
        tecla = evento.key
        if ((tecla == K_ESCAPE) or (tecla == K_q)):
            raise SystemExit


    def tratar_eventos(self):
        """ Observa e trata os eventos """
        for evento in pygame.event.get():
            if (evento.type == QUIT):
                raise SystemExit
            if (evento.type == KEYDOWN):
                self.tratar_eventos_teclado(evento)


    def caminhar(self):
        """ Laco principal do Jogo - Caminhar """
        self.criar_atores()
        FPS = 8
        relogio = pygame.time.Clock()
        self.fim_jogo = False
        while (not self.fim_jogo):
            self.tratar_eventos()
            self.atualizar_atores()
            self.repintar_tela()
            relogio.tick(FPS)


    def rodar(self):
        """ Roda o jogo """
        menu = Menu(self.tela)
        menu_creditos = Menu_Creditos(self.tela)
        opcao = menu.rodar()
        while (opcao != 3):
            if (opcao == 1):
                self.caminhar()
            elif (opcao == 2):
                opcao = menu_creditos.rodar()
            opcao = menu.rodar()


if (__name__ == "__main__"):
    jogo = Jogo()
    jogo.rodar()
