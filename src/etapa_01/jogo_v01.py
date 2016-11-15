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


pygame.init()
tela = pygame.display.set_mode((800, 600)) # tela eh uma 'surface'
paola = pygame.image.load("paola.png") # paola eh uma 'surface'
tela.blit(paola, (0, 100))
pygame.display.update()
pygame.display.quit()
