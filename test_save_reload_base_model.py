#!/usr/bin/python3

from typing import Dict

from models import storage
from models.base_model import BaseModel

all_objs: Dict[str, BaseModel] = storage.all()
print("-- Reloaded objects --")
for obj_id, obj in all_objs.items():
    print(obj)

print("-- Create a new object --")
my_model: BaseModel = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
my_model.save()
print(my_model)
