import sys
import pygame
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()
figura = pygame.image.load("./figura.jpg")
janela = pygame.display.set_mode([1366, 768])

rodando = True

x = 357
y = 54
sx = 130
sy = 50

while rodando:
    for event in pygame.event.get():
        if event.type == QUIT:
            rodando = False

    delta = clock.tick(30) / 1000
    x += sx * delta
    y += sy * delta

    if x + 204 > janela.get_width() or x < 0:
        sx *= -1

    if y + 192 > janela.get_height() or y < 0:
        sy *= -1

    janela.fill((0,0,0))
    janela.blit(figura, (x,y))
    pygame.display.update()

pygame.quit()