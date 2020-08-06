import pygame
import sys
import os
from pygame.sprite import Sprite


class Lamp(Sprite):
    """A class to manage lamp object and its functions"""

    def __init__(self, letter):
        super().__init__()
        self.letter = letter

        # load images for lamp
        self.image = pygame.image.load(self._resource_path("images/lamp.png"))
        self.rect = self.image.get_rect()

        # lettering on lamp image
        self.font = pygame.font.Font(self._resource_path("Roboto-Regular.ttf"), 20)
        self.font.set_bold(True)
        self.ltr_img = self.font.render(letter, True, (80, 80, 80))
        self.ltr_img_rect = self.ltr_img.get_rect()
        self.ltr_img_rect.center = (16, 15)
        self.image.blit(self.ltr_img, self.ltr_img_rect)

        # to restore lamp off image
        self.off_image = self.image.copy()

        # store lamp state whether on or off
        self.is_on = False

    def _resource_path(self, relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

    def on(self):
        self.is_on = True
        ltr_on = self.font.render(self.letter, True, (249, 235, 176))
        ltr_on_rect = ltr_on.get_rect()
        ltr_on_rect.center = (16, 15)
        self.image.blit(ltr_on, ltr_on_rect)

    def off(self):
        self.is_on = False
        self.image.blit(self.off_image, (0, 0))
