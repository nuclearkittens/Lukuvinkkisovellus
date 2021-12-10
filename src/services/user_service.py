from os import urandom
from werkzeug.security import check_password_hash, generate_password_hash


class UserService:
    def __init__(self, user_repository, session):
        self._user_repository = user_repository
        self._session = session

    """
    Fetches user data from repository and validates user.
    Then checks password hash and creates session.

    Args: 
        user (User): User who wants to login.

    Returns:
        Boolean: True if login was successful

    """

    def login(self, user):
        user_data = self._user_repository.get_user(user)
        if user_data is None:
            return False
        if check_password_hash(user_data[1], user.password):
            self._session["user_id"] = user_data[0]
            self._session["username"] = user.username
            self._session["csrf_token"] = urandom(16).hex()
            return True
        return False

    def register(self, user):
        user.set_password(generate_password_hash(user.password))
        return self._user_repository.add_user(user)

    def logout(self):
        del self._session["user_id"]
        del self._session["username"]
        del self._session["csrf_token"]
