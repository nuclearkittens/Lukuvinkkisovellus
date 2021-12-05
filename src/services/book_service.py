class BookService:
    def __init__(self, book_repository):
        self._book_repository = book_repository

    def new_book(self, book, user_id):
        return self._book_repository.add_book(book, user_id)

    def get_my_books(self, user_id):
        return self._book_repository.get_users_books(user_id)

    def mark_book_finished(self, book_id):
        return self._book_repository.mark_finished(book_id)

    def is_book_mine(self, user_id, book_id):
        return self._book_repository.is_owner(user_id, book_id)
