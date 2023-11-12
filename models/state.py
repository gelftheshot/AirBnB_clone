#!/usr/bin/python3
from models.base_model import BaseModel

"""
The State class inherits from BaseModel
 and adds an additional attribute for name.

Attributes:
    name (str): The name of the state.

Methods:
    Inherited from BaseModel.
"""


class State(BaseModel):
    """
    This class represents a State and inherit
      from the BaseModel class.
    """
    name = ""
