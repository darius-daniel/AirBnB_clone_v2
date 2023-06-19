#!/usr/bin/python3
""" A suit of unittests for Amenity objects
"""
from tests.test_models.test_base_model import TestBaseModel
from models.amenity import Amenity


class TestAmenity(TestBaseModel):
    """
    Perform tests on the Amenity class
    """

    def __init__(self, *args, **kwargs):
        """
        Tests on new object instantiation
        """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """
        Test a new object's name
        """
        new = self.value()
        self.assertEqual(type(new.name), str)
