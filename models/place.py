#!/usr/bin/python3
from models.base_model import BaseModel

"""
The Place class inherits from BaseModel
 and adds additional attributes for
 city_id, user_id, name, description, number_rooms, number_bathrooms,
   max_guest, price_by_night, latitude, longitude, and amenity_ids.

Attributes:
    city_id (str): The id of the city the place is located in.
    user_id (str): The id of the user who owns the place.
    name (str): The name of the place.
    description (str): A description of the place.
    number_rooms (int): The number of rooms in the place.
    number_bathrooms (int): The number
    of bathrooms in the place.
    max_guest (int): The maximum number of guests the place can accommodate.
    price_by_night (int): The price per night to stay at the place.
    latitude (float): The latitude of the place's location.
    longitude (float): The longitude of the place's location.
    amenity_ids (list): A list of amenity ids associated with the place.

Methods:
    Inherited from BaseModel.
"""


class Place(BaseModel):
    """
    This class represents a Place and
      inherits from the BaseModel class.
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
