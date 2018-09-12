#!/usr/bin/python3
"""
Module: contains BaseModel class definitiaon
"""
import models
from datetime import datetime
import uuid
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (Column, String, DateTime)

Base = declarative_base()


class BaseModel:
    """ defines the parent model for all other model types """
    id = Column(String(60),
                nullable=False,
                primary_key=True)

    created_at = Column(DateTime,
                        nullable=False,
                        default=datetime.utcnow())

    updated_at = Column(DateTime,
                        nullable=False,
                        default=datetime.utcnow(),
                        onupdate=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """ initializes BaseModel """
        if kwargs:
            self.__set_attributes(kwargs)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at

    def __set_attributes(self, attribute_dict):
        if 'id' not in attribute_dict:
            attribute_dict['id'] = str(uuid.uuid4())

        if 'created_at' not in attribute_dict:
            attribute_dict['created_at'] = datetime.utcnow()
        elif not isinstance(attribute_dict['created_at'], datetime):
            attribute_dict['created_at'] = datetime.strptime(
                attribute_dict['created_at'], "%Y-%m-%d %H:%M:%S.%f")

        if 'updated_at' not in attribute_dict:
            attribute_dict['updated_at'] = datetime.utcnow()
        elif not isinstance(attribute_dict['updated_at'], datetime):
            attribute_dict['updated_at'] = datetime.strptime(
                attribute_dict['updated_at'], "%Y-%m-%d %H:%M:%S.%f")

        for (attribute, value) in attribute_dict.items():
            setattr(self, attribute, value)

    def to_json(self):
        obj_class = self.__class__.__name__
        obj_dict = {
            key: value if self.__is_serializable else str(value)
            for key, value in self.__dict__.items()
        }
        obj_dict.pop('_sa_instance_state', None)
        if obj_class == 'User':
            obj_dict.pop("password", None)
        return (obj_dict)

    def save(self):
        """ updates 'updated_at' and commits to db  """
        self.updated_at = datetime.utcnow()
        db_session.add(self)
        db_session.commit()

    def __is_serializable(self, obj_v):
        """
        private: checks if object is serializable
        """
        try:
            obj_to_str = json.dumps(obj_v)
            return obj_to_str is not None and isinstance(obj_to_str, str)
        except:
            return False
