import unittest
from repositories.user_repository import UserRepository
import app
from db import db


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        pass

    def test_nothing(self):
        db.session.execute("SELECT * FROM users")
        db.session.commit()
