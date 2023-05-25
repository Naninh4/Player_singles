import pygame
import os
import curses
import random  

# Configura a interface do usuário utilizando a biblioteca curses. initscr() inicializa a tela padrão 
# para o uso da biblioteca curses. noecho() desativa a exibição de caracteres digitados pelo usuário. 
# cbreak() habilita o modo de entrada cbreak, que permite que as teclas digitadas pelo usuário sejam 
# imediatamente enviadas ao programa. keypad(True) habilita o teclado do terminal.

#inicializando a bib curses

cursor = curses.initscr()

#desativando a exibição de caracteres digitados pelo usuário
curses.noecho()

#Permite que as teclas digitadas pelo usuário sejam imediatamente emviadas para o programa
curses.cbreak()

#habilita o teclado do terminal
cursor.keypad(True)

#Definindo teclas de controle

PLAY_KEY = ord('p')
PAUSE_KEY = ord(' ')
NEXT_KEY = ord('n')
STOP_KEY = ord('s')
QUIT_KEY = ord('q')
RANDOM_KEY = ord('r')
NUMERIC_KEY = ord('o')
folder = r'Musicas\\'


# Inicializa o mixer do pygame
pygame.mixer.init()

def main(music_list):
    cursor.nodelay(True)
   
    print(music_list)
    for nome_arquivo in music_list:
        musica = os.path.join(folder, nome_arquivo)
    
        # verificar se o arquivo é uma música suportada pelo pygame
        if nome_arquivo.endswith('.mp3') or nome_arquivo.endswith('.ogg') or nome_arquivo.endswith('.wav'):
            print(f'Tocando {nome_arquivo}...')

            cursor.clear()
            cursor.addstr(0, 0, 'Player de Música')
            cursor.addstr(2, 0, 'Teclas de Controle:')
            cursor.addstr(3, 4, 'P: Play')
            cursor.addstr(4, 4, 'Espaço: Pause')
            cursor.addstr(5, 4, 'Q: Sair')
            cursor.addstr(6, 4, 'N: Passar música')

            cursor.refresh()
            cursor.nodelay(True)
            key = cursor.getch() 

            # Carrega o arquivo de áudio
            pygame.mixer.music.load(musica)
            pygame.mixer.music.set_volume(0.2)
            print(pygame.mixer.music.get_volume())
            # Inicia a reprodução do arquivo
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                cursor.addstr(1, 3, f'Reproduzindo... "{nome_arquivo}" ',)
                cursor.refresh()
                key = cursor.getch()
                if key == PAUSE_KEY:
                    cursor.nodelay(False)
                    # pygame.time.delay(5000)
                    pygame.mixer.music.pause()
                    key = cursor.getch()
                    curses.napms(1)
                    if key == PLAY_KEY:
                            cursor.nodelay(False)
                            #  espera um 5 segundos para executar o comando
                            #  pygame.time.delay(5000)
                            pygame.mixer.music.unpause()
                            cursor.nodelay(True)
                            curses.napms(1)
                elif key == QUIT_KEY:
                    exit()
                elif key == NEXT_KEY:
                    pygame.mixer.music.stop()
                    break
                curses.napms(1)
            
            pygame.time.wait

# Começa a tocar a primeira música
cursor.addstr(0, 0, 'Player de Música')
cursor.addstr(2, 0, 'Teclas de Controle:')
cursor.addstr(3, 4, 'R: Aleatório')
cursor.addstr(4, 4, 'O: Ordem Numérica')
cursor.refresh()
key = cursor.getch() 
music_list = os.listdir(folder)
if key == RANDOM_KEY:
    music_list = os.listdir(folder)
    random.shuffle(music_list)
    main(music_list)
elif key == NUMERIC_KEY:
    music_list = os.listdir(folder)
    main(music_list)