import pygame
caminho = input('Coloque o caminho da música: ')
pygame.mixer.init()
pygame.mixer.music.load(caminho) # caminho da url da música dentro dessa parenteses.
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
