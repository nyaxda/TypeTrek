#!/usr/bin/python3
"""Runs flask application"""

from web_flask import create_app
from sqlalchemy import create_engine
from models.base_model import Base, DATABASE_URI
from models.user import User
from models.base_model import BaseModel

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

engine = create_engine(DATABASE_URI)
Base.metadata.create_all(engine)
