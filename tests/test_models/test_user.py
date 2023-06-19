#!/usr/bin/python3
"""A suite of unittests for User objects"""
from tests.test_models.test_base_model import TestBaseModel
from models.user import User


class TestUser(TestBaseModel):
    """
    Tests on all User attributes and methods
    """

    def __init__(self, *args, **kwargs):
        """Instantiation tests"""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """Tests on the first_name attribute"""
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """Tests on the last_name attribute"""
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """Tests on the email attribute"""
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """Tests on the password attribute"""
        new = self.value()
        self.assertEqual(type(new.password), str)
