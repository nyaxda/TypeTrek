#!/usr/bin/python3
""" sets up the exercise model """

from sqlalchemy import Column, String, Text, CheckConstraint
from sqlalchemy.orm import relationship
from .base_model import BaseModel


class Exercise(BaseModel):
    """ Exercise model"""
    __tablename__ = 'exercises'
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    difficulty_level = Column(String(50), nullable=False)
    __table_args__ = (
        CheckConstraint("difficulty_level in ('beginner', 'intermediate', 'hard')",
                        name='chk_difficulty'),)

    # establishes relationship to the Progress Model.
    progress_entries = relationship("Progress", back_populates="exercise")
