#!/usr/bin/python3
"""Module containing unittests of the Place class"""
from tests.test_models.test_base_model import TestBaseModel
from models.place import Place


class TestPlace(TestBaseModel):
    """Testing attributes and methods of the Place class"""

    def __init__(self, *args, **kwargs):
        """Tests for instantiation of new objects"""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """Tests pf the city_id attribute"""
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """Tests for the user_id attribute"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """Tests for the name attribute"""
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """Tests for the description attribute"""
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """Tests for number_of_bathrooms attribute"""
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """Tests for max_guests attribute"""
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """Tests for the price_by_night attribute"""
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """Tests for the latitude attribute"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """Tests for the longitude attribute"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """Tests for the amenity_ids attribute"""
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
