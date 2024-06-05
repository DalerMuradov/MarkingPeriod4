import pygame
from CreditScreen import CreditScreen
from GameScreen import GameScreen
from IntroScreen import IntroScreen
from Music import MusicHandler

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((719, 719))
        pygame.display.set_caption("Sisyphus")
        icon = pygame.image.load("icon.png")
        pygame.display.set_icon(icon)

        self.music_handler_intro = MusicHandler('Intro.mp3', 'Credit.mp3')
        self.music_handler_credit = MusicHandler('Credit.mp3', 'Intro.mp3')
        self.music_handler_game = MusicHandler('Game.mp3', 'Game.mp3')

        self.intro_screen = IntroScreen(self.screen, self.music_handler_intro, self)

    def startPlayScreen(self):
        if self.music_handler_intro:
            self.music_handler_intro.stop()
        if self.music_handler_credit:
            self.music_handler_credit.stop()
        self.music_handler_game.play()
        self.game_screen = GameScreen(self.screen, self.music_handler_game)
        self.game_screen.run()

    def run(self):
        self.intro_screen.run()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break
            if self.intro_screen.show_credit_screen:
                if self.music_handler_intro:
                    self.music_handler_intro.stop()
                if self.music_handler_credit:
                    self.music_handler_credit.stop()
                self.credit_screen = CreditScreen(self.screen, self.music_handler_credit,
                                                  self.intro_screen.currentlyPlayingButton)
                self.credit_screen.run()
                self.intro_screen.show_credit_screen = False

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()