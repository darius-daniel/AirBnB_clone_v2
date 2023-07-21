#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state')

    @property
    def cities(self):
        """Returns the list of city instances with state_id = self.State.id
        """
        data = models.storage.all()
        city_objs = []
        matches = []

        for key in data:
            city = key.split('.')
            if city[0] == 'City':
                city_objs.append(data[key])

        for city_obj in city_objs:
            if city_obj.state_id == self.id:
                matches.append(city_obj)
        return matches
