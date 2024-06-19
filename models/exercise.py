#!/usr/bin/python3

from sqlalchemy import Column, String, Text, CheckConstraint
from .base_model import BaseModel

class Exercise(BaseModel):
    __tablename__ = 'exercises'
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    difficulty_level = Column(String(50), nullable=False)
    __table_args__ = (CheckConstraint("difficulty_level in ('beginner', 'intermediate', 'hard')", name='chk_difficulty'),)
