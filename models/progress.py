#!/usr/bin/python3
"""sets up the progress model"""

from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime
from models.base_model import BaseModel
from sqlalchemy.orm import relationship
from datetime import datetime


class Progress(BaseModel):
    """Progress model"""
    __tablename__ = 'progress'
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    exercise_id = Column(Integer, ForeignKey('exercises.id'), nullable=False)
    accuracy = Column(Float, nullable=False)
    words_per_minute = Column(Float, nullable=False)
    strokes_per_minute = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

    # establishes the relationship to Exercise model
    exercise = relationship("Exercise", back_populates="progress_entries")
