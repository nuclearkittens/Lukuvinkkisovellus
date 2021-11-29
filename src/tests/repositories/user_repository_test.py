import unittest
from repositories.user_repository import UserRepository
import app
from db import db


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        db.session.execute("DELETE FROM users")

    def test_nothing(self):
        db.session.execute(""" 
            INSERT INTO users (username, password) 
            VALUES ('Paavo', 'pesusieni')

            """)
        db.session.commit()
