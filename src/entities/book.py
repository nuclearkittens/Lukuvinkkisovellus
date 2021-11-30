class Book:
    # tags and related_courses as String-lists
    def __init__(self, author, title, description, isbn = None, tags = None, related_courses = None):
        self._author = author
        self._title = title
        self._description = description
        self._isbn = isbn
        self._tags = tags
        self._related_courses = related_courses

    # TARKISTA PSQL ALUSTUS ASIA
    # psql lukuvinkit < schema.sql

