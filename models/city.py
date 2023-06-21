#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from models.place import Place
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    state_id = Column(
        String(60),
        ForeignKey('states.id'),
        nullable=False,
        primary_key=True
    )
    name = Column(String(128), nullable=False)
    places = relationship(
        'Places',
        backref='cities'
        cascade='all, delete, delete-orphan'
    )
