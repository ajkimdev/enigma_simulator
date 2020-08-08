import pygame
import sys
import os

versions = [
    {
        "model": "Enigma I",
        "rotors": [1, 2, 3, 4, 5],
        "reflectors": ["b", "c"],
        "skin": ("i_lamp_board.png", (0, 0))
    },
    {
        "model": "Enigma M3",
        "rotors": [1, 2, 3, 4, 5, 6, 7],
        "reflectors": ["b", "c"],
        "skin": ("m3_lamp_board.png", (0, 0))
    }]


class Settings:
    """A class to store all settings which can be changed in simulator"""

    def __init__(self):
        print("Loading settings...")
        self.version = versions[0]
        self.sound_on = True
        self.display_on = False
        self.sfxs = []
