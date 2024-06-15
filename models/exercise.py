#!/usr/bin/python3

from sqalchemy import Column, String, Text
from base_model import BaseModel

class Exercise(BaseModel):
    __tablename__ = 'exercises'
    title = Column(String(100), nullable=False)
    content = Column(Text, nullable=False)
