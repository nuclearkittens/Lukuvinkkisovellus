from entities.user import User
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash
from os import urandom

class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def login(self, username, password):
        user = self._user_repository.get_user(username)
        if user == None:
            return False
        if check_password_hash(user[1], password):
            session["user_id"] = user[0]
            session["username"] = username
            session["csrf_token"] = urandom(16).hex()
            return True
        return False

    def register(self, username, password):
        hash_val = generate_password_hash(password)
        return self._user_repository.add_user(username, hash_val)

    def logout(self):
        del session["user_id"]
        del session["username"]
        del session["csrf_token"]
