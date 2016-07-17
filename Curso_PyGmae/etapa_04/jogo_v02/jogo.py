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
        self.gasper = Ator(800-64, 250)
        self.gasper.inserir_estado("Direta_Esquerda")
        for x in range(1, 5):
            self.gasper.inserir_pose("imagens/gasper_DE_%02i.png" % x)
        self.grupo_atores = pygame.sprite.RenderPlain((self.gasper))


    def atualizar_atores(self):
        """ Atualiza os atores """
        retangulo = self.tela.get_rect()
        if (self.gasper.rect.x > 0):
            self.gasper.rect.x -= 8


    def repintar_tela(self):
        """ Repinta a tela """
        self.tela.fill((80, 80, 80))
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
