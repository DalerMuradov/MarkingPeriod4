import pygame
from Boulder import Boulder
from Button import CurrentlyPlayingButton
from Quotes import Quotes
import random

class GameScreen:
    def __init__(self, screen, music_handler):
        self.screen = screen
        self.music_handler = music_handler
        self.clock = pygame.time.Clock()
        self.background_image = pygame.image.load("Background.png")  # Load background image
        self.hill_image = pygame.image.load("Hill.png")
        self.boulder = Boulder(self.screen)
        self.currently_playing_button = CurrentlyPlayingButton("CurrentlyPlaying3.png", (140, 50), (260, 50))
        self.quotes = Quotes()

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.boulder.startMoving()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    self.boulder.stopMoving()
        return True

    def run(self):
        self.music_handler.play()
        running = True
        while running:
            running = self.handleEvents()

            if self.boulder.update():
                quote = self.quotes.get_random_quote()
                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                print(f"\033[38;2;{color[0]};{color[1]};{color[2]}m{quote}\033[0m")

            self.boulder.cycleImages()

            self.screen.fill((0, 0, 0))
            # Blit background image under the hill
            self.screen.blit(self.background_image, (0, 0))
            self.screen.blit(self.hill_image, (0, 0))  # Blit hill image on top of background
            self.boulder.draw()
            self.currently_playing_button.update()
            self.currently_playing_button.draw(self.screen)
            pygame.display.flip()

            self.clock.tick(60)

        pygame.quit()
