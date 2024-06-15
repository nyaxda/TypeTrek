#!/usr/bin/python3

from base_model import BaseModel
from sqlalchemy import Column, String

class User(BaseModel):
    __tablename__ = 'users' #setting the table name
    username = Column(String(50), unique=True, nullable=False)
    password_hash = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
