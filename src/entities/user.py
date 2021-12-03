class User:
    def __init__(self, username, password):
        """
        Creates a user object.

        Args:
            username (String): Username
            password (String): Password for user.
        """

        self.username = username
        self.password = password

    def set_password(self, password):
        """
        Sets password for user.

        Args:
            password (String)

        """
        self.password = password
