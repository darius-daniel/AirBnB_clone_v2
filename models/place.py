#!/usr/bin/python3
""" Place Module for HBNB project """
import models
import os
from models.base_model import BaseModel, Base
from models.review import Review
from models.amenity import Amenity
from sqlalchemy import Column, String, Integer, ForeignKey, Float
from sqlalchemy import ForeignKeyConstraint
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if os.getenv("HBNB_TYPE_STORAGE") == 'db':
        reviews = relationship(
            'Review',
            cascade='all, delete, delete-orphan',
            backref='place'
        )
    else:
        @property
        def reviews(self):
            """
            Returns the list of Review instances with their place_id == Place.id
            """
            objs = models.storage.all()
            classes = []
            result = []

            for obj in objs:
                if obj.split('.')[0] == 'Review':
                    classes.append(objs[obj])

            for item in classes:
                if (item.place_id == self.id):
                    result.append(item)

            return result
