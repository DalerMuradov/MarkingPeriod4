import sys
import pygame

class CreditScreen:
    def __init__(self, screen, music_handler, current_playing_button):
        self.screen = screen
        self.screen_width, self.screen_height = screen.get_size()
        self.background_img = pygame.image.load("CreditScreen.png")
        self.background_img = pygame.transform.scale(self.background_img, (self.screen_width, self.screen_height))
        self.music_handler = music_handler
        self.current_playing_button = current_playing_button
        self.fade_speed = 2

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def draw(self):
        self.screen.blit(self.background_img, (0, 0))
        self.current_playing_button.draw(self.screen)

    def playMusic(self):
        self.music_handler.CreditMusic()

    def run(self):
        self.playMusic()
        while True:
            self.handleEvents()
            self.current_playing_button.update_alt_image("CurrentlyPlaying2.png", (self.screen_width - 100, 50))
            self.current_playing_button.update()
            self.draw()
            pygame.display.flip()
