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


class Ator(pygame.sprite.Sprite):
    """ Classe Ator """

    def __init__(self, pos_x=0, pos_y=0):
        """ Construtor:  __init__()) -> instancia de ator """
        pygame.sprite.Sprite.__init__(self)
        self.poses = {}
        self.__pt_pose = 0 # ponteiro para pose atual.
        self.__pos_x = pos_x
        self.__pos_y = pos_y


    def inserir_estado(self, estado):
        """ Insere um novo estado """
        self.estado = estado
        self.poses[estado] = []


    def inserir_pose(self, nome_arq_img):
        """ Armazena uma 'surface' dentro da lista do estado corrente """
        self.poses[self.estado].append(pygame.image.load(nome_arq_img))
        self.image = self.poses[self.estado][self.__pt_pose]
        self.rect = self.image.get_rect()
        self.rect.x = self.__pos_x
        self.rect.y = self.__pos_y


    def update(self):
        """ Reimplementa updade() """
        self.__pt_pose = self.__pt_pose % len(self.poses[self.estado])
        self.image = self.poses[self.estado][self.__pt_pose]
        self.__pt_pose += 1
