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
        self.carregar_objetos()
        self.carregar_mapa()


    def carregar_objetos(self):
        """ Carrega os objetos """
        poste = pygame.image.load("imagens/objetos/poste_p.png")
        flor = pygame.image.load("imagens/objetos/flor_f.png")
        vegetacao = pygame.image.load("imagens/objetos/vegetacao_v.png")
        tronco = pygame.image.load("imagens/objetos/tronco_t.png")
        self.objetos = {"v":vegetacao,
                        "p":poste,
                        "f":flor,
                        "t":tronco}


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
                if (simbolo in "vpft"):
                    self.tela.blit(self.objetos[simbolo], (x, y))
                x = x + 100
            y = y + 100
