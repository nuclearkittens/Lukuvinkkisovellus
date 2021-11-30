import unittest
from repositories.user_repository import UserRepository
from db import db
from entities.user import User


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        db.session.execute("DELETE FROM users")
        self.user_repository = UserRepository(db)

    def test_db_connection(self):
        db.session.execute(""" 
            INSERT INTO users (username, password)             VALUES ('Paavo', 'pesusieni')

            """)
        db.session.commit()
    
    def test_add_user(self):
        result = self.user_repository.add_user(User('Paavo', 'pesusieni'))
        
        self.assertTrue(result)
