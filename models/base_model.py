#!usr/bin/python3
"""
Has Basemodel Class
"""

import models
from datetime import datetime
from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BaseModel:
    """
    Base class for other classes to inherit from
    """
    #Ensures that the class is not
    # mapped to a database table, because is a base class for other models
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow,
                        onupdate=datetime.utcnow)

    def __tablename__(cls):
        """Return the tablename"""
        return cls.__name__.lower()

    def save(self):
        """Save the current instance to the storage"""
        from . import db
        try:
            if not self.id:
                db.session.add(self)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(f"Error occured during save: {e}")

    def delete(self):
        """Delete the current instance from the storage"""
        from . import db
        try:
            db.session.delete(self)
            db.session.commit()
        except Exception as e:
            pring(f"Error occured during delete: {e}")

    def to_dict(self):
        try:
            return {column.name: getattr(self, column.name) for column in self.__table__.columns}
        except AttributeError as e:
            print(f"Error occured during conversion to dict: {e}")
            return {}
