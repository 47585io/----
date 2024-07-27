import pygame
import sys
from scenes import Scenes

pygame.init()
screen = pygame.display.set_mode((800, 600))
scenes = Scenes(rect=(0, 0, 1000, 1000))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    scenes.update()
    scenes.render(screen)
    pygame.display.flip()
    
pygame.quit()
sys.exit()
