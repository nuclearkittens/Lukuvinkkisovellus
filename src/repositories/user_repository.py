from entities.user import User

class UserRepository:
    def __init__(self, db):
        self._db = db

    def get_user(self, username):
        sql = "SELECT id, password FROM users WHERE username=:username"
        result = self._db.session.execute(sql, {"username": username})
        return result.fetchone()
    
    def add_user(self, username, password):
        try:
            sql = "INSERT INTO users (username, password) VALUES (:username,:password)"
            self._db.session.execute(sql, {"username": username, "password": password})
            self._db.session.commit()
            return True
        except:
            return False