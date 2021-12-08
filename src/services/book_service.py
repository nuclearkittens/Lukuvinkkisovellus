import urllib.request
import json
from config import isbn_url


class BookService:
    def __init__(self, book_repository):
        self._book_repository = book_repository

    def new_book(self, book, user_id):
        return self._book_repository.add_book(book, user_id)

    def update_book(self, author, title, description, isbn, book_id):
        """
        First searches that book to be updated exists based on book_id. 
        Then updates its fields.

        Args:
            author (String): Updated author of the book.
            title (String): Updated title of the book.
            description (String): Updated description of the book.
            isbn (String): Updated isbn of the book.
            book_id (Integer): Id of the book to be updated.

        Returns:
            Boolean: True if update was successful.
        """
        book_db_row = self._book_repository.get_book(book_id)
        # Update only if book was actually found
        if book_db_row != None and len(book_db_row) > 0:
            return self._book_repository.update_book(author, title, description, isbn, book_id)
        return False

    def get_my_books(self, user_id):
        """
        Matches given user_id to found books from the database and returns them.

        Args:
            user_id (Integer): user_id of the logged in user.

        Returns:
            List(Tuple) / None: List of books if any is found. Else None.
        """
        my_books = self._book_repository.get_users_books(user_id)
        if len(my_books) == 0:
            return None
        else:
            return my_books

    def mark_book_finished(self, book_id):
        return self._book_repository.mark_finished(book_id)

    def is_book_mine(self, user_id, book_id):
        return self._book_repository.is_owner(user_id, book_id)

    def get_book_info_from_isbn(self, isbn):
        """
        Returns (str, str) the author(s) and title of a book given an ISBN code.

        Args:
        isbn (String): ISBN code of book.
        """

        query_url = isbn_url + isbn
    
        with urllib.request.urlopen(query_url) as response:
            response_text = response.read()
            data = json.loads(response_text.decode())["items"][0]
            
            title = data["volumeInfo"]["title"]
            authors = ",".join(data["volumeInfo"]["authors"])

        return(authors, title)

