from entities.user import User
from repositories.user_repository import (
    user_repository as default_user_repository
)
from db import (db as default_db)
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash
from os import urandom
import re


class UserService:
    def __init__(self,
            user_repository=default_user_repository,
            db=default_db
        ):
        self._user_repository = user_repository
        self._db = db

    def login(self, username, password):
        sql = "SELECT id, password FROM users WHERE username=:username"
        result = self._db.session.execute(sql, {"username": username})
        user = result.fetchone()
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
        try:
            sql = "INSERT INTO users (username, password) VALUES (:username,:password)"
            self._db.session.execute(
                sql, {"username": username, "password": hash_val})
            self._db.session.commit()
        except:
            return False
        return True

    def logout(self):
        del session["user_id"]
        del session["username"]
        del session["csrf_token"]

    def check_username(self, username):
        return not (
            len(username) > 12
            or len(username) < 3
            or bool(re.search(r'\W', username))
        )

    def check_password(self, password):
        return not (
            len(password) > 16
            or len(password) < 8
        )


user_service = UserService()
