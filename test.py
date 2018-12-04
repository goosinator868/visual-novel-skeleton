"""
Unit Testing for Visual Novel Scene
"""
import unittest
from code.world import *
import PIL
from PIL import Image
from enum import Enum

class TestUtil(unittest.TestCase):
    def test_util_check_validity_of_name(self):
        # Check Type
        with self.assertRaises(TypeError):
            check_validity_of_name(None)
        check_validity_of_name("Emily")

        # Search for duplicates
        #with self.assertRaises(ValueError):
        #    check_validity_of_name("Emily")
    
    def test_util_check_validity_of_image_path(self):
        background = Background()
        with self.assertRaises(TypeError):
            check_validity_of_image_path(0, background)
        with self.assertRaises(ValueError):
            check_validity_of_image_path("does_not_exist", background)
        with self.assertRaises(FileNotFoundError):
            check_validity_of_image_path("does_not_exist.png", background)
        check_validity_of_image_path("example.jpg", background)
        check_validity_of_image_path("example.png", background)

        # TODO add other type validity checking
    
    def test_util_check_validity_of_image(self):
        background = Background()
        with self.assertRaises(TypeError):
            check_validity_of_image(0, background)
        with self.assertRaises(TypeError):
            check_validity_of_image("example.png", background)
        image_png = Image.open("images/backgrounds/example.png")
        image_jpg = Image.open("images/backgrounds/example.jpg")
        check_validity_of_image(image_png, background)
        check_validity_of_image(image_jpg, background)
    
    def test_util_check_validity_of_background(self):
        background = Background()
        with self.assertRaises(TypeError):
            check_validity_of_background(background)
        background.name = "Background1"
        with self.assertRaises(TypeError):
            check_validity_of_background(background)
        background.name = None
        image_png = Image.open("images/backgrounds/example.png")
        background.image = image_png
        with self.assertRaises(TypeError):
            check_validity_of_background(background)
        background.name = "Background1"
        check_validity_of_background(background)
    
    def test_check_validity_of_relationships(self):
        character = Character()
        character.platonic_relationship = -3
        with self.assertRaises(ValueError):
            check_validity_of_relationships(character)
        character.platonic_relationship = 0
        character.romantic_relationship = -3
        with self.assertRaises(ValueError):
            check_validity_of_relationships(character)
        character.romantic_relationship = 0
        character.sexual_relationship = -3
        with self.assertRaises(ValueError):
            check_validity_of_relationships(character)

        character.sexual_relationship = 0
        character.platonic_relationship = 6
        with self.assertRaises(ValueError):
            check_validity_of_relationships(character)
        character.platonic_relationship = 0
        character.romantic_relationship = 6
        with self.assertRaises(ValueError):
            check_validity_of_relationships(character)
        character.romantic_relationship = 0
        character.sexual_relationship = 6
        with self.assertRaises(ValueError):
            check_validity_of_relationships(character)
        character.sexual_relationship = 0

        check_validity_of_relationships(character)

        with self.assertRaises(TypeError):
            check_validity_of_relationships(0)

class TestTextElement(unittest.TestCase):
    pass

