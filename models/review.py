#!/usr/bin/python3
"""
Describes Review class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents Review:"""

    place_id = ""
    user_id = ""
    text = ""
