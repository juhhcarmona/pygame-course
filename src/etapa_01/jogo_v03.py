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
x_paola = 0
y_paola = 100
print ("Ctrl+C para encerrar ;-)")
while (True):
    x_paola += 4
    tela.blit(paola, (x_paola, y_paola))
    pygame.display.update()
pygame.display.quit()
