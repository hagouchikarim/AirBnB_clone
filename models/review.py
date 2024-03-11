#!/usr/bin/python3
from models.base_model import BaseModel


class Review(BaseModel):
    """a module for review file"""
    place_id = ""
    user_id = ""
    text = ""