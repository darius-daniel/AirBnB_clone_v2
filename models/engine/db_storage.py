#!/usr/bin/python3
""" A new Engine that interacts with a MySQL server rather than a json file
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.state import Base
import os


class DBStorage:
    """ A class that handles file storage in a database
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        Initialize a new instance of DBStorage
        """
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                os.environ['HBNB_MYSQL_USER'],
                os.environ['HBNB_MYSQL_PWD'],
                os.environ['HBNB_MYSQL_HOST'],
                os.environ['HBNB_MYSQL_DB']
            ),
            pool_pre_ping=True
        )
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()

        if os.environ['HBNB_ENV'] == 'test':
            self.__session.execute('DROP * FROM {}'.format(os.environ['HBNB_MYSQL_DB']))

    def all(self, cls=None):
        if cls:
            objs = self.__session.query(cls).all()

            result = {}
            for obj in objs:
                cls_name = str(cls).split('.')[-1].rstrip("'>")
                obj_id = cls.__getattribute__('id')
                key = "{}.{}".format(cls_name, obj_id)
                result[key] = obj

                return result
