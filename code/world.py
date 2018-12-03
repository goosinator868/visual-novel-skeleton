"""
world.py
"""
from code.util import *
from PIL import Image

class Character():
    pass

class Background():
    
    def __init__(self):
        self.name = None
        self.image = None
    
    def set_name(self, new_name):
        check_validity_of_name(new_name)
        self.name = new_name
    
    def set_image(self, image_path):
        check_validity_of_image(image_path, BACKGROUND_PATH)
        self.image = Image.open(BACKGROUND_PATH + image_path)


class TextElement():
    pass

"""
Scene()
Description:
    Creates a scene that is displayed for the user to see.
    Scenes contain a background, a text element, and up to two characters.
"""
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

"""
World()
Description:
    Creates a world that holds game data. Worlds are used for saves.
"""
class World():
    pass

"""
UI()
Description:
    The UI for the game.
"""
class UI():
    pass

"""
Game()
Description:
    Runs the game. Runs UI and world.
"""
class Game():
    pass
        