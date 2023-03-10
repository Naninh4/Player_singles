import pygame
import os
import _curses
   
                         

# Configura a interface do usuário utilizando a biblioteca _curses. initscr() inicializa a tela padrão 
# para o uso da biblioteca curses. noecho() desativa a exibição de caracteres digitados pelo usuário. 
# cbreak() habilita o modo de entrada cbreak, que permite que as teclas digitadas pelo usuário sejam 
# imediatamente enviadas ao programa. keypad(True) habilita o teclado do terminal.

#inicializando a bib curses

cursor = _curses.initscr()

#desativando a exibição de caracteres digitados pelo usuário
_curses.noecho()

#Permite que as teclas digitadas pelo usuário sejam imediatamente emviadas para o programa
_curses.cbreak()

#habilita o teclado do terminal
cursor.keypad(True)

#Definindo teclas de controle

PLAY_KEY = ord('p')
PAUSE_KEY = ord(' ')
NEXT_KEY = ord('n')
STOP_KEY = ord('s')
QUIT_KEY = ord('q')

folder = r'C:\Users\Livia Saturno\Videos\4K Video Downloader\\'
music_list = os.listdir(folder)


# Inicializa o mixer do pygame
pygame.mixer.init()

cursor.nodelay(True)
def main():
# iterar sobre os arquivos na pasta de música
    for nome_arquivo in os.listdir(folder):
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
            
            key = cursor.getch() 

            # Carrega o arquivo de áudio
            pygame.mixer.music.load(musica)
            pygame.mixer.music.set_volume(1.0)
            print(pygame.mixer.music.get_volume())
            # Inicia a reprodução do arquivo
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                cursor.addstr(8, 3, f'\nReproduzindo... "{nome_arquivo}"\n')
                key = cursor.getch()
                if key == PAUSE_KEY:
                    cursor.nodelay(False)
                    # pygame.time.delay(5000)
                    pygame.mixer.music.pause()
                    key = cursor.getch()
                    _curses.napms(1)
                    if key == PLAY_KEY:
                            cursor.nodelay(False)
                            #  espera um 5 segundos para executar o comando
                            #  pygame.time.delay(5000)
                            pygame.mixer.music.unpause()
                            cursor.nodelay(True)
                            _curses.napms(1)
                elif key == QUIT_KEY:
                    exit()
                elif key == NEXT_KEY:
                    pygame.mixer.music.stop()
                    break
                _curses.napms(1)
            
            pygame.time.wait

# Começa a tocar a primeira música
main()
