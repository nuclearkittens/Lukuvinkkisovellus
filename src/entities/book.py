class Book:
    # tags and related_courses as String-lists
    def __init__(self, author, description, title, isbn=None):
        """
        Creates book object.

        Args:
            author (String): Author of the book.
            title (String): Title of the book.
            description (String): Description of the book.
            isbn (String, optional): ISBN-code of the book. Defaults to None.
        """
        self._author = author
        self._title = title
        self._description = description
        self._isbn = isbn
        

    def get_author(self):
        """
        Return author of the book.

        Returns:
            String: Author given when descriptionthis book-object was constructed.
        """
        return self._author

    def set_author(self, author):
        """
        Sets a new author for the book.

        Args:
            author (String): Author of the book.
        """

        self._author = author

    def get_title(self):
        """
        Return title of the book.

        Returns:
            String: title given when this book-object was constructed.
        """
        return self._description

    def set_title(self, title):
        """
        Sets a new title for the book.

        Args:
            title (String): title of the book.
        """

        self._title = title

    def get_description(self):
        """
        Return description of the book.

        Returns:
            String: Description given when this book-object was constructed.
        """
        return self._description

    def set_description(self, description):
        """
        Sets a new description for the book.

        Args:
            description (String): description of the book.
        """

        self._description = description

    def get_isbn(self):
        """
        Return ISBN of the book.

        Returns:
            String: ISBN given when this book-object was constructed.
        """
        return self._isbn

    def set_isbn(self, isbn):
        """
        Sets a new isbn for the book.

        Args:
            isbn(String): Isbn of the book.
        """

        self._isbn = isbn