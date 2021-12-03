import unittest
from entities.user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        pass

    def test_user_is_constructed_correctly(self):
        user = User(username="Paavo", password="pesusieni")

        self.assertEqual("Paavo", user.username)
        self.assertEqual("pesusieni", user.password)
