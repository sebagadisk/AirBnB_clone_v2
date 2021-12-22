#!/usr/bin/python3
"""
defines all common attributes/mothods for other classes
"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """Base for all AirBnB website projects"""

    TIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self, *args, **kwargs):
        """initializes the basemodel class"""
        if (not kwargs):
            self.id = str(uuid4())
            self.created_at = datetime.today()
            self.updated_at = self.created_at
            models.storage.new(self)
        elif kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        value = datetime.strptime(value, BaseModel.TIME_FORMAT)
                    setattr(self, key, value)

    def __str__(self):
        """returns string representation of this class"""
        name = self.__class__.__name__
        return "[{}] ({}) {}".format(name, self.id, self.__dict__)

    def save(self):
        """updates updated_at with the current datetime"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """returns the dictionary containing all keys of __dict__"""
        representation = {}
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                representation[key] = value.isoformat()
            else:
                representation[key] = value

        representation["__class__"] = self.__class__.__name__
        return representation
