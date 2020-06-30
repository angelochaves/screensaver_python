import sys
import pygame
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()
janela = pygame.display.set_mode([1366, 768], pygame.FULLSCREEN)

rodando = True

while rodando:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            rodando = False
        if event.type == pygame.KEYDOWN:
            rodando = False

    delta = clock.tick(30) / 1000

    janela.fill((0,0,0))
    pygame.display.update()

pygame.quit()