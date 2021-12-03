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
            sql = "INSERT INTO books (author, title, type, isbn, user_id) \
                    VALUES (:author, :title, 'Book', :isbn, :user_id)"
            self._db.session.execute(
                sql, {"author": author, "title": title, "isbn": isbn, "user_id": user_id})
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
            result = self._db.session.execute(sql, {"user_id": user_id})
            return result.fetchall()
        except:
            return None

    def delete(self):
        self._db.session.execute("DELETE FROM books CASCADE")
        self._db.session.commit()
