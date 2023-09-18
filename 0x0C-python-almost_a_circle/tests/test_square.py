#!/usr/bin/python3
"""Defines tests for the Square class"""
import os
import unittest
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for the Square class"""

    def setUp(self):
        """Sets up the test environment"""
        Base._Base__nb_objects = 0

    def test_square_inheritance(self):
        """Test square inheritance"""
        self.assertTrue(issubclass(Square, Base))

    def test_square_attributes(self):
        """Test square instance attributes"""
        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.id, 1)

        s2 = Square(3, 2, 3, 4)
        self.assertEqual(s2.size, 3)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.y, 3)
        self.assertEqual(s2.id, 4)

    def test_square_size_property(self):
        """Test size property of Square"""
        s = Square(5)
        self.assertEqual(s.size, 5)
        s.size = 10
        self.assertEqual(s.size, 10)
        with self.assertRaises(ValueError):
            s.size = -5
        with self.assertRaises(TypeError):
            s.size = "hello"

    def test_square_update_method(self):
        """Test update method of Square"""
        s = Square(5, 2, 3, 1)
        s.update(10)
        self.assertEqual(s.id, 10)
        s.update(20, 8)
        self.assertEqual(s.size, 8)
        s.update(30, 8, 5)
        self.assertEqual(s.x, 8)
        self.assertEqual(s.y, 5)
        s.update(40, 8, 5, 6)
        self.assertEqual(s.id, 40)

    def test_square_to_dictionary(self):
        """Test to_dictionary method of Square"""
        s = Square(5, 2, 3, 1)
        s_dict = s.to_dictionary()
        expected_dict = {'id': 1, 'size': 5, 'x': 2, 'y': 3}
        self.assertEqual(s_dict, expected_dict)

    def test_square_invalid_inputs(self):
        """Test invalid inputs for Square"""
        # Negative size
        with self.assertRaises(ValueError):
            s = Square(-5)
        # Non-integer size
        with self.assertRaises(TypeError):
            s = Square("hello")
        # Negative x coordinate
        with self.assertRaises(ValueError):
            s = Square(5, -2, 3)
        # Non-integer x coordinate
        with self.assertRaises(TypeError):
            s = Square(5, "hello", 3)
        # Negative y coordinate
        with self.assertRaises(ValueError):
            s = Square(5, 2, -3)
        # Non-integer y coordinate
        with self.assertRaises(TypeError):
            s = Square(5, 2, "hello")

    def test_square_str_representation(self):
        """Test str representation of Square"""
        s = Square(5, 2, 3, 1)
        self.assertEqual(str(s), '[Square] (1) 2/3 - 5')

    def test_square_save_to_file(self):
        """Test save_to_file method of Square"""
        s1 = Square(5)
        s2 = Square(3, 2, 3, 4)
        Square.save_to_file([s1, s2])
        filename = "Square.json"
        self.assertTrue(os.path.exists(filename))
        with open(filename, "r") as file:
            file_content = file.read()
            self.assertNotEqual(file_content, "")

    def test_square_load_from_file(self):
        """Test load_from_file method of Square"""
        s1 = Square(5)
        s2 = Square(3, 2, 3, 4)
        Square.save_to_file([s1, s2])
        loaded_squares = Square.load_from_file()
        self.assertEqual(len(loaded_squares), 2)
        self.assertIsInstance(loaded_squares[0], Square)
        self.assertEqual(loaded_squares[0].size, 5)
        self.assertEqual(loaded_squares[1].x, 2)
        self.assertEqual(loaded_squares[1].y, 3)
        self.assertEqual(loaded_squares[1].id, 4)

    def test_square_draw(self):
        """Test draw method of Square"""
        s1 = Square(5)
        s2 = Square(3, 2, 3, 4)
        squares = [s1, s2]
        Square.draw(squares, [])
        # Manual verification of the drawn shapes is required


if __name__ == '__main__':
    unittest.main()