class TestCharacter(unittest.TestCase):
    def test_character_default(self):
        character = Character()
        self.assertIsNone(character.name)
        self.assertIsNone(character.state)
        self.assertEquals(character.platonic_relationship, 0)
        self.assertEquals(character.romantic_relationship, 0)
        self.assertEquals(character.sexual_relationship, 0)
        self.assertEquals(character.images, {})

    def test_character_name(self):
        character = Character()
        self.assertIsNone(character.name)
        with self.assertRaises(TypeError):
            character.set_name(0)
        character.set_name("John Doe")
        self.assertEquals(character.name, "John Doe")
        character.name = Scene()
        with self.assertRaises(TypeError):
            check_validity_of_name(character.name)
    
    def test_character_platonic_relationship(self):
        character = Character()
        self.assertEquals(character.platonic_relationship, 0)
        character.increase_relationship(PLATONIC, 3)
        self.assertEquals(character.platonic_relationship, 3)
        character.increase_relationship(PLATONIC, 5)
        self.assertEquals(character.platonic_relationship, 5)
        with self.assertRaises(ValueError):
            character.increase_relationship(PLATONIC, -2)
        self.assertEquals(character.platonic_relationship, 5)
        character.decrease_relationship(PLATONIC, 4)
        self.assertEquals(character.platonic_relationship, 1)
        character.decrease_relationship(PLATONIC, 2)
        self.assertEquals(character.platonic_relationship, -1)
        with self.assertRaises(ValueError):
            character.decrease_relationship(PLATONIC, -3)
        self.assertEquals(character.platonic_relationship, -1)
        character.decrease_relationship(PLATONIC, 3)
        self.assertEquals(character.platonic_relationship, -2)
        with self.assertRaises(TypeError):
            character.increase_relationship(PLATONIC, 2.0)
        self.assertEquals(character.platonic_relationship, -2)
        character.increase_relationship(PLATONIC, 2)
        with self.assertRaises(TypeError):
            character.decrease_relationship(PLATONIC, 2.0)
        self.assertEquals(character.platonic_relationship, 0)
        character.platonic_relationship = -3
        with self.assertRaises(ValueError):
            check_validity_of_relationships(character)
        character.platonic_relationship = 6
        with self.assertRaises(ValueError):
            check_validity_of_relationships(character)
        character.platonic_relationship = "eggs"
        with self.assertRaises(TypeError):
            check_validity_of_relationships(character)
    
    def test_character_romantic_relationship(self):
        character = Character()
        self.assertEquals(character.romantic_relationship, 0)
        character.increase_relationship(ROMANTIC, 3)
        self.assertEquals(character.romantic_relationship, 3)
        character.increase_relationship(ROMANTIC, 5)
        self.assertEquals(character.romantic_relationship, 5)
        with self.assertRaises(ValueError):
            character.increase_relationship(ROMANTIC, -2)
        self.assertEquals(character.romantic_relationship, 5)
        character.decrease_relationship(ROMANTIC, 4)
        self.assertEquals(character.romantic_relationship, 1)
        character.decrease_relationship(ROMANTIC, 2)
        self.assertEquals(character.romantic_relationship, -1)
        with self.assertRaises(ValueError):
            character.decrease_relationship(ROMANTIC, -3)
        self.assertEquals(character.romantic_relationship, -1)
        character.decrease_relationship(ROMANTIC, 3)
        self.assertEquals(character.romantic_relationship, -2)
        with self.assertRaises(TypeError):
            character.increase_relationship(ROMANTIC, 2.0)
        self.assertEquals(character.romantic_relationship, -2)
        character.increase_relationship(ROMANTIC, 2)
        with self.assertRaises(TypeError):
            character.decrease_relationship(ROMANTIC, 2.0)
        self.assertEquals(character.romantic_relationship, 0)
        character.romantic_relationship = -3
        with self.assertRaises(ValueError):
            check_validity_of_relationships(character)
        character.romantic_relationship = 6
        with self.assertRaises(ValueError):
            check_validity_of_relationships(character)
        character.romantic_relationship = "eggs"
        with self.assertRaises(TypeError):
            check_validity_of_relationships(character)

    def test_character_sexual_relationship(self):
        character = Character()
        self.assertEquals(character.sexual_relationship, 0)
        character.increase_relationship(SEXUAL, 3)
        self.assertEquals(character.sexual_relationship, 3)
        character.increase_relationship(SEXUAL, 5)
        self.assertEquals(character.sexual_relationship, 5)
        with self.assertRaises(ValueError):
            character.increase_relationship(SEXUAL, -2)
        self.assertEquals(character.sexual_relationship, 5)
        character.decrease_relationship(SEXUAL, 4)
        self.assertEquals(character.sexual_relationship, 1)
        character.decrease_relationship(SEXUAL, 2)
        self.assertEquals(character.sexual_relationship, -1)
        with self.assertRaises(ValueError):
            character.decrease_relationship(SEXUAL, -3)
        self.assertEquals(character.sexual_relationship, -1)
        character.decrease_relationship(SEXUAL, 3)
        self.assertEquals(character.sexual_relationship, -2)
        with self.assertRaises(TypeError):
            character.increase_relationship(SEXUAL, 2.0)
        self.assertEquals(character.sexual_relationship, -2)
        character.increase_relationship(SEXUAL, 2)
        with self.assertRaises(TypeError):
            character.decrease_relationship(SEXUAL, 2.0)
        self.assertEquals(character.sexual_relationship, 0)
        character.sexual_relationship = -3
        with self.assertRaises(ValueError):
            check_validity_of_relationships(character)
        character.sexual_relationship = 6
        with self.assertRaises(ValueError):
            check_validity_of_relationships(character)
        character.sexual_relationship = "eggs"
        with self.assertRaises(TypeError):
            check_validity_of_relationships(character)
    
    def test_character_images(self):
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