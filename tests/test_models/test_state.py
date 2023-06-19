#!/usr/bin/python3
"""A suite of unittests for State object attributes"""
from tests.test_models.test_base_model import TestBaseModel
from models.state import State


class TestState(TestBaseModel):
    """
    Testing all attributes and methods of the State class
    """

    def __init__(self, *args, **kwargs):
        """Instantiation tests"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """Tests on the name attribute"""
        new = self.value()
        self.assertEqual(type(new.name), str)
