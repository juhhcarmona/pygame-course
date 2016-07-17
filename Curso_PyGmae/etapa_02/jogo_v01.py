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

import pygame, sys


class Jogo:
    """ Classe Jogo """

    def __init__(self):
        """ Construtor:  __init__() -> instancia de jogo """
        pygame.init()
        self.tela = pygame.display.set_mode((800, 600))


    def criar_atores(self):
        """ Cria os atores """
        self.paola = pygame.image.load("paola.png")
        self.x_paola, self.y_paola = 0, 100


    def atualizar_atores(self):
        """ Atualiza os atores """
        # Metodo ainda nao implementado
        pass


    def repintar_tela(self):
        """ Repinta a tela """
        self.tela.blit(self.paola, (self.x_paola, self.y_paola))
        pygame.display.update()


    def tratar_eventos(self):
        """ Observa e trata os eventos """
        for evento in pygame.event.get():
            if (evento.type == pygame.QUIT):
                pygame.display.quit()
                sys.exit()


    def rodar(self):
        """ Roda o jogo """
        self.criar_atores()
        while (True):
            self.tratar_eventos()
            self.atualizar_atores()
            self.repintar_tela()


if (__name__ == "__main__"):
    jogo = Jogo()
    jogo.rodar()
