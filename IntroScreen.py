import sys
import pygame

from Button import CurrentlyPlayingButton, Button
from CreditScreen import CreditScreen


class IntroScreen:
    def __init__(self, screen, music_handler, game):
        self.screen = screen
        self.screen_width, self.screen_height = screen.get_size()
        self.background_img = pygame.image.load("Intro.png")
        self.game = game

        button_x = 150
        self.playButton = Button("Play.png", (button_x, 200))
        self.quitButton = Button("Quit.png", (button_x, 300))
        self.creditsButton = Button("Credit.png", (button_x, 400))

        button_width = 150
        button_height = 30
        button_y = 700
        button_x = 700
        self.currentlyPlayingButton = CurrentlyPlayingButton("CurrentlyPlaying1.png", (button_x, button_y),
                                                             (button_width, button_height))

        self.music_handler = music_handler

        self.fadeDirection = 1
        self.fadeSpeed = 2
        self.alpha = 255
        self.show_credit_screen = False

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if self.playButton.is_clicked(event):
                self.game.startPlayScreen()
            elif self.quitButton.is_clicked(event):
                pygame.quit()
                sys.exit()
            elif self.creditsButton.is_clicked(event):
                self.music_handler.stop()
                self.show_credit_screen = True
                new_currently_playing_button = CurrentlyPlayingButton("CurrentlyPlaying1.png",
                                                                      (self.screen_width - 100, 50),
                                                                      (150, 30))
                credit_screen = CreditScreen(self.screen, self.music_handler, new_currently_playing_button)
                credit_screen.run()

    def update(self):
        self.playButton.update()
        self.quitButton.update()
        self.creditsButton.update()
        self.currentlyPlayingButton.update()

        self.alpha += self.fadeDirection * self.fadeSpeed
        if self.alpha > 255:
            self.alpha = 255
            self.fadeDirection = -1
        elif self.alpha < 0:
            self.alpha = 0
            self.fadeDirection = 1
        temp_img = self.currentlyPlayingButton.image.copy()
        temp_img.fill((255, 255, 255, self.alpha), special_flags=pygame.BLEND_RGBA_MULT)
        self.screen.blit(temp_img, self.currentlyPlayingButton.rect)

    def draw(self):
        self.screen.blit(self.background_img, (0, 0))
        self.playButton.draw(self.screen)
        self.quitButton.draw(self.screen)
        self.creditsButton.draw(self.screen)
        self.currentlyPlayingButton.draw(self.screen)

    def run(self):
        self.music_handler.play()

        while True:
            self.handleEvents()
            self.update()
            self.draw()
            pygame.display.flip()
