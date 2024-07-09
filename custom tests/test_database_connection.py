#!/usr/bin/python3
"""This module is a debugging tool meant to check database connectivity"""

from sqlalchemy import create_engine

DATABASE_URI = 'mysql+mysqldb://project:Mg(HCO3)2@localhost/TypeTrek'

try:
    engine = create_engine(DATABASE_URI)
    connection = engine.connect()
    print("Connection to database was successful!")
except Exception as e:
    print("Failed to connect to database. The error is as follows:")
    print(e)

if 'connection' in locals():
    connection.close()
