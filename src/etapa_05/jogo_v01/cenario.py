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


class Cenario:
    """ Classe Cenario """

    def __init__(self, tela):
        """ Construtor:  __init__() -> instancia de cenario """
        self.tela = tela
        self.poste = pygame.image.load("imagens/objetos/poste_p.png")
        self.flor = pygame.image.load("imagens/objetos/flor_f.png")
        self.vegetacao = pygame.image.load("imagens/objetos/vegetacao_v.png")
        self.tronco = pygame.image.load("imagens/objetos/tronco_t.png")
        self.carregar_mapa()


    def carregar_mapa(self):
        """ Carrega o mapa """
        arq_mapa = open("mapa.db", "r")
        self.mapa = arq_mapa.readlines()
        arq_mapa.close()


    def reconstruir_cenario(self):
        """ Reconstroi o cenario """
        y = 0
        for linha in self.mapa:
            x = 0
            for simbolo in linha:
                if (simbolo == "p"):
                    self.tela.blit(self.poste, (x, y))
                elif (simbolo == "f"):
                    self.tela.blit(self.flor, (x, y))
                elif (simbolo == "v"):
                    self.tela.blit(self.vegetacao, (x, y))
                elif (simbolo == "t"):
                    self.tela.blit(self.tronco, (x, y))
                x += 100
            y += 100
