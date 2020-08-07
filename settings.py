import pygame
import sys
import os

versions = [
    {
        "model": "Enigma I",
        "rotors": [1, 2, 3, 4, 5],
        "reflector": ["b", "c"],
        "skin": ("i_lamp_board.png", (0, 0))
    }]


class Settings:
    """A class to store all settings which can be changed in simulator"""

    def __init__(self, enigma_sim):
        print("Loading settings...")
        self.screen = enigma_sim.screen
        self.version = versions[0]
        self.sound_on = True
        self.display_on = False
        self.sfxs = []
        self.fonts = []
        self.key_images = []
        self.lamp_images = []

        self._draw_screen()
        self._set_sfx()
        self._set_fonts()
        self._set_images()

    def _set_images(self):
        self.key_images.append(pygame.image.load(self._load_png("key.png")))
        self.key_images.append(pygame.image.load(self._load_png("key_pressed.png")))
        self.lamp_images.append(pygame.image.load(self._load_png("lamp.png")))

    def _set_fonts(self):
        self.font.append(pygame.font.Font(self._resource_path("Roboto-Regular.ttf"), 20))

    def _set_sfx(self):
        self.sfxs.append(self._load_wav("key-down.wav"))
        self.sfxs.append(self._load_wav("key-up.wav"))
        self.sfxs.append(self._load_wav("tick.wav"))

    def _load_wav(self, name):
        full_name = os.path.join("sounds", name)
        try:
            pygame_sound = pygame.mixer.Sound(self._resource_path(full_name))
            pygame_sound.set_volume(0.5)
        except pygame.error as e:
            print(e)

        return pygame_sound

    def _draw_screen(self):
        background = self._load_png("background.png")
        self.screen.blit(background, (0, 0))
        lamp_board = self._load_png(self.version["skin"][0])
        self.screen.blit(lamp_board, self.version["skin"][1])
        # paper_roll = self._load_png("paper_roll_off.png")
        # self.screen.blit(paper_roll, (440, 206))

    def _load_png(self, name):
        full_name = os.path.join("images", name)
        try:
            pygame_image = pygame.image.load(self._resource_path(full_name))
        except pygame.error as e:
            print(e)

        return pygame_image

    def _resource_path(self, relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)
