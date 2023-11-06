#!/usr/bin/python3
import uuid
from datetime import datetime

FORMAT = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    def __init__(self, *args, **kwargs):
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

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        return {
            **self.__dict__,
            "created_at": self.created_at.strftime(FORMAT),
            "updated_at": self.updated_at.strftime(FORMAT),
            "__class__": self.__class__.__name__,
        }
