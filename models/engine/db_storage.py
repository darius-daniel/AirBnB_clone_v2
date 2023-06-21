#!/usr/bin/python3
""" A new Engine that interacts with a MySQL server rather than a json file
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
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

        if os.environ['HBNB_ENV'] == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Query on the current database session depending on the class name
        """
        pass

    def new(self, obj):
        """Add new object the current database session
        """
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """Delete a non-None object @obj from the current db session
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ Creates all tables in the db and creates the current db session
        from the engine
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine,
            expire_on_commit=False,
        )
        Session = scoped_session(session_factory)
        session = Session()
