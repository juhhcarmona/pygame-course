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

import pygame, time
from ator import Ator
from menu import Menu
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
        self.luzi = Ator(336, 500)
        self.luzi.inserir_estado("BC")
        for x in range(1, 5):
            self.luzi.inserir_pose("dados/imagens/luzi_BC_%02i.png" % x)
        self.beneton = Ator(400, 0)
        self.beneton.inserir_estado("CB")
        for x in range(1, 5):
            self.beneton.inserir_pose("dados/imagens/beneton_CB_%02i.png" % x)
        self.grupo_atores = pygame.sprite.RenderPlain((self.luzi, self.beneton))


    def atualizar_atores(self):
        """ Atualiza os atores """
        ret_tela = self.tela.get_rect()
        if (self.luzi.rect.y > 0):
            self.luzi.rect.y -= 4
        else:
            self.fim_jogo = True
        if (self.beneton.rect.y < 500):
            self.beneton.rect.y += 6


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
        FPS = 8
        relogio = pygame.time.Clock()
        self.fim_jogo = False
        tic, tac = time.time(), 0
        while (tac <= 1.8):
            self.tratar_eventos()
            self.atualizar_atores()
            self.repintar_tela()
            tac = time.time() - tic
            relogio.tick(FPS)


    def rodar(self):
        """ Roda o Jogo """
        self.criar_atores()
        menu = Menu(self.tela)
        opcao = menu.rodar()
        while (opcao != 2):
            if (opcao == 1):
                self.caminhar()
            menu.opcao = 2
            opcao = menu.rodar()


if (__name__ == "__main__"):
    jogo = Jogo()
    jogo.rodar()
