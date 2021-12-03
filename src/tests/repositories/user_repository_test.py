import unittest
from repositories.user_repository import UserRepository
from app import app
from db import db
from entities.user import User
from tests.database_test_helper import Database_test_helper as dth


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        empty_database = dth(db).delete()        
        self.user_repository = UserRepository(db)
        self.test_user = User("tester", "tester123")
        self.empty_user = None

    def test_add_user_with_valid_params(self):
        self.assertTrue(self.user_repository.add_user(self.test_user))
        
    def test_add_user_with_invalid_params(self):    
        self.assertFalse(self.user_repository.add_user(self.empty_user))

    def test_get_user(self):
        self.user_repository.add_user(self.test_user)

        self.assertEqual(self.user_repository.get_user(
            self.test_user)[1], self.test_user.password)
