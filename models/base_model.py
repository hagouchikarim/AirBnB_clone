#!/usr/bin/python3
"""
The BaseModel class is the base class for all models in the application.
It defines common attributes and methods for all models.
This module also defines the storage for the models.
Each model is responsible for its own storage, so this module is just a
helper to manage the serialization and deserialization of instances.
"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    A Base class for all the models that can
    define common attributes and methods.
    """

    def __init__(self, *args: any, **kwargs: any) -> None:
        """
        This Function can initialize a new instance of the BaseModel class.

        Args:
            *args: Variable length arguments.
            **kwargs: Arbitrary keyword arguments.
        """
        self.id = kwargs.get('id', str(uuid4()))
        self.created_at = kwargs.get('created_at', datetime.now())
        self.updated_at = kwargs.get('updated_at', datetime.now())

        for key, value in kwargs.items():
            if key in ["created_at", "updated_at"]:
                self.__dict__[key] = datetime \
                    .strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
            elif key != "__class__":
                setattr(self, key, value)

        if not kwargs:
            models.storage.new(self)

    def __str__(self) -> str:
        """
        This Function can returns a string representation of the instance.

        Returns:
            str: String representation of the instance.
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self) -> None:
        """
        This Function Update instance updated_at
        attribute and saves changes after.
        """
        current_time = datetime.now()
        self.updated_at = current_time
        models.storage.save()

    def to_dict(self) -> dict[str, any]:
        """
        Returns a dictionary representation of the instance.

        Returns:
            dict: Dictionary representation of our instance.
        """
        obj_dict = {key: getattr(self, key) for key in self.__dict__}
        obj_dict["__class__"] = self.__class__.__name__
        if not isinstance(obj_dict["created_at"], str):
            obj_dict["created_at"] = obj_dict["created_at"].isoformat()
        if not isinstance(obj_dict["updated_at"], str):
            obj_dict["updated_at"] = obj_dict["updated_at"].isoformat()
        return obj_dict
