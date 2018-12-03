"""
Unit Testing for Visual Novel Scene
"""
import unittest
from code.world import *
import PIL
from PIL import Image

class TestUtil(unittest.TestCase):
    def test_util_check_validity_of_name(self):
        # Check Type
        with self.assertRaises(TypeError):
            check_validity_of_name(None)
        check_validity_of_name("Emily")

        # Search for duplicates
        #with self.assertRaises(ValueError):
        #    check_validity_of_name("Emily")

class TestTextElement(unittest.TestCase):
    pass

class TestCharacter(unittest.TestCase):
    pass

class TestBackground(unittest.TestCase):
    def test_background_default(self):
        background = Background()
        self.assertIsNone(background.name)
        self.assertIsNone(background.image)

    def test_background_name(self):
        background = Background()
        self.assertIsNone(background.name)
        with self.assertRaises(TypeError):
            background.set_name(Scene())
        background.set_name("School Yard")
        self.assertEquals(background.name, "School Yard")
        background.name = 70.5
        with self.assertRaises(TypeError):
            check_validity_of_name(background.name)

    def test_background_image(self):
        # Check default
        # Set to a png or jpg
        background = Background()
        image_png = Image.open("images/backgrounds/example.png")
        image_jpg = Image.open("images/backgrounds/example.jpg")
        self.assertIsNone(background.image)
        with self.assertRaises(TypeError):
            background.set_image(5)
        with self.assertRaises(ValueError):
            background.set_image("Hello.pn")
        with self.assertRaises(FileNotFoundError):
            background.set_image("does_not_exist.jpg")
        background.set_image("example.png")
        self.assertIsInstance(background.image, PIL.PngImagePlugin.PngImageFile)
        background.set_image("example.jpg")
        self.assertIsInstance(background.image, PIL.JpegImagePlugin.JpegImageFile)
        background.image = "Definitely not a file"
        with self.assertRaises(TypeError):
            check_validity_of_image(background.image, background)
    
class TestScene(unittest.TestCase):

    def test_scene_default(self):
        # Test Scene Element Existence
        # Should have no name
        # Should have no background
        # Should have no characters
        # Should have no text element
        scene = Scene()
        self.assertIsNone(scene.name)
        self.assertIsNone(scene.background)
        self.assertIsNone(scene.character_a)
        self.assertIsNone(scene.character_b)
        self.assertIsNone(scene.text_element)
    
    def test_scene_name(self):
        scene = Scene()
        self.assertIsNone(scene.name)
        with self.assertRaises(TypeError):
            scene.set_name(5)
        scene.set_name("Scene1")
        self.assertEquals(scene.name, "Scene1")
        scene.name = 1
        self.assertEquals(scene.name, 1)
        with self.assertRaises(TypeError):
            check_validity_of_name(scene.name)

    def test_scene_background(self):
        scene = Scene()
        self.assertIsNone(scene.background)

        value = 90
        with self.assertRaises(TypeError):
            scene.set_background(value)

        empty_background = Background()
        self.assertIsNone(scene.background)

        name_only_background = Background()
        name_only_background.set_name("Background1")
        with self.assertRaises(TypeError):
            scene.set_background(name_only_background)

        image_only_background = Background()
        image_only_background.set_image("example.jpg")
        with self.assertRaises(TypeError):
            scene.set_background(image_only_background)

        name_bad_background = Background()
        name_bad_background.name = 1
        name_bad_background.set_image("example.jpg")
        with self.assertRaises(TypeError):
            scene.set_background(name_bad_background)

        image_bad_background = Background()
        image_bad_background.set_name("Background1")
        image_bad_background.image = "not_valid"
        with self.assertRaises(TypeError):
            scene.set_background(image_bad_background)

        completed_background = Background()
        completed_background.set_name("Background1")
        completed_background.set_image("example.jpg")
        print (type(completed_background.image))
        scene.set_background(completed_background)
        self.assertEquals(scene.background, completed_background)

        scene.background = value
        with self.assertRaises(TypeError):
            check_validity_of_background(scene.background)

        scene.background = name_bad_background
        with self.assertRaises(TypeError):
            check_validity_of_background(scene.background)
        
        scene.background = image_bad_background
        with self.assertRaises(TypeError):
            check_validity_of_background(scene.background)
        
    
    def test_scene_character_a(self):
        pass
    
    def test_scene_character_b(self):
        pass
    
    def test_scene_text_element(self):
        pass

class TestWorld(unittest.TestCase):
    pass

class TestUI(unittest.TestCase):
    pass

class TestGame(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main()