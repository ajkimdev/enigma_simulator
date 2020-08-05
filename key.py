import pygame
import sys
import os
from pygame.sprite import Sprite


class Key(Sprite):
    """A class to manage key object and its functions"""

    def __init__(self, enigma_sim, letter):
        super().__init__()
        self.screen = enigma_sim.screen
        self.letter = letter

        # load images for key
        self.image = pygame.image.load(self._resource_path("images/key.png"))
        self.pressed_img = pygame.image.load(self._resource_path("images/key_pressed.png"))
        self.rect = self.image.get_rect()

        # lettering on key
        self.font = pygame.font.Font(self._resource_path("Roboto-Regular.ttf"), 20)
        self.ltr_img = self.font.render(letter, True, (220, 220, 220))
        self.ltr_img_rect = self.ltr_img.get_rect()
        self.ltr_img_rect.center = (15, 15)
        self.image.blit(self.ltr_img, self.ltr_img_rect)

        # to restore released image
        self.released_img = self.image.copy()

        # store key state whether pressed or released
        self.is_pressed = False

    def _resource_path(self, relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

    def pressed(self):
        self.is_pressed = True
        self.image.blit(self.pressed_img, (0, 0))

    def released(self):
        self.is_pressed = False
        self.image.blit(self.released_img, (0, 0))
