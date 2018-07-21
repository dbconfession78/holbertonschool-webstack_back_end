#!/usr/bin/python3
"""
Module: contains BaseModel class definitiaon
"""
import uuid
from datetime import datetime


class BaseModel:
    """ defines the parent model for all other model types """
    id = None
    created_at = None
    updated_at = None

    def __init__(self):
        """ initializes BaseModel """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at
