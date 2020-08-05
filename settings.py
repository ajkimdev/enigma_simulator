import pygame

versions = [{
    "model": "Enigma I",
    "rotors": [1, 2, 3, 4, 5],
    "reflector": ["b", "c"],
    "skins": [{
        "file_name": "enigma_i_lamp_panel.png",
        "image_pos": (10, 10)
    }, {
        "file_name": "enigma_i_plug_board.png",
        "image_pos": (10, 500)
    }]
}]


class Settings:
    """A class to store all settings which can be changed in simulator"""

    def __init__(self, enigma_sim):
        print("Loading settings...")
        self.screen = enigma_sim.screen
        self.version = versions[0]
        self.sound_on = True
        self.display_on = False

    def _load_png(self, version):
        for file_name, image_loc in version["skins"]:
            pass
