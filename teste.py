import mad
import pygame
tempo =  mad.MadFile("musica.mp3")
tempo_ms = tempo.total_time()
pygame.time.delay(tempo_ms)