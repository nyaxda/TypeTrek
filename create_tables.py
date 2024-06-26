#!/usr/bin/python3
"""
Script to manually create database tables, for debugging purposes only
"""
from web_flask import db, create_app
from models.user import User

app = create_app()
with app.app_context():
    print("Creating all tables...")
    db.create_all()
    print("Tables created.")
