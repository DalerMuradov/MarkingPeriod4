import pygame



class MusicHandler:
    def __init__(self, intro_music_file, credit_music_file):
        pygame.mixer.init()
        self.intro_music = pygame.mixer.Sound(intro_music_file)
        self.credit_music = pygame.mixer.Sound(credit_music_file)
        self.current_music = self.intro_music

    def play(self, loop=-1):
        self.current_music.play(loop)

    def stop(self):
        self.current_music.stop()

    def Intromusic(self):
        self.stop()
        self.current_music = self.intro_music
        self.play(-1)

    def CreditMusic(self):
        self.stop()
        self.current_music = self.credit_music
        self.play(-1)
