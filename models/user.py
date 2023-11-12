#!/usr/bin/python3
from models.base_model import BaseModel

"""
The User class inherits from BaseModel
 and adds additional attributes for email, password, first_name, and last_name.

Attributes:
    email (str): The email of the user.
    password (str): The password of the user.
    first_name (str): The first name of the user.
    last_name (str): The last name of the user.

Methods:
    Inherited from BaseModel.
"""


class User(BaseModel):
    """
    This class represents a User and inherits from the BaseModel class.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
