#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      s201016279
#
# Created:     09/05/2017
# Copyright:   (c) s201016279 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import pygame
import sys
from pygame.locals import *
pygame.init()

WINDOW = pygame.display.set_mode((800,600))
pygame.display.set_caption("5 Horizontal Lines")

blue = (38,45,238)
red = (238,38,38)
green = (28,176,28)
pink = (238,29,196)
yellow = (255,255,34)
orange = (255,126,27)

FPS = 300
fpsClock = pygame.time.Clock()

y = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    WINDOW.fill(green)
    y = y + 1
    pygame.draw.circle(WINDOW,blue, (400,110), 100,10)
    pygame.draw.circle(WINDOW,red, (370,80), 15)
    pygame.draw.circle(WINDOW,red, (430,80), 15)
    pygame.draw.line(WINDOW,blue, (400,210), (400,400), 20)
    pygame.draw.line(WINDOW,blue, (400,250), (200,150), 20)
    pygame.draw.line(WINDOW,blue, (400,250), (600,150), 20)
    pygame.draw.line(WINDOW,blue, (400,400), (200,590), 20)
    pygame.draw.line(WINDOW,blue, (400,400), (600,590), 20)
    pygame.display.update()
    fpsClock.tick(FPS)