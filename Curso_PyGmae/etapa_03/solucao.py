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
from pygame.constants import *


class Ator(pygame.sprite.Sprite):
    """ Classe Ator """

    def __init__(self, pos_x=0, pos_y=0):
        """ Construtor:  __init__()) -> instancia de ator """
        pygame.sprite.Sprite.__init__(self)
        self.poses = []
        self.pt_poses = 0 # ponteiro para pose atual.
        self.__pos_x = pos_x
        self.__pos_y = pos_y


    def inserir_pose(self, nome_arq_img):
        """ Armazena uma 'surface' dentro da lista poses """
        self.poses.append(pygame.image.load(nome_arq_img))
        self.image = self.poses[self.pt_poses]
        self.rect = self.image.get_rect()
        self.rect.x = self.__pos_x
        self.rect.y = self.__pos_y


    def update(self):
        """ Reimplementa updade() """
        self.pt_poses = self.pt_poses % len(self.poses)
        self.image = self.poses[self.pt_poses]
        self.pt_poses += 1




class Jogo:
    """ Classe Jogo """

    def __init__(self):
        """ Construtor:  __init__() -> instancia de jogo """
        pygame.init()
        self.tela = pygame.display.set_mode((800, 600))


    def criar_atores(self):
        """ Cria os atores """
        self.paola = Ator(0, 250)
        for x in range(1, 5):
            self.paola.inserir_pose("paola_ED_%02i.png" % x)
        self.ju = Ator(800-64, 250)
        for x in range(1, 5):
            self.ju.inserir_pose("ju_DE_%02i.png" % x)
        self.grupo_atores = pygame.sprite.RenderPlain((self.paola, self.ju))


    def atualizar_atores(self):
        """ Atualiza os atores """
        ret_tela = self.tela.get_rect()
        if (self.paola.rect.x < ret_tela.centerx - 64):
            self.paola.rect.x += 6
        if (self.ju.rect.x > ret_tela.centerx):
            self.ju.rect.x -= 6


    def repintar_tela(self):
        """ Repinta a tela """
        self.tela.fill((180, 180, 180))
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
