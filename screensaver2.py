import sys
import pygame
from pygame import *
from pygame.locals import *
import random

pygame.init()

clock = pygame.time.Clock()
window = pygame.display.set_mode([1366, 768])#, pygame.FULLSCREEN)

running = True

class Chain:
    speed = 0
    size = 0
    fontsize = 0
    green = 0
    subset = ""
    posx0 = 0
    posy0 = 0

    def __init__(self):
        self.speed = random.triangular(10, 800)
        self.size = (int)(random.triangular(8, 33))
        self.fontsize = (int)(random.triangular(6, 43))
        self.green = (int)((15/(57-self.fontsize)) * 255)
        self.posx0 = (int)(random.triangular(0,(1367-self.fontsize)))
        self.posy0 = (int)(random.triangular(0,(769-self.fontsize)))
        self.subset = []
        for i in range(0,self.size+1):
            self.subset.append(chr((int)(random.triangular(33,127))))

while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            running = False
        if event.type == pygame.KEYDOWN:
            running = False

    window.fill((0,0,0))

    qtyChains = (int)(random.triangular(10, 100))
    for i in range(qtyChains):
        newchain = Chain()
        ffont = pygame.font.Font('arial.ttf', newchain.fontsize)
        fullss = "".join(newchain.subset)
        text = ffont.render(fullss, False, (0,newchain.green,0))
        textRect = text.get_rect()  
        textRect.x = newchain.posx0
        textRect.y = newchain.posy0
        window.blit(text, textRect)

    pygame.time.delay(500)
    pygame.display.update()

pygame.quit()