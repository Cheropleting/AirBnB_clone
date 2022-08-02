#!/usr/bin/python3
"""class review"""

from models.base_model import BaseModel


class Review(BaseModel):
    """class review"""

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """constructor class"""
        super().__init__(*args, **kwargs)
