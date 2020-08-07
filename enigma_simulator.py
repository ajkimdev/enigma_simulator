import pygame
import sys
import os
from settings import Settings
from key import Key
from lamp import Lamp


version = "v0.2"


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

        # load settings
        self.settings = Settings(self)

        # load background images
        self.screen.blit(self.settings.screen, (0, 0))

        # load sound effect from settings
        self.key_down_sfx = self.settings.sfxs[0]
        self.key_up_sfx = self.settings.sfxs[1]

        self.keys = pygame.sprite.Group()
        self.lamps = pygame.sprite.Group()

        self._create_keyboard()
        self._create_lampboard()
        self._create_paper_roll()

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
                self._check_mousebtndown_event(mouse_pos)
            elif event.type == pygame.MOUSEBUTTONUP:
                self._check_keyreleased_event()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)
            elif event.type == pygame.KEYUP:
                self._check_keyreleased_event()

    def _check_keydown_event(self, event):
        if len(event.unicode) > 0:
            key_ascii = ord(event.unicode)
            if (key_ascii > 64 and key_ascii < 91) or (key_ascii > 96 and key_ascii < 123):
                upper_key = chr(key_ascii).upper()
                print("{0} hitted".format(upper_key))
                for key in self.keys:
                    if key.letter == upper_key:
                        self._check_key_pressed(key)
                        break

    def _check_mousebtndown_event(self, mouse_pos):
        for key in self.keys:
            if key.rect.collidepoint(mouse_pos):
                print("{0} clicked".format(key.letter))
                self._check_key_pressed(key)
                break

    def _check_key_pressed(self, key):
        # response to key pressing
        key.pressed()
        self.key_down_sfx.play()
        self.keys.draw(self.screen)

        # response to lamp on
        for lamp in self.lamps:
            if lamp.letter == key.letter:
                lamp.on()
                self.lamps.draw(self.screen)

    def _check_keyreleased_event(self):
        # response to key releasing
        for key in self.keys:
            if key.is_pressed:
                key.released()
                self.key_up_sfx.play()
                self.keys.draw(self.screen)

        # response to lamp off
        for lamp in self.lamps:
            if lamp.is_on:
                lamp.off()
                self.lamps.draw(self.screen)

    def _create_paper_roll(self):
        pass

    def _create_lampboard(self):
        # create lamp sprites and put in lamps sprite group
        lamp_top = "QWERTZUIO"
        lamp_mid = "ASDFGHJK"
        lamp_btm = "PYXCVBNML"

        lamp_top_x = 69
        lamp_top_y = 253
        for ltr in lamp_top:
            lamp = Lamp(ltr)
            lamp.rect.center = (lamp_top_x, lamp_top_y)
            self.lamps.add(lamp)
            lamp_top_x += 44

        lamp_mid_x = 87
        lamp_mid_y = 301
        for ltr in lamp_mid:
            lamp = Lamp(ltr)
            lamp.rect.center = (lamp_mid_x, lamp_mid_y)
            self.lamps.add(lamp)
            lamp_mid_x += 44

        lamp_btm_x = 59
        lamp_btm_y = 349
        for ltr in lamp_btm:
            lamp = Lamp(ltr)
            lamp.rect.center = (lamp_btm_x, lamp_btm_y)
            self.lamps.add(lamp)
            lamp_btm_x += 44

        self.lamps.draw(self.screen)

    def _create_keyboard(self):
        # create key sprites and put in keys sprite group
        key_top = "QWERTZUIO"
        key_mid = "ASDFGHJK"
        key_btm = "PYXCVBNML"

        key_top_x = 69
        key_top_y = 407
        for ltr in key_top:
            key = Key(ltr)
            key.rect.center = (key_top_x, key_top_y)
            self.keys.add(key)
            key_top_x += 44

        key_mid_x = 87
        key_mid_y = 455
        for ltr in key_mid:
            key = Key(ltr)
            key.rect.center = (key_mid_x, key_mid_y)
            self.keys.add(key)
            key_mid_x += 44

        key_btm_x = 59
        key_btm_y = 503
        for ltr in key_btm:
            key = Key(ltr)
            key.rect.center = (key_btm_x, key_btm_y)
            self.keys.add(key)
            key_btm_x += 44

        # draw key sprite group on key board
        self.keys.draw(self.screen)


if __name__ == '__main__':
    # Make a simulator instance and run it
    es = EnigmaSimulator()
    es.run_sim()
