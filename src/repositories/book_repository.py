from sqlalchemy import exc
from entities.tag import Tag
from entities.book import Book


class BookRepository:
    def __init__(self, db):
        self._db = db

    def add_book(self, book, user_id):
        """
        Adds Book-object to database and links it to current user with id.

        Args:
            book (Book): Book-object to be added
            user_id (Integer): Id of the user adding the book.

        Returns:
            Boolen: True if successful.
        """
        try:
            author = book.get_author()
            title = book.get_title()
            isbn = book.get_isbn()
            description = book.get_description()
            sql = "INSERT INTO books (author, title, description, type, isbn, user_id) \
                    VALUES (:author, :title, :description, 'Book', :isbn, :user_id)"
            self._db.session.execute(
                sql, {"author": author, "title": title, "description": description, "isbn": isbn, "user_id": user_id})
            self._db.session.commit()
            return True
        except:
            return False

    def mark_finished(self, book_id):
        """
        Adds timestamp to the marked_read field on the row of this book-id.

        Args:
            book_id (Integer): Id of the book to be marked finished.

        Returns:
            Boolean: True, if marking was successful.
        """
        try:
            sql = "UPDATE books SET marked_read=NOW() WHERE id=:book_id"
            self._db.session.execute(sql, {"id": book_id})
            self._db.session.commit()
            return True
        except:
            return False

    def is_owner(self, user_id, book_id):
        """
        Checks if the user-id and the book-id are in the same row in the database.

        Args:
            user_id (Integer): User-id of the currently logged in user.
            book_id (Integer): Book-id of the book to be checked.

        Returns:
            Boolean: True if logged user and book-id matches.
        """
        try:
            sql = "SELECT * FROM books WHERE user_id=:user_id AND id=:book_id"
            result = self._db.session.execute(sql, {"user_id": user_id, "book_id": book_id})
            if result.fetchone() is not None:
                return True
            else:
                return False
        except:
            return False

    def get_book(self, book_id):
        try:
            sql = "SELECT * FROM books WHERE id=:book_id"
            result = self._db.session.execute(sql, {"book_id": book_id})
            return result.fetchone()
        except:
            return None

    def update_book(self, author, title, description, isbn, book_id):
        try:
            sql = "UPDATE books SET author=:author, title=:title, description=:description, isbn=:isbn WHERE id=:book_id"
            self._db.session.execute(sql, {"author": author, "title": title, "description": description, "isbn": isbn, "book_id": book_id})
            self._db.session.commit()
            return True
        except:
            return False

    def get_users_books(self, user_id):
        """
        Gets all added books by the given user-id.

        Args:
            user_id (Integer): Id of the user whose books will be retrieved.

        Returns:
            List(Tuple): List of books found. If no books were found, return None.
        """
        try:
            sql = "SELECT * FROM books WHERE user_id=:user_id"
            result = self._db.session.execute(sql, {"user_id": user_id}).fetchall()
            books = []
            for data in result:
                tags = self.get_tags_by_book(data[0])
                book = Book(
                    author=data[1],
                    title=data[2],
                    description=data[3],
                    read=data[7],
                    id=data[0],
                    isbn=data[5],
                    tags=tags
                    )
                books.append(book)
            return books
        except:
            return None

    def mark_finished(self, book_id):
        try:
            sql = "UPDATE books SET marked_read=NOW() WHERE id=:book_id"
            self._db.session.execute(sql, {"book_id": book_id})
            self._db.session.commit()
            return True
        except:
            return False

    def get_books_by_tag(self, tag_id):
        try:
            sql = "SELECT * FROM books, book_tags \
                WHERE book_tags.tag_id=:tag_id AND \
                    book_tags.book_id=books.id"
            result = self._db.session.execute(
                sql, {"tag_id": tag_id})
            return result.fetchall()
        except:
            return None
    
    def get_tags_by_book(self, book_id):
        try:
            sql = "SELECT tags.id, tags.tag FROM tags, \
                book_tags WHERE book_tags.tag_id=tags.id \
                    AND book_tags.book_id=:book_id"
            result = self._db.session.execute(
                sql, {"book_id": book_id}).fetchall()
            tags = []
            for data in result:
                tag = Tag(data[0], data[1])
                tags.append(tag)
            return tags
        except:
            return None

    def attach_tag(self, tag_id, book_id):
        try:
            sql = "INSERT INTO book_tags (tag_id, book_id) \
                    VALUES (:tag_id, :book_id)"
            self._db.session.execute(
                sql, {"tag_id": tag_id, "book_id": book_id})
            self._db.session.commit()
            return True
        except:
            return False

    def remove_tag(self, tag_id, book_id):
        try:
            sql = "DELETE FROM book_tags \
                WHERE tag_id=:tag_id AND book_id=:book_id"
            self._db.session.execute(
                sql, {"tag_id": tag_id, "book_id": book_id})
            self._db.session.commit()
            return True
        except:
            return False
