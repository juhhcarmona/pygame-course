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
        self.area = pygame.surface.Surface((2000, 2000))
        self.x_area = self.tela.get_rect().width / 2
        self.y_area = self.tela.get_rect().height / 2
        self.__carregar_mapa()
        self.__carregar_objetos()


    def __carregar_objetos(self):
        """ Carrega os objetos """
        arvore_01 = pygame.image.load("imagens/objetos/arvore_(.png")
        arvore_02 = pygame.image.load("imagens/objetos/arvore_).png")
        arvore_03 = pygame.image.load("imagens/objetos/arvore_{.png")
        arvore_04 = pygame.image.load("imagens/objetos/arvore_}.png")
        arvore_05 = pygame.image.load("imagens/objetos/arvore_].png")
        arvore_06 = pygame.image.load("imagens/objetos/arvore_[.png")
        poste = pygame.image.load("imagens/objetos/poste_p.png")
        flor = pygame.image.load("imagens/objetos/flor_f.png")
        vegetacao = pygame.image.load("imagens/objetos/vegetacao_v.png")
        tronco = pygame.image.load("imagens/objetos/tronco_t.png")
        piso = pygame.image.load("imagens/objetos/chao_,.png")
        self.objetos = {"(":arvore_01, ")":arvore_02,
                        "{":arvore_03, "}":arvore_04,
                        "]":arvore_05, "[":arvore_06,
                        "p":poste, "f":flor, "v":vegetacao,
                        "t":tronco, ".":piso}


    def __carregar_mapa(self):
        """ Carrega o mapa """
        arq_mapa = open("mapa.db", "r")
        self.mapa = arq_mapa.readlines()
        arq_mapa.close()


    def construir(self):
        """ Constroi o cenario """
        y = 0
        for linha in self.mapa:
            x = 0
            for simbolo in linha:
                self.area.blit(self.objetos["."], (x, y))
                if (simbolo in "(){}][vpft"):
                    self.area.blit(self.objetos[simbolo], (x, y))
                x = x + 100
            y = y + 100


    def repintar(self):
        """ Repinta o cenario """
        largura = self.area.get_rect().width
        altura = self.area.get_rect().height
        origem = (self.x_area, self.y_area, largura, altura)
        largura = self.tela.get_rect().width
        altura = self.tela.get_rect().height
        destino = (0, 0, largura, altura)
        self.tela.blit(self.area, destino, origem)


    def mover(self, dx, dy):
        """ Move o cenario """
        self.x_area += dx
        self.y_area += dy
        largura = self.tela.get_rect().width
        altura = self.tela.get_rect().height
        if not (0 <= self.x_area <= self.area.get_width() - largura):
            self.x_area -= dx
        if not (0 <= self.y_area <= self.area.get_height() - altura):
            self.y_area -= dy
