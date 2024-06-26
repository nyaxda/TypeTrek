#!/usr/bin/python3
"""Runs flask application"""
import os
from web_flask import create_app
from sqlalchemy import create_engine
from models.base_model import Base, DATABASE_URI
from models.user import User
from models.exercise import Exercise
from models.progress import Progress
from models.base_model import BaseModel

# Check if MySQL service is running
if os.system('sudo service mysql status') != 0:
    # If not running, start MySQL service
    os.system('sudo service mysql start')

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

engine = create_engine(DATABASE_URI)
Base.metadata.create_all(engine)
