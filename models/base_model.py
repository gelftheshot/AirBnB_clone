#!/usr/bin/python3
"""
This module contains the BaseModel
 class which serves as the "base" for all other
model classes in this application.
 It includes common attributes and methods
that can be inherited by subclasses.

Imported modules:
    uuid: This module is used
      to generate unique IDs for instances.
    datetime: This module is used to handle date
      and time information.
    models: This module contains the
      application's models.
"""
import uuid
from datetime import datetime

import models

FORMAT = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    def __init__(self, *args, **kwargs):
        """
        Initialize the BaseModel instance.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Attributes:
            id (str): Unique id generated using uuid.
            created_at (datetime): Current date and
              time when instance is created.
            updated_at (datetime): Current date
              and time when instance is updated.
        """
        if kwargs:
            for k, v in kwargs.items():
                if k in ("created_at", "updated_at"):
                    self.__dict__[k] = datetime.strptime(v, FORMAT)
                else:
                    self.__dict__[k] = v
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Return the string representation of the
          BaseModel instance.

        Returns:
            str: String representation of the BaseMode
              instance.
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Update the updated_at attribute with the current datetime.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Return a dictionary containing all keys/values
          of the instance’s __dict__.
        """
        return {
            **self.__dict__,
            "created_at": self.created_at.strftime(FORMAT),
            "updated_at": self.updated_at.strftime(FORMAT),
            "__class__": self.__class__.__name__,
        }
