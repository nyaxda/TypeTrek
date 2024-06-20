#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from models.exercise import Exercise  # Adjust the import according to your project structure
from models.base_model import Base

DATABASE_URI = 'mysql+mysqldb://project:Mg(HCO3)2@localhost/TypeTrek'

# Create a new database session
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

# Sample data to insert
sample_exercises = [
    {
        'title': 'Home Row Practice',
        'content': 'asdf jkl; asdf jkl; asdf jkl; asdf jkl;',
        'created_at': datetime(2024, 6, 20, 10, 0, 0),
        'updated_at': datetime(2024, 6, 20, 10, 0, 0),
        'difficulty_level': 'beginner'
    },
    {
        'title': 'Basic Words',
        'content': 'the quick brown fox jumps over the lazy dog',
        'created_at': datetime(2024, 6, 20, 10, 0, 0),
        'updated_at': datetime(2024, 6, 20, 10, 0, 0),
        'difficulty_level': 'beginner'
    },
    {
        'title': 'Short Paragraphs',
        'content': 'Typing is a skill that is necessary for many jobs. Practicing regularly can improve your typing speed and accuracy.',
        'created_at': datetime(2024, 6, 20, 10, 0, 0),
        'updated_at': datetime(2024, 6, 20, 10, 0, 0),
        'difficulty_level': 'beginner'
    },
    {
        'title': 'Advanced Practice',
        'content': 'The quick brown fox jumps over the lazy dog. This pangram contains every letter in the alphabet and is often used for typing practice.',
        'created_at': datetime(2024, 6, 20, 10, 0, 0),
        'updated_at': datetime(2024, 6, 20, 10, 0, 0),
        'difficulty_level': 'hard'
    },
    {
        'title': 'Intermediate Drills',
        'content': 'Practicing typing drills can help improve your typing speed and accuracy over time. Consistency is key to making progress.',
        'created_at': datetime(2024, 6, 20, 10, 0, 0),
        'updated_at': datetime(2024, 6, 20, 10, 0, 0),
        'difficulty_level': 'intermediate'
    }
]

# Insert data into the database
for data in sample_exercises:
    exercise = Exercise(
        title=data['title'],
        content=data['content'],
        difficulty_level=data['difficulty_level']
    )
    session.add(exercise)

try:
    session.commit()
    print("Sample data inserted successfully.")
except Exception as e:
    session.rollback()
    print(f"Error occurred: {e}")
finally:
    session.close()
