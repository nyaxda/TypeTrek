#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from models.exercise import Exercise
from models.progress import Progress
from models.base_model import Base

DATABASE_URI = 'mysql+mysqldb://project:Mg(HCO3)2@localhost/TypeTrek'

# Create a new database session
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

# Sample data to insert
sample_exercises = [
    {
        'title': 'Accuracy Focus: Special Characters',
        'content': '!@# $%^ &*() _+[] {}|; \':",./ <>? `~ !@# $%^ &*() ' +
                   '_+[] {}|; \':",./ <>? `~ !@# $%^ &*() _+[] {}|; \':",./ ' +
                   '<>? `~ !@# $%^ &*() _+[] {}|; \':",./ <>? `~ !@# $%^ ' +
                   '&*() _+[] {}|; \':",./ <>? `~ !@# $%^ &*() _+[] {}|; ' +
                   '\':",./ <>? `~ !@# $%^ &*() _+[] {}|; \':",./ <>? `~ ' +
                   '!@# $%^ &*() _+[] {}|; \':",./ <>? `~ !@# $%^ &*() ' +
                   '_+[] {}|; \':",./ <>? `~ !@# $%^ &*() _+[] {}|; \':",./ ' +
                   '<>? `~',
        'created_at': datetime(2024, 6, 25, 15, 0, 0),
        'updated_at': datetime(2024, 6, 25, 15, 0, 0),
        'difficulty_level': 'hard'
    },
    {
        'title': 'Accuracy Focus: Long Words',
        'content': 'antidisestablishmentarianism floccinaucinihilipilification ' +
                   'supercalifragilisticexpialidocious pseudopseudohypoparathyroidism ' +
                   'thyroparathyroidectomized pneumonoultramicroscopicsilicovolcanoconiosis ' +
                   'hippopotomonstrosesquipedaliophobia ' +
                   'antidisestablishmentarianism floccinaucinihilipilification ' +
                   'supercalifragilisticexpialidocious pseudopseudohypoparathyroidism ' +
                   'thyroparathyroidectomized pneumonoultramicroscopicsilicovolcanoconiosis ' +
                   'hippopotomonstrosesquipedaliophobia ' +
                   'antidisestablishmentarianism floccinaucinihilipilification ' +
                   'supercalifragilisticexpialidocious pseudopseudohypoparathyroidism ' +
                   'thyroparathyroidectomized pneumonoultramicroscopicsilicovolcanoconiosis ' +
                   'hippopotomonstrosesquipedaliophobia',
        'created_at': datetime(2024, 6, 25, 15, 10, 0),
        'updated_at': datetime(2024, 6, 25, 15, 10, 0),
        'difficulty_level': 'hard'
    },
    {
        'title': 'Accuracy Focus: Mixed Practice',
        'content': 'The quick brown fox jumps over the lazy dog. ' +
                   '123 456 789 0 !@# $%^ &*()_+ `~ -= [] {} | ;:\' ",< .> /? ' +
                   'The quick brown fox jumps over the lazy dog. ' +
                   '123 456 789 0 !@# $%^ &*()_+ `~ -= [] {} | ;:\' ",< .> /? ' +
                   'The quick brown fox jumps over the lazy dog. ' +
                   '123 456 789 0 !@# $%^ &*()_+ `~ -= [] {} | ;:\' ",< .> /? ' +
                   'The quick brown fox jumps over the lazy dog. ' +
                   '123 456 789 0 !@# $%^ &*()_+ `~ -= [] {} | ;:\' ",< .> /? ' +
                   'The quick brown fox jumps over the lazy dog. ' +
                   '123 456 789 0 !@# $%^ &*()_+ `~ -= [] {} | ;:\' ",< .> /? ' +
                   'The quick brown fox jumps over the lazy dog. ' +
                   '123 456 789 0 !@# $%^ &*()_+ `~ -= [] {} | ;:\' ",< .> /?',
        'created_at': datetime(2024, 6, 25, 15, 20, 0),
        'updated_at': datetime(2024, 6, 25, 15, 20, 0),
        'difficulty_level': 'hard'
    },
    {
        'title': 'Accuracy Focus: Code Snippets',
        'content': 'def function():\n    print("Hello, World!")\n    return True\n\n' +
                   'def add(a, b):\n    return a + b\n\n' +
                   'for i in range(10):\n    print(i)\n\n' +
                   'if __name__ == "__main__":\n    function()\n    add(1, 2)\n\n' +
                   'class Example:\n    def __init__(self, value):\n        self.value = value\n\n' +
                   '    def display(self):\n        print(self.value)\n\n' +
                   'example = Example("Hello")\nexample.display()\n\n' +
                   'print("End of coding practice")\n\n' +
                   'def function():\n    print("Hello, World!")\n    return True\n\n' +
                   'def add(a, b):\n    return a + b\n\n' +
                   'for i in range(10):\n    print(i)\n\n' +
                   'if __name__ == "__main__":\n    function()\n    add(1, 2)\n\n' +
                   'class Example:\n    def __init__(self, value):\n        self.value = value\n\n' +
                   '    def display(self):\n        print(self.value)\n\n' +
                   'example = Example("Hello")\nexample.display()\n\n' +
                   'print("End of coding practice")\n\n',
        'created_at': datetime(2024, 6, 25, 15, 30, 0),
        'updated_at': datetime(2024, 6, 25, 15, 30, 0),
        'difficulty_level': 'hard'
    },
    {
        'title': 'Accuracy Focus: Random Text',
        'content': 'Zebras zigzagged zealously while zookeepers zoomed by. ' +
                   'Quaintly quirky quotes quickly quench queries. ' +
                   'Briskly baked bread brings bright bliss. ' +
                   'Clever cats can climb carefully crafted columns. ' +
                   'Daringly dainty dancers delight during dusk. ' +
                   'Eagerly energetic eagles engage effortlessly. ' +
                   'Frogs find fun flipping from fronds. ' +
                   'Gently gliding geese gracefully gather. ' +
                   'Hastily hopping hares hide hurriedly. ' +
                   'Ingenious iguanas imitate interesting insects. ' +
                   'Jovial jugglers jostle jauntily. ' +
                   'Keenly kind kittens keep kites. ' +
                   'Lions leap lightly leaving little landmarks. ' +
                   'Mice meander mysteriously making maps. ' +
                   'Nimble newts nimbly navigate. ' +
                   'Owls observe outside oaks. ' +
                   'Penguins parade pompously. ' +
                   'Quails quietly quiver. ' +
                   'Rabbits rest rapidly. ' +
                   'Snakes slither silently. ' +
                   'Tigers trot tenaciously. ' +
                   'Umbrellas unfold under unusual updrafts. ' +
                   'Vultures vigilantly view. ' +
                   'Wolves wade warily. ' +
                   'Xylophones xenogeny xenoliths. ' +
                   'Yaks yawn yearningly. ' +
                   'Zebras zigzagged zealously while zookeepers zoomed by. ' +
                   'Quaintly quirky quotes quickly quench queries. ' +
                   'Briskly baked bread brings bright bliss. ' +
                   'Clever cats can climb carefully crafted columns. ' +
                   'Daringly dainty dancers delight during dusk. ' +
                   'Eagerly energetic eagles engage effortlessly. ' +
                   'Frogs find fun flipping from fronds. ' +
                   'Gently gliding geese gracefully gather. ' +
                   'Hastily hopping hares hide hurriedly. ' +
                   'Ingenious iguanas imitate interesting insects. ' +
                   'Jovial jugglers jostle jauntily. ' +
                   'Keenly kind kittens keep kites. ' +
                   'Lions leap lightly leaving little landmarks. ' +
                   'Mice meander mysteriously making maps. ' +
                   'Nimble newts nimbly navigate. ' +
                   'Owls observe outside oaks. ' +
                   'Penguins parade pompously. ' +
                   'Quails quietly quiver. ' +
                   'Rabbits rest rapidly. ' +
                   'Snakes slither silently. ' +
                   'Tigers trot tenaciously. ' +
                   'Umbrellas unfold under unusual updrafts. ' +
                   'Vultures vigilantly view. ' +
                   'Wolves wade warily. ' +
                   'Xylophones xenogeny xenoliths. ' +
                   'Yaks yawn yearningly.',
        'created_at': datetime(2024, 6, 25, 15, 40, 0),
        'updated_at': datetime(2024, 6, 25, 15, 40, 0),
        'difficulty_level': 'hard'
    }
]




# Insert data into the database
for data in sample_exercises:
    exercise = Exercise(title=data['title'], content=data['content'], difficulty_level=data['difficulty_level']
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
