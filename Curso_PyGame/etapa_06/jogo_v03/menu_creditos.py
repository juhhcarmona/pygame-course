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
from pygame.constants import *


class Menu_Creditos:
    """ Classe Menu Creditos """

    def __init__(self, tela):
        """ Construtor:  __init__() -> instancia de jogo """
        self.tela = tela
        self.opcao = 1
        self.enter = False


    def tratar_eventos_menu(self):
        """ Observa e trata eventos desejados """
        for evento in pygame.event.get():
            if (evento.type == QUIT):
                raise SystemExit
            elif (evento.type == KEYDOWN):
                if ((evento.key == K_ESCAPE) or (evento.key == K_q)):
                    raise SystemExit
                elif (evento.key == K_RETURN):
                    self.enter = True


    def repintar_menu(self):
        """ Repinta o menu """
        fundo = pygame.image.load("dados/imagens/creditos.png")
        self.tela.blit(fundo, (0, 0))
        rotulo = " [ Voltar ] "
        cor = (0, 0, 0)
        fonte = pygame.font.Font("dados/fontes/dejavu_sans.ttf", 25)
        fonte.set_bold(True)
        fonte_rend = fonte.render(rotulo, True, cor)
        self.tela.blit(fonte_rend, (500, 500))
        pygame.display.update()


    def rodar(self):
        """ Roda o menu """
        self.enter = False
        while (True):
            self.tratar_eventos_menu()
            self.repintar_menu()
            if (self.enter):
                return self.opcao
