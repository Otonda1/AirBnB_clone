#!/usr/bin/python3
"""
     a class User that inherits from BaseModel:
"""
from models.base_model import BaseModel
class User(BaseModel):
    """
        class that inherits from BaseModel
        
        Attributes:
            email (str): user email
            password (str): user password
            first_name (str): user first name
            last_name (str): user last name
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
