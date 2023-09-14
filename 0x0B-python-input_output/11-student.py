#!/usr/bin/python3
"""this will define a class Student"""


class Student:
    """this will represent a student"""

    def __init__(self, first_name, last_name, age):
        """this will start a new Student.

        Arguments:
            first_name: This will be the student's first name
            last_name: This will be the student's last name
            age: This will be the student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """this will retreive a dictionary representation of the student

        Arguments:
            attrs: this will be the attribute to be represented
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """this will substitute all the attributes of the Student

        Arguments:
            json: this is the value that will be used to substitute the attributes
        """
        for k, v in json.items():
            setattr(self, k, v)
