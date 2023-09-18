#!/usr/bin/python3
"""Defines tests for the Rectangle class"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class"""

    def setUp(self):
        """Sets up the test environment"""
        Base._Base__nb_objects = 0

    def test_rectangle_inheritance(self):
        """Test rectangle inheritance"""
        self.assertTrue(issubclass(Rectangle, Base))

    def test_rectangle_attributes(self):
        """Test rectangle instance attributes"""
        r1 = Rectangle(5, 4)
        self.assertEqual(r1.width, 5)
        self.assertEqual(r1.height, 4)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(3, 2, 1, 2, 3)
        self.assertEqual(r2.width, 3)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.x, 1)
        self.assertEqual(r2.y, 2)
        self.assertEqual(r2.id, 3)

    def test_rectangle_width_property(self):
        """Test width property of Rectangle"""
        r = Rectangle(5, 4)
        self.assertEqual(r.width, 5)
        r.width = 10
        self.assertEqual(r.width, 10)
        with self.assertRaises(ValueError):
            r.width = -5
        with self.assertRaises(TypeError):
            r.width = "hello"

    def test_rectangle_height_property(self):
        """Test height property of Rectangle"""
        r = Rectangle(5, 4)
        self.assertEqual(r.height, 4)
        r.height = 8
        self.assertEqual(r.height, 8)
        with self.assertRaises(ValueError):
            r.height = -5
        with self.assertRaises(TypeError):
            r.height = "hello"

    def test_rectangle_update_method(self):
        """Test update method of Rectangle"""
        r = Rectangle(5, 4, 2, 3, 1)
        r.update(10)
        self.assertEqual(r.id, 10)
        r.update(20, 8)
        self.assertEqual(r.width, 8)
        self.assertEqual(r.height, 4)
        r.update(30, 8, 5)
        self.assertEqual(r.x, 8)
        self.assertEqual(r.y, 5)
        r.update(40, 8, 5, 6)
        self.assertEqual(r.id, 40)

    def test_rectangle_to_dictionary(self):
        """Test to_dictionary method of Rectangle"""
        r = Rectangle(5, 4, 2, 3, 1)
        r_dict = r.to_dictionary()
        expected_dict = {'id': 1, 'width': 5, 'height': 4, 'x': 2, 'y': 3}
        self.assertEqual(r_dict, expected_dict)

    def test_rectangle_invalid_inputs(self):
        """Test invalid inputs for Rectangle"""
        # Negative width
        with self.assertRaises(ValueError):
            r = Rectangle(-5, 4)
        # Non-integer width
        with self.assertRaises(TypeError):
            r = Rectangle("hello", 4)
        # Negative height
        with self.assertRaises(ValueError):
            r = Rectangle(5, -4)
        # Non-integer height
        with self.assertRaises(TypeError):
            r = Rectangle(5, "hello")
        # Negative x coordinate
        with self.assertRaises(ValueError):
            r = Rectangle(5, 4, -2, 3)
        # Non-integer x coordinate
        with self.assertRaises(TypeError):
            r = Rectangle(5, 4, "hello", 3)
        # Negative y coordinate
        with self.assertRaises(ValueError):
            r = Rectangle(5, 4, 2, -3)
        # Non-integer y coordinate
        with self.assertRaises(TypeError):
            r = Rectangle(5, 4, 2, "hello")

    def test_rectangle_str_representation(self):
        """Test str representation of Rectangle"""
        r = Rectangle(5, 4, 2, 3, 1)
        self.assertEqual(str(r), '[Rectangle] (1) 2/3 - 5/4')

    def test_rectangle_save_to_file(self):
        """Test save_to_file method of Rectangle"""
        r1 = Rectangle(5, 4)
        r2 = Rectangle(3, 2, 1, 2, 3)
        Rectangle.save_to_file([r1, r2])
        filename = "Rectangle.json"
        self.assertTrue(os.path.exists(filename))
        with open(filename, "r") as file:
            file_content = file.read()
            self.assertNotEqual(file_content, "")

    def test_rectangle_load_from_file(self):
        """Test load_from_file method of Rectangle"""
        r1 = Rectangle(5, 4)
        r2 = Rectangle(3, 2, 1, 2, 3)
        Rectangle.save_to_file([r1, r2])
        loaded_rectangles = Rectangle.load_from_file()
        self.assertEqual(len(loaded_rectangles), 2)
        self.assertIsInstance(loaded_rectangles[0], Rectangle)
        self.assertEqual(loaded_rectangles[0].width, 5)
        self.assertEqual(loaded_rectangles[0].height, 4)
        self.assertEqual(loaded_rectangles[1].x, 1)
        self.assertEqual(loaded_rectangles[1].y, 2)
        self.assertEqual(loaded_rectangles[1].id, 3)

    def test_rectangle_draw(self):
        """Test draw method of Rectangle"""
        r1 = Rectangle(5, 4)
        r2 = Rectangle(3, 2, 1, 2, 3)
        rectangles = [r1, r2]
        Rectangle.draw(rectangles, [])
        # Manual verification of the drawn shapes is required


if __name__ == '__main__':
    unittest.main()
