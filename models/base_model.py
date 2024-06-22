#!usr/bin/python3
"""
Has Basemodel Class
"""

from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URI = 'mysql+mysqldb://project:Mg(HCO3)2@localhost/TypeTrek'
Base = declarative_base()

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()


class BaseModel(Base):
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

    def save(self):
        """Save the current instance to the storage"""
        try:
            if not self.id:
                session.add(self)
            session.commit()
        except Exception as e:
            session.rollback()
            print(f"Error occured during save: {e}")

    def delete(self):
        """Delete the current instance from the storage"""
        try:
            session.delete(self)
            session.commit()
        except Exception as e:
            print(f"Error occured during delete: {e}")
    
    def update(self):
        """Update the current instance in the storage"""
        try:
            session.commit()
        except Exception as e:
            session.rollback()
            print(f"Error occured during update: {e}")

    def to_dict(self):
        try:
            return {column.name: getattr(self, column.name) for column in self.__table__.columns}
        except AttributeError as e:
            print(f"Error occured during conversion to dict: {e}")
            return {}
