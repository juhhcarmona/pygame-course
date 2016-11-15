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


    def criar_atores(self):
        """ Cria os atores """
        self.bembeu = Ator(0, 100)
        for x in range(1, 5):
            self.bembeu.inserir_pose("imagens/bembeu_ED_%02i.png" % x)
        self.grupo_atores = pygame.sprite.RenderPlain((self.bembeu))


    def atualizar_atores(self):
        """ Atualiza os atores """
        ret_tela = self.tela.get_rect()
        if (self.bembeu.rect.x < ret_tela.width - self.bembeu.rect.width):
            self.bembeu.rect.x += 8


    def repintar_tela(self):
        """ Repinta a tela """
        self.tela.fill((200, 200, 200))
        self.grupo_atores.update()
        self.grupo_atores.draw(self.tela)
        pygame.display.flip()


    def tratar_eventos_teclado(self, evento):
        """ Trata o evento caso desejado """
        tecla = evento.key
        if ((tecla == K_ESCAPE) or (tecla == K_q)):
            raise SystemExit


    def tratar_eventos(self):
        """ Observa e trata eventos desejados """
        for evento in pygame.event.get():
            if (evento.type == QUIT):
                raise SystemExit
            if (evento.type == KEYDOWN):
                self.tratar_eventos_teclado(evento)


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
