from entities.user import User
from repositories.user_repository import (
    user_repository as default_user_repository
)
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash
from os import urandom
from db import db
import re

class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository

    def login(self, username, password):
        _sql = "SELECT id, password FROM users WHERE username=:username"
        _result = db.session.execute(_sql, {"username":username})
        _user = _result.fetchone()
        if _user == None:
            return False
        else:
            if check_password_hash(_user[1], password):
                session["user_id"] = _user[0]
                session["csrf_token"] = urandom(16).hex()
                return True
            else:
                return False

    def register(self, username, password):
        _hash_val = generate_password_hash(password)
        try:
            _sql = "INSERT INTO users (username, password) VALUES (:username,:password)"
            db.session.execute(_sql, {"username":username, "password":_hash_val})
            db.session.commit()
        except:
            return False
        return self.login(username, password)
    
    def logout(self):
        del session["user_id"]
        del session["csrf_token"]

    def check_username(self, username):
        if (
            len(username) > 12
            or len(username) < 3
            or bool(re.search(r'\W', username))
        ):
            return False
        return True

    def check_password(self, password):
        if (
            len(password) > 16
            or len(password) < 8
        ):
            return False
        return True

user_service = UserService()
