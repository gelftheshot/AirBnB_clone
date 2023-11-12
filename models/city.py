#!/usr/bin/python3
from models.base_model import BaseModel

"""
The City class inherits from BaseModel
 and adds additional attributes for state_id and name.

Attributes:
    state_id (str): The id of the state
      the city belongs to.
    name (str): The name of the city.

Methods:
    Inherited from BaseModel.
"""


class City(BaseModel):
    """
    This class represents a City and inherits
      from the BaseModel class.
    """
    state_id = ""
    name = ""
