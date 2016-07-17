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
from pygame.constants import *


class Jogo:
    """ Classe Jogo """

    def __init__(self):
        """ Construtor:  __init__() -> instancia de jogo """
        pygame.init()
        self.tela = pygame.display.set_mode((800, 600))
        self.fim_jogo = False


    def criar_atores(self):
        """ Cria os atores """
        self.wil = Ator(50, 100)
        self.wil.inserir_estado("EsqDir")
        for x in range(1, 5):
            self.wil.inserir_pose("imagens/wil_ED_%02i.png" % x)
        self.wil.inserir_estado("DirEsq")
        for x in range(1, 5):
            self.wil.inserir_pose("imagens/wil_DE_%02i.png" % x)
        self.wil.inserir_estado("CimaBaixo")
        for x in range(1, 5):
            self.wil.inserir_pose("imagens/wil_CB_%02i.png" % x)
        self.wil.inserir_estado("BaixoCima")
        for x in range(1, 5):
            self.wil.inserir_pose("imagens/wil_BC_%02i.png" % x)
        self.grupo_atores = pygame.sprite.RenderPlain((self.wil))


    def atualizar_atores(self):
        """ Atualiza os atores """
        retangulo = self.tela.get_rect()
        if (self.wil.estado == "EsqDir"):
            if (self.wil.rect.x < retangulo.width - 64 - 50):
                self.wil.rect.x += 8
            else:
                self.wil.estado = "CimaBaixo"
        elif (self.wil.estado == "CimaBaixo"):
            if (self.wil.rect.y < retangulo.height - 100 - 100):
                self.wil.rect.y += 8
            else:
                self.wil.estado = "DirEsq"
        elif (self.wil.estado == "DirEsq"):
            if (self.wil.rect.x > 0 + 50):
                self.wil.rect.x -= 8
            else:
                self.wil.estado = "BaixoCima"
        elif (self.wil.estado == "BaixoCima"):
            if (self.wil.rect.y > 0 + 100):
                self.wil.rect.y -= 8
            else:
                self.wil.estado = "EsqDir"


    def repintar_tela(self):
        """ Repinta a tela """
        self.tela.fill((255, 255, 255))
        self.grupo_atores.update()
        self.grupo_atores.draw(self.tela)
        pygame.display.flip()


    def tratar_evento_teclado(self, evento):
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
                self.tratar_evento_teclado(evento)


    def rodar(self):
        """ Roda o jogo """
        self.criar_atores()
        FPS = 8
        relogio = pygame.time.Clock()
        while (not self.fim_jogo):
            self.tratar_eventos()
            self.atualizar_atores()
            self.repintar_tela()
            relogio.tick(FPS)


if (__name__ == "__main__"):
    jogo = Jogo()
    jogo.rodar()
