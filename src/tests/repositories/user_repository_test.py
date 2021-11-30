import unittest
from repositories.user_repository import UserRepository
from app import app
from db import db
from entities.user import User


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        self.user_repository = UserRepository(db)
        self.user_repository.delete()
        self.test_user = User("testaaja", "testaaja123")
        self.empty_user = None

    def test_add_user(self):
        self.assertTrue(self.user_repository.add_user(self.test_user))
        self.assertFalse(self.user_repository.add_user(self.empty_user))
    
    def test_get_user(self):
        self.user_repository.add_user(self.test_user)

        self.assertEqual(self.user_repository.get_user(self.test_user)[1], self.test_user.password)