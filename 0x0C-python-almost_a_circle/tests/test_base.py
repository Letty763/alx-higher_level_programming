#!/usr/bin/python3
"""Defines tests for the Base class"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for the Base class"""

    def test_base_id_auto_increment(self):
        """Test automatic increment of id attribute"""
        Base._Base__nb_objects = 0

        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base()
        self.assertEqual(b3.id, 3)

    def test_base_id_manual_assignment(self):
        """Test manual assignment of id attribute"""
        Base._Base__nb_objects = 0

        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base(10)
        self.assertEqual(b2.id, 10)

        b3 = Base(-5)
        self.assertEqual(b3.id, -5)

    def test_base_id_string_assignment(self):
        """Test id assignment with a string"""
        Base._Base__nb_objects = 0

        b = Base("hello")
        self.assertEqual(b.id, "hello")

    def test_base_id_float_assignment(self):
        """Test id assignment with a float"""
        Base._Base__nb_objects = 0

        b = Base(3.14)
        self.assertEqual(b.id, 3.14)

    def test_base_id_list_assignment(self):
        """Test id assignment with a list"""
        Base._Base__nb_objects = 0

        b = Base([1, 2, 3])
        self.assertEqual(b.id, [1, 2, 3])

    def test_base_id_dict_assignment(self):
        """Test id assignment with a dictionary"""
        Base._Base__nb_objects = 0

        b = Base({"key": "value"})
        self.assertEqual(b.id, {"key": "value"})

    def test_base_to_json_string(self):
        """Test to_json_string method of Base"""
        Base._Base__nb_objects = 0

        b1 = Base()
        json_string1 = Base.to_json_string([b1.to_dictionary()])
        self.assertEqual(json_string1, '[{"id": 1}]')

        b2 = Base(10)
        json_string2 = Base.to_json_string([b1.to_dictionary(), b2.to_dictionary()])
        self.assertEqual(json_string2, '[{"id": 1}, {"id": 10}]')

    def test_base_from_json_string(self):
        """Test from_json_string method of Base"""
        Base._Base__nb_objects = 0

        json_string1 = '[{"id": 1}]'
        list_dict1 = Base.from_json_string(json_string1)
        self.assertEqual(len(list_dict1), 1)
        self.assertEqual(list_dict1[0]["id"], 1)

        json_string2 = '[{"id": 1}, {"id": 10}]'
        list_dict2 = Base.from_json_string(json_string2)
        self.assertEqual(len(list_dict2), 2)
        self.assertEqual(list_dict2[0]["id"], 1)
        self.assertEqual(list_dict2[1]["id"], 10)

    def test_base_save_to_file(self):
        """Test save_to_file method of Base"""
        Base._Base__nb_objects = 0

        b1 = Base()
        b2 = Base(10)
        Base.save_to_file([b1, b2], "base.json")

        with open("base.json", "r") as file:
            file_content = file.read()
            self.assertNotEqual(file_content, "")

    def test_base_load_from_file(self):
        """Test load_from_file method of Base"""
        Base._Base__nb_objects = 0

        b1 = Base()
        b2 = Base(10)
        Base.save_to_file([b1, b2], "base.json")

        loaded_bases = Base.load_from_file("base.json")
        self.assertEqual(len(loaded_bases), 2)
        self.assertIsInstance(loaded_bases[0], Base)
        self.assertEqual(loaded_bases[0].id, 1)
        self.assertEqual(loaded_bases[1].id, 10)


if __name__ == '__main__':
    unittest.main()
