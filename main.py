from pickle import FALSE
import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("SPACE INVEDORS")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,0))
    pygame.display.update()

