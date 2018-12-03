"""
Unit Testing for Visual Novel Scene
"""
import unittest
from code.world import Scene, Background, Character
from code.util import *

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
    pass
    
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

class TestWorld(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main()