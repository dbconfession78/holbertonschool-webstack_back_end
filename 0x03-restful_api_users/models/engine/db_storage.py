#!/usr/bin/python3
"""
Database engine
"""

import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models import base_model, user


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        self.class_dict = {
            "user": user.User
        }

        self.__engine = create_engine(
            #            'mysql+mysqldb://{}:{}@{}/{}'.format(
            'mysql+pymysql://{}:{}@{}/{}'.format(
                os.environ.get('HBNB_YELP_MYSQL_USER'),
                os.environ.get('HBNB_YELP_MYSQL_PWD'),
                os.environ.get('HBNB_YELP_MYSQL_HOST'),
                os.environ.get('HBNB_YELP_MYSQL_DB')))
        self.reload()

    def all(self, cls=None):
        """
           returns a dictionary of all objects
        """
        self.reload()
        obj_dict = {}
        if cls is not None:
            a_query = self.__session.query(self.class_dict[cls])
            for obj in a_query:
                obj_ref = "{}.{}".format(type(obj).__name__, obj.id)
                obj_dict[obj_ref] = obj
            return obj_dict

        for c in DBStorage.CNC.values():
            a_query = self.__session.query(c)
            for obj in a_query:
                obj_ref = "{}.{}".format(type(obj).__name__, obj.id)
                obj_dict[obj_ref] = obj
        return obj_dict

    def delete(self, obj=None):
        """
            deletes obj from current database session if not None
        """
        if obj:
            self.__session.delete(obj)
            self.__session.commit()

    def reload(self):
        """
           creates all tables in database & session from engine
        """
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(
            sessionmaker(
                bind=self.__engine,
                expire_on_commit=False))

    def close(self):
        """
            calls remove() on private session attribute (self.session)
        """
        self.__session.remove()

    def count(self, cls=None):
        """
            returns the count of all objects in storage
        """
        count = len(self.all(cls))
        return count
