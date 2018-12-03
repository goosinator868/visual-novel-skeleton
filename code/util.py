"""
util.py
Description: Contains utilities
"""
from PIL import Image

"""
Macros
"""
BACKGROUND_PATH = "images/backgrounds/"

"""
checks that a name is a string
TODO check for no duplicate names
"""
def check_validity_of_name(name):
    if not isinstance(name, str):
            raise TypeError("Name is not a string.")

def check_validity_of_image(image_path, object_path):
    if not isinstance(image_path, str):
        raise TypeError("Image path is not a string.")
    image_type = image_path.split(".")
    if len(image_type) != 2:
        raise TypeError("Image not set. Make sure the input end with a .png or .jpg.")

    if image_type[1] == "png" or image_type[1] == "jpg":
        image = Image.open(object_path + image_path)
    else:
        raise TypeError("Invalid type. Make sure the image is of the format png or jpg.")
