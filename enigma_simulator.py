import pygame
import sys
from settings import Settings

version = "v0.1"


class EnigmaSimulator:
    """Overall class to manage simulator and its features."""

    def __init__(self):
        # Initialize pygame
        pygame.init()

        # Screen settings
        self.screen_width = 480
        self.screen_height = 600
        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height))
        pygame.display.set_caption("Enigma Simulator {0}".format(version))

        self.background = pygame.image.load("images/background.png")

        # Load settings
        self.settings = Settings()

    def run_sim(self):
        # Start main loop for the simulator
        while True:
            self._check_event()

            pygame.display.flip()

            self.screen.blit(self.background, (0, 0))

    def _check_event(self):
        # watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


if __name__ == '__main__':
    # Make a simulator instance and run it
    es = EnigmaSimulator()
    es.run_sim()
