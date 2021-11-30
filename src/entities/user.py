class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def set_password(self, password):
        self.password = password
