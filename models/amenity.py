#!/usr/bin/python3
from models.base_model import BaseModel

"""
The Amenity class inherits from BaseModel and adds an additional attribute for name.

Attributes:
    name (str): The name of the amenity.

Methods:
    Inherited from BaseModel.
"""

class Amenity(BaseModel):
    """
    This class represents an Amenity and inherits from the BaseModel class.
    """
    name = ""
