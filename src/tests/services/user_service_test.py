import unittest
from services.user_service import UserService
from entities.user import User

class StubRepo:
    def __init__(self):
        self.password = ""
    
    def get_user(self, user):
        return ["1", self.password]

    def add_user(self, user):
        self.password = user.password
        return True


class TestUserService(unittest.TestCase):
    def setUp(self):
        self.user = User("username", "password")
        self.repo = StubRepo()
        self.session = {}
        self.service = UserService(self.repo, self.session)

    def test_register_user_completes_succesfully(self):
        self.assertTrue(self.service.register(self.user))
    
    def test_login_succesful_login_returns_true(self):
        self.service.register(self.user)
        self.assertTrue(self.service.login(User("username", "password")))
    
    def test_failed_login_returns_false(self):
        self.service.register(self.user)
        self.assertFalse(self.service.login(User("username", "wrong")))

    def test_login_sets_session(self):
        self.service.register(self.user)
        self.service.login(User("username", "password"))
        self.assertTrue(self.session["username"] == "username")
    
    def test_logout_deletes_session(self):
        self.service.register(self.user)
        self.service.login(User("username", "password"))
        self.service.logout()
        self.assertFalse("username" in self.session)