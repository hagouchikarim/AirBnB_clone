from uuid import uuid4
from datetime import datetime
import models

class BaseModel:
    """
    A Baseclass for all the models that can  defines common attributes and methods.
    """

    def __init__(self, *args, **kwargs) -> None:
    """
    This Function can initialize a new instance of the BaseModel class.
    Args:
        *args: Variable length .
        **kwargs: Arbitrary .
    """
    self.id = kwargs.get('id', str(uuid4()))
    self.created_at = kwargs.get('created_at', datetime.now())
    self.updated_at = kwargs.get('updated_at', datetime.now())

    for key, value in kwargs.items():
        if key in ["created_at", "updated_at"]:
            self.__dict__[key] = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
        elif key != "__class__":
            setattr(self, key, value)

    if not kwargs:
        models.storage.new(self)


    def __str__(self) -> str:
    """
    This Function can returns a string representation of the instance.
    Returns:
        str: Stringrepresentationoftheinstance.
    """
    attributes_str = ", ".join([f"{key}={value}" for key, value in self.__dict__.items()])
    return f"[{self.__class__.__name__}] (id={self.id}, {attributes_str})"

    def save(self) -> None:
    """
    This Function Update  instance updated_at attribute and saves changes after .
    """
    current_time = datetime.now()
    self.updated_at = current_time
    models.storage.save()

    def to_dict(self) -> dict:
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

