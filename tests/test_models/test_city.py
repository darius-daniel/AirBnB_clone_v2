#!/usr/bin/python3
""" Suites of tests for the City class
"""
from tests.test_models.test_base_model import TestBaseModel
from models.city import City


class TestCity(TestBaseModel):
    """
    Tests for the class
    """

    def __init__(self, *args, **kwargs):
        """Testing new object instantiation"""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """Tests for id attribute"""
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """Tests for name attribute"""
        new = self.value()
        self.assertEqual(type(new.name), str)
