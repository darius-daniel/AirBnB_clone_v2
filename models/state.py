#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state')

    @property
    def cities(self):
        """Returns the list of city instances with state_id = self.State.id
        """
        matches = []
        for city in State.cities:
            if city.state_id == State.id:
                matches.append(city)
        return matches
