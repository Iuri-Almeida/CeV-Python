import pygame

while True:
    pygame.init()
    pygame.mixer.music.load('021.mp3')
    pygame.mixer.music.play()
    pygame.event.wait()
