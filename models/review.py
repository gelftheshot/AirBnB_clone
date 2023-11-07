#!/usr/bin/python3
from models.base_model import BaseModel

"""
The Review class inherits from BaseModel and adds additional attributes for place_id, user_id, and text.

Attributes:
    place_id (str): The id of the place the review is for.
    user_id (str): The id of the user who wrote the review.
    text (str): The text of the review.

Methods:
    Inherited from BaseModel.
"""

class Review(BaseModel):
    """
    This class represents a Review and inherits from the BaseModel class.
    """
    place_id = ""
    user_id = ""
    text = ""
