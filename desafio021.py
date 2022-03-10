import pygame

# Iniciando mixer Pygame
pygame.mixer.init()

# Iniciando o Pygame
pygame.init()

pygame.mixer.music.load('kimi_no_shiranai_monogatari.mp3')
pygame.mixer.music.play(loops=0,start=0.0)
pygame.event.wait