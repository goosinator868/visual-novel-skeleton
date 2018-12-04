"""
world.py
"""
import PIL
from PIL import Image
from enum import Enum

"""
Macros
"""
BACKGROUND_PATH = "images/backgrounds/"
PLATONIC = "platonic"
ROMANTIC = "romantic"
SEXUAL = "sexual"
"""
Character()
Description:
    Creates a character that the player can interact with.
    Relationships can be platonic or romantic and depending on the character can be romanced.
    State determines which image will be displayed.
"""
class Character():

    def __init__(self):
        self.name = None
        self.state = None
        self.platonic_relationship = 0
        self.romantic_relationship = 0
        self.sexual_relationship = 0
        self.images = {}

    def set_name(self, new_name):
        check_validity_of_name(new_name)
        self.name = new_name
    
    def increase_relationship(self, relation, value):
        if type(value) != int:
            raise TypeError("Wrong type entered.")
        if value < 0:
            raise ValueError("Negative value entered.")
        if value > 7:
            raise ValueError("Too large a value entered.")
        if type(relation) != type(PLATONIC) or type(relation) != type(ROMANTIC) or type(relation) != type(SEXUAL):
            raise TypeError("Wrong type entered.")

        if relation == PLATONIC:
            self.platonic_relationship = self.platonic_relationship + value
            if self.platonic_relationship > 5:
                self.platonic_relationship = 5
            if self.platonic_relationship < -2:
                self.platonic_relationship = 5
        if relation == ROMANTIC:
            self.romantic_relationship = self.romantic_relationship + value
            if self.romantic_relationship > 5:
                self.romantic_relationship = 5
            if self.romantic_relationship < -2:
                self.romantic_relationship = 5
        if relation == SEXUAL:
            self.sexual_relationship = self.sexual_relationship + value
            if self.sexual_relationship > 5:
                self.sexual_relationship = 5
            if self.sexual_relationship < -2:
                self.sexual_relationship = 5

    def decrease_relationship(self, relation, value):
        if type(value) != int:
            raise TypeError("Wrong type entered.")
        if value < 0:
            raise ValueError("Negative value entered.")
        if value > 7:
            raise ValueError("Too large a value entered.")
        if type(relation) != type(PLATONIC) or type(relation) != type(ROMANTIC) or type(relation) != type(SEXUAL):
            raise TypeError("Wrong type entered.")
        if relation != PLATONIC and relation != ROMANTIC and relation != SEXUAL:
            raise TypeError("Wrong type entered.")

        if relation == PLATONIC:
            self.platonic_relationship = self.platonic_relationship - value
            if self.platonic_relationship > 5:
                self.platonic_relationship = -2
            if self.platonic_relationship < -2:
                self.platonic_relationship = -2
        if relation == ROMANTIC:
            self.romantic_relationship = self.romantic_relationship - value
            if self.romantic_relationship > 5:
                self.romantic_relationship = -2
            if self.romantic_relationship < -2:
                self.romantic_relationship = -2
        if relation == SEXUAL:
            self.sexual_relationship = self.sexual_relationship - value
            if self.sexual_relationship > 5:
                self.sexual_relationship = -2
            if self.sexual_relationship < -2:
                self.sexual_relationship = -2

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
***********Utils***********
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
checks that a character's relationships are valid
"""
def check_validity_of_relationships(caller):
    if type(caller) == Character:
        platonic = caller.platonic_relationship
        romantic = caller.romantic_relationship
        sexual = caller.sexual_relationship

        if type(platonic) == int:
            if platonic > 5 or platonic < -2:
                raise ValueError("A relationship value is outside of the range -2 : 5.")
        else:
            raise TypeError("A relationship isn't an integer.")
        
        if type(romantic) == int:
            if romantic > 5 or romantic < -2:
                raise ValueError("A relationship value is outside of the range -2 : 5.")
        else:
            raise TypeError("A relationship isn't an integer.")
        
        if type(sexual) == int:
            if sexual > 5 or sexual < -2:
                raise ValueError("A relationship value is outside of the range -2 : 5.")
        else:
            raise TypeError("A relationship isn't an integer.")
    else:
        raise TypeError("This type doesn't have valid relationships to check.")

"""
checks that a background is valid
"""
def check_validity_of_background(background):
    if not isinstance(background, Background):
        raise TypeError("Type other than Background passed.")
    check_validity_of_name(background.name)
    check_validity_of_image(background.image, background)