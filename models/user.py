#!/usr/bin/python3
"""sets up the user model"""

from .base_model import BaseModel
from sqlalchemy import Column, String
from werkzeug.security import generate_password_hash, check_password_hash


class User(BaseModel):
    """User model"""
    __tablename__ = 'users'  # setting the table name
    username = Column(String(50), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    email = Column(String(100), unique=True, nullable=False)

    def set_password(self, password):
        """Sets password by hashing it"""
        self.password_hash = generate_password_hash(password)
        self.save()

    def check_password(self, password):
        """check password against the stored hash"""
        return check_password_hash(self.password_hash, password)
