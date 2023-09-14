#!/usr/bin/python3
"""this will define a class Student"""


class Student:
    """this will represent a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Arguments:
            first_name: This will be the student's first name
            last_name: This will be the student's last name
            age: This will be the student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """this will retreive a dictionary representation of the student"""
        return self.__dict__
