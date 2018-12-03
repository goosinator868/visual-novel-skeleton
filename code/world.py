"""
world.py
"""
from code.util import *

class Character():
    pass

class Background():
    pass

class TextElement():
    pass

class Scene():

    def __init__(self):
        self.name = None
        self.background = None
        self.character_a = None
        self.character_b = None
        self.text_element = None
    def set_name(self, new_name):
        check_validity_of_name(new_name)
        self.name = new_name
    def set_background(self, new_background):
        pass

class World():
    pass
        