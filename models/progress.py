from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime
from base_model import BaseModel

class Progress(BaseModel):
    __tablename__ = 'progress'
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    exercise_id = Column(Integer, ForeignKey('exercises.id'), nullable=False)
    accuracy = Column(Float, nullable=False)
    words_per_minute = Column(Float, nullable=False)
    strokes_per_minute = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
