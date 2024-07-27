
import pygame
import pygame.surface
from pygame.rect import Rect
import sys

pygame.init()

screen = pygame.display.set_mode((800, 600))

image = pygame.image.load('res/pictures/background/meadow.png')
x = 0
y = 0
running = True
while running:
    
    screen.fill((0, 0, 0))
    screen.blit(image, (x, y))  # ? (100, 100) ?????
    x-=10
    if(x < screen.get_width()-image.get_width()):
        x = 0
    
    # ??????
    pygame.display.flip()

    # ????
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# ?? Pygame
pygame.quit()
sys.exit()
