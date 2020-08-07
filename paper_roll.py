import pygame
from pygame.sprite import Sprite


class PaperRoll(Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load(self._resource_path("images/paper_roll_on.png"))

    def _resource_path(self, relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)
