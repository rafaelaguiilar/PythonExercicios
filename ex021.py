import pygame

# Inicializa o mixer do pygame
pygame.mixer.init()
''
# Carrega e toca o áudio
pygame.mixer.music.load("audio.mp3")
pygame.mixer.music.play()

# Mantém o programa rodando enquanto o áudio toca
input("Pressione Enter para sair...")