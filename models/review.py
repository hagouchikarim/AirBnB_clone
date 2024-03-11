#!/usr/bin/python3
"""Module for File Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """a module for review file"""
    place_id = ""
    user_id = ""
    text = ""
