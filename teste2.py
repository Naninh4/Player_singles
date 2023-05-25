import tkinter as tk
import pygame
import os

folder = r'Musicas\\'
music_list = os.listdir(folder)

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("LivinhaSingles")

        # Inicializa o mixer do Pygame
        pygame.mixer.init()

        # Variáveis
        self.playing = False
        self.paused = False
        self.current_song = None

        # Frames
        

        # Define a posição da janela e exibe
        
        self.control_frame = tk.Frame(self.root)
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width - 400) // 2  # 400 é a largura da janela
        y = (screen_height - 300) // 2  # 300 é a altura da janela
        root.geometry(f"400x300+{x}+{y}")
        self.control_frame.pack(padx=80, pady=125) #definindo tamanho da janela

        # Botões de controle
        self.play_button = tk.Button(self.control_frame, text="Play", command=self.play)
        self.play_button.pack(side="left", padx=5)

        self.pause_button = tk.Button(self.control_frame, text="Pause", command=self.pause, state="disabled")
        self.pause_button.pack(side="left", padx=5)

        self.stop_button = tk.Button(self.control_frame, text="Stop", command=self.stop, state="disabled")
        self.stop_button.pack(side="left", padx=5)

        # self.add_button = tk.Button(self.control_frame, text="Add", command=self.add_song)
        # self.add_button.pack(side="left", padx=5)

    
    def play(self):
        for nome_arquivo in music_list:
            self.current_song = os.path.join(folder, nome_arquivo)
        
            # verificar se o arquivo é uma música suportada pelo pygame
            if nome_arquivo.endswith('.mp3') or nome_arquivo.endswith('.ogg') or nome_arquivo.endswith('.wav'):
                if not self.playing:
                    print(f'Tocando {nome_arquivo}...')
  
  # Criando um Label com o texto 'Curso Python Progressivo'
                    self.texto = tk.Label(self.control_frame, text='Curso Python Progressivo! ' )

  # Chamando o metodo pack() da função Label()
                    self.texto.pack(side="top",padx=10)


                    pygame.mixer.music.load(self.current_song)
                    pygame.mixer.music.play()
                    self.playing = True
                    self.paused = False
                    self.play_button.config(state="disabled")
                    self.pause_button.config(state="normal")
                    self.stop_button.config(state="normal")

                # while pygame.mixer.music.get_busy():
                #     print()
                
        # if self.current_song:
        #     if not self.playing:
        #         pygame.mixer.music.load(self.current_song)
        #         pygame.mixer.music.play()
        #         self.playing = True
        #         self.paused = False
        #         self.play_button.config(state="disabled")
        #         self.pause_button.config(state="normal")
        #         self.stop_button.config(state="normal")
        # else:
        #     self.add_song()

    def pause(self):
        if self.playing:
            if not self.paused:
                pygame.mixer.music.pause()
                self.paused = True
                self.play_button.config(state="normal")
                self.pause_button.config(text="Resume", command=self.play)
                
        else:
            self.play()
  

    def stop(self):
        if self.playing or self.paused:
            pygame.mixer.music.stop()
            self.playing = False
            self.paused = False
            self.play_button.config(state="normal")
            self.pause_button.config(text="Pause", state="disabled")
            self.stop_button.config(state="disabled")


root = tk.Tk()
#root é a biblioteca que cria a interface
app = MusicPlayer(root)

root.mainloop()