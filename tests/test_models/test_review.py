#!/usr/bin/python3
"""A module containing unittests for the Review class"""
from tests.test_models.test_base_model import TestBaseModel
from models.review import Review


class TestReview(TestBaseModel):
    """Tests on the attributes of the Review class"""

    def __init__(self, *args, **kwargs):
        """Tests on instantiation of new objects"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """Tests on the place_id attribute"""
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """Tests on the user_id attribute"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """Tests on the text attribute"""
        new = self.value()
        self.assertEqual(type(new.text), str)
