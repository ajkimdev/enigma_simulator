import pygame
import sys
import os
from pygame.sprite import Sprite


class PaperRoll(Sprite):
    def __init__(self):
        super().__init__()
        self.paper_roll_off_img = pygame.image.load(self._resource_path("images/paper_roll_off.png"))
        self.paper_roll_on_img = pygame.image.load(self._resource_path("images/paper_roll_on.png"))
        self.image = self.paper_roll_off_img
        self.rect = self.image.get_rect()

        self.is_on = False

    def clicked(self):
        if not self.is_on:
            print("on")
            self.image = self.paper_roll_on_img
            off_rect = self.paper_roll_on_img.get_rect()
            self.rect.x -= 440
            self.rect.width = off_rect[2]
            self.rect.height = off_rect[3]
            print(self.rect)
            self.is_on = True

        else:
            print("off")
            self.image = self.paper_roll_off_img
            on_rect = self.paper_roll_off_img.get_rect()
            self.rect.x += 440
            self.rect.width = on_rect[2]
            self.rect.height = on_rect[3]
            self.is_on = False

    def _resource_path(self, relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)
