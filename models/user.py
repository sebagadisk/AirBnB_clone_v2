#!/usr/bin/python3
"""
Defines a User Class
"""

from models.base_model import BaseModel


class User(BaseModel):
    """a class that inherits from Base Model"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
