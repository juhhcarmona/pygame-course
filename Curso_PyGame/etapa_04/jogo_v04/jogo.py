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
from ator import Ator
from pygame.constants import *


class Jogo:
    """ Classe Jogo """

    def __init__(self):
        """ Construtor:  __init__() -> instancia de jogo """
        pygame.init()
        self.tela = pygame.display.set_mode((800, 600), FULLSCREEN)


    def criar_atores(self):
        """ Cria os atores """
        self.bruno = Ator(50, 100)
        self.bruno.inserir_estado("EsqDir")
        for x in range(1, 5):
            self.bruno.inserir_pose("imagens/bruno_ED_%02i.png" % x)
        self.bruno.inserir_estado("DirEsq")
        for x in range(1, 5):
            self.bruno.inserir_pose("imagens/bruno_DE_%02i.png" % x)
        self.bruno.inserir_estado("CimaBaixo")
        for x in range(1, 5):
            self.bruno.inserir_pose("imagens/bruno_CB_%02i.png" % x)
        self.bruno.inserir_estado("BaixoCima")
        for x in range(1, 5):
            self.bruno.inserir_pose("imagens/bruno_BC_%02i.png" % x)
        self.grupo_atores = pygame.sprite.RenderPlain((self.bruno))


    def atualizar_atores(self):
        """ Atualiza os atores """
        retangulo = self.tela.get_rect()
        if (self.bruno.estado == "EsqDir"):
            self.bruno.rect.x += 8
        elif (self.bruno.estado == "CimaBaixo"):
            self.bruno.rect.y += 8
        elif (self.bruno.estado == "DirEsq"):
            self.bruno.rect.x -= 8
        elif (self.bruno.estado == "BaixoCima"):
            self.bruno.rect.y -= 8


    def repintar_tela(self):
        """ Repinta a tela """
        self.tela.fill((120, 120, 120))
        self.grupo_atores.update()
        self.grupo_atores.draw(self.tela)
        pygame.display.flip()


    def tratar_evento_teclado(self, evento):
        """ Observa e trata os eventos """
        tecla = evento.key
        if ((tecla == K_ESCAPE) or (tecla == K_q)):
            raise SystemExit
        elif (evento.type == KEYDOWN):
            if (evento.key == K_UP):
                self.bruno.estado = "BaixoCima"
            elif (evento.key == K_DOWN):
                self.bruno.estado = "CimaBaixo"
            elif (evento.key == K_LEFT):
                self.bruno.estado = "DirEsq"
            elif (evento.key == K_RIGHT):
                self.bruno.estado = "EsqDir"


    def tratar_eventos(self):
        """ Observa e trata os eventos """
        for evento in pygame.event.get():
            if (evento.type == QUIT):
                raise SystemExit
            if (evento.type == KEYDOWN):
                self.tratar_evento_teclado(evento)


    def rodar(self):
        """ Roda o jogo """
        self.criar_atores()
        FPS = 8
        relogio = pygame.time.Clock()
        while (True):
            self.tratar_eventos()
            self.atualizar_atores()
            self.repintar_tela()
            relogio.tick(FPS)


if (__name__ == "__main__"):
    jogo = Jogo()
    jogo.rodar()
