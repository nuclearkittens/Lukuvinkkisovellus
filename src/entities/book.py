class Book:
    # tags and related_courses as String-lists
    def __init__(self, author, title, isbn=None, tags=None, related_courses=None):
        """
        Creates book object.

        Args:
            author (String): Author of the book.
            title (String): Title of the book.
            isbn (String, optional): ISBN-code of the book. Defaults to None.
            tags ([type], optional): WIP. Defaults to None.
            related_courses ([type], optional): WIP. Defaults to None.
        """
        self._author = author
        self._title = title
        self._isbn = isbn
        self._tags = tags
        self._related_courses = related_courses

    def get_author(self):
        """
        Return author of the book.

        Returns:
            String: Author given when this book-object was constructed.
        """
        return self._author

    def get_title(self):
        """
        Return title of the book.

        Returns:
            String: Title given when this book-object was constructed.
        """
        return self._title

    def get_isbn(self):
        """
        Return ISBN of the book.

        Returns:
            String: ISBN given when this book-object was constructed.
        """
        return self._isbn

