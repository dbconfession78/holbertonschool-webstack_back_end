#!/usr/bin/python3

"""
module: base_model
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    BaseModel - defines the parent model for all other model types
    """
    def __init__(self):
        """ initializes BaseModel """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
