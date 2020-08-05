import pygame
import sys
from settings import Settings
from key import Key


version = "v0.1"


class EnigmaSimulator:
    """Overall class to manage simulator and its features."""

    def __init__(self):
        # initialize pygame
        pygame.mixer.pre_init(44100, -16, 1, 512)
        pygame.init()

        # screen settings
        self.screen_width = 480
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Enigma Simulator {0}".format(version))
        self.background = pygame.image.load("images/background.png")
        self.screen.blit(self.background, (0, 0))

        # load sound effect files
        self.key_down_sfx = pygame.mixer.Sound('sounds/key-down.wav')
        self.key_up_sfx = pygame.mixer.Sound('sounds/key-up.wav')

        # load settings
        self.settings = Settings(self)

        self.keys = pygame.sprite.Group()
        self._create_keyboard()

    def run_sim(self):
        # start main loop for the simulator
        while True:
            self._check_event()
            pygame.display.flip()

    def _check_event(self):
        # watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_key_pressed(mouse_pos)
            elif event.type == pygame.MOUSEBUTTONUP:
                self._check_key_released()

    def _check_key_released(self):
        # response to key releasing
        for key in self.keys:
            if key.is_pressed:
                key.released()
                self.key_up_sfx.play()
                self.keys.draw(self.screen)

    def _check_key_pressed(self, mouse_pos):
        # response to key pressing
        for key in self.keys:
            if key.rect.collidepoint(mouse_pos):
                print("{0} clicked".format(key.letter))
                key.pressed()
                self.key_down_sfx.play()
                self.keys.draw(self.screen)

    def _create_keyboard(self):
        # create key sprites and put in sprite group
        key_top = "QWERTZUIO"
        key_mid = "ASDFGHJK"
        key_btm = "PYXCVBNML"

        key_top_x = 69
        key_top_y = 407
        for ltr in key_top:
            key = Key(self, ltr)
            key.rect.center = (key_top_x, key_top_y)
            self.keys.add(key)
            key_top_x += 44

        key_mid_x = 87
        key_mid_y = 455
        for ltr in key_mid:
            key = Key(self, ltr)
            key.rect.center = (key_mid_x, key_mid_y)
            self.keys.add(key)
            key_mid_x += 44

        key_btm_x = 59
        key_btm_y = 503
        for ltr in key_btm:
            key = Key(self, ltr)
            key.rect.center = (key_btm_x, key_btm_y)
            self.keys.add(key)
            key_btm_x += 44

        # draw key sprite group on key board
        self.keys.draw(self.screen)


if __name__ == '__main__':
    # Make a simulator instance and run it
    es = EnigmaSimulator()
    es.run_sim()
