from entities.user import User
from repositories.user_repository import (
    user_repository as default_user_repository
)


class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository


user_service = UserService()
