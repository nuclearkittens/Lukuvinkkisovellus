class Book:
    # tags and related_courses as String-lists
    def __init__(self, author, title, isbn = None, tags = None, related_courses = None):
        self._author = author
        self._title = title
        self._isbn = isbn
        self._tags = tags
        self._related_courses = related_courses


