"""
world.py
"""
import PIL
from PIL import Image

"""
Macros
"""
BACKGROUND_PATH = "images/backgrounds/"

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
        check_validity_of_image_path(image_path, self)
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
        check_validity_of_background(new_background)
        self.background = new_background

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



"""
Utils
"""

"""
checks that a name is a string
TODO check for no duplicate names
"""
def check_validity_of_name(name):
    if not isinstance(name, str):
            raise TypeError("Name is not a string.")
    # TODO check for no duplicates

"""
checks that an image path is valid
TODO Account for other types
"""
def check_validity_of_image_path(image_path, caller):
    if isinstance(caller, Background):
        if not isinstance(image_path, str):
            raise TypeError("Image path is not a string.")
        image_type = image_path.split(".")
        if len(image_type) != 2:
            raise ValueError("Image not set. Make sure the image is of the format png or jpg.")

        if image_type[1] == "png" or image_type[1] == "jpg":
            image = Image.open(BACKGROUND_PATH + image_path)
        else:
            raise ValueError("Image not set. Make sure the image is of the format png or jpg.")
    else:
        raise TypeError("This type doesn't have a valid image to check.")

"""
checks that an image is valid
TODO Account for other types
"""
def check_validity_of_image(image, caller):
    if isinstance(caller, Background):
        if not isinstance(image, PIL.PngImagePlugin.PngImageFile) and not isinstance(image, PIL.JpegImagePlugin.JpegImageFile):
            raise TypeError("Image is not an image.")
    else:
        raise TypeError("This type doesn't have a valid image to check.")

"""
checks that a background is valid
"""
def check_validity_of_background(background):
    if not isinstance(background, Background):
        raise TypeError("Type other than Background passed.")
    check_validity_of_name(background.name)
    check_validity_of_image(background.image, background)