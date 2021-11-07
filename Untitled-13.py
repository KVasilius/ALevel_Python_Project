import pygame

pygame.init()
screen = pygame.display.set_mode((500,500))
r1 = pygame.draw.rect(screen,(255,255,255),(15,15,15,15))
while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: pygame.quit()
    """
import pygame, sys
from pygame.locals import *

def main():
    pygame.init()

    DISPLAY=pygame.display.set_mode((500,400),0,32)

    WHITE=(255,255,255)
    BLUE=(0,0,255)

    DISPLAY.fill(WHITE)

    pygame.draw.rect(DISPLAY,BLUE,(200,150,100,50))
2
    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

main()
"""