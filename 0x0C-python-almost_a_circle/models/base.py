#!/usr/bin/python3
"""Defines a base model class."""
import json
import csv
import turtle


class Base:
    """Represent the base model.

    Represents the "base" for all other classes in project 0x0C*.

    Attributes:
        __nb_objects (int): The number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.

        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if not list_dictionaries:
            return "[]"

        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """  JSON Save file """
        json_data = []
        filename = cls.__name__ + ".json"
        if list_objs:
            for obj in list_objs:
                json_data.append(obj.to_dictionary())

        json_string = cls.to_json_string(json_data)
        with open(filename, "w", encoding="utf-8") as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if not json_string or len(json_string) == 0:
            return []
        return json.loads(json_string)

     @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all the attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances of type caller class from a file"""
        filename = cls.__name__ + ".json"

        try:
            with open(filename, encoding="utf-8") as myfile:
                rd = myfile.read()
                dicst = cls.from_json_string(rd)
                inslist = []
                for i in dicst:
                    inslist.append(cls.create(**i))
                return inslist
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Serializes CSV and saves """
        filename = cls.__name__ + ".csv"
        csvlist = []
        if list_objs:
            for i in list_objs:
                dic = i.to_dictionary()
                if cls.__name__ == "Rectangle":
                    csvlist.append([dic["id"], dic["width"],
                                   dic["height"], dic["x"], dic["y"]])

                elif cls.__name__ == "Square":
                    csvlist.append([dic["id"], dic["size"],
                                   dic["x"], dic["y"]])

        with open(filename, "w", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerows(csvlist)

    @classmethod
    def load_from_file_csv(cls):
        """ Deserializes CSV and load """
        filename = cls.__name__ + ".csv"

        try:
            with open(filename, encoding="utf-8") as f:
                r = csv.reader(f)
                if cls.__name__ == "Rectangle":
                    att = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == "Square":
                    att = ["id", "size", "x", "y"]
                inslist = []
                for row in r:
                    ct, dic = 0, {}
                    for i in row:
                        dic[att[ct]] = int(i)
                        ct += 1
                    inslist.append(cls.create(**dic))
                return inslist
        except IOError:
            return []

    def draw(list_rectangles, list_squares):
        """draws all rectangles and squares"""
