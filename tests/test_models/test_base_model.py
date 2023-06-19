#!/usr/bin/python3
"""Suite of tests for the BaseModel class that every other class inherits from
"""
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os


class TestBaseModel(unittest.TestCase):
    """
    Test cases for BaseModel
    """

    def __init__(self, *args, **kwargs):
        """
        Instantiation tests
        """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """
        Set up tests
        """
        pass

    def tearDown(self):
        """
        Tear down tests
        """
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_default(self):
        """
        Tests for default and attributes
        """
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """
        Tests for keyword arguments
        """
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """
        Testing integer keyword arguments
        """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """ Testing save() """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """
        Testing the __str__() method
        """
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """
        Testing todict()
        """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """
        Testing absence of keyword argument
        """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """Testing only one keyword argument"""
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = self.value(**n)

    def test_id(self):
        """Testing id"""
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """Testing created_at"""
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """Testing updated_at"""
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)
