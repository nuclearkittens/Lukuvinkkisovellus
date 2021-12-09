import unittest
from services.book_service import BookService
from entities.book import Book


class StubRepo:
    def __init__(self):
        self.books = []
        self.book_id = 0

    def add_book(self, book, user_id):
        self.books.append((user_id, book))
        self.book_id += 1

        return True

    def get_users_books(self, user_id):
        return [book for book in self.books if book[0] == user_id]    


class TestBookService(unittest.TestCase):
    def setUp(self):
        self.repo = StubRepo()
        self.service = BookService(self.repo)
        self.test_book = Book("author", "title", "isbn1", "a fine book")
        self.user_id = 1
        self.other_user_id = 2
        self.service.new_book(self.test_book, self.user_id)

    def test_user_can_add_book(self):
        a_book = Book("another author", "another tilte", "isbn+1", "a good read")
        response = self.service.new_book(a_book, self.user_id)

        self.assertTrue(response)

    def test_user_can_get_list_of_their_books(self):
        books = self.service.get_my_books(self.user_id)

        self.assertEqual(len(books), 1)
        self.assertEqual(books[0][0], self.user_id)

    def test_user_only_gets_their_own_books(self):
        a_book = Book("another author", "another tilte", "isbn+1", "a good read")
        self.service.new_book(a_book, self.other_user_id)
        books = self.service.get_my_books(self.user_id)

        self.assertEqual(len(books), 1)
        self.assertEqual(books[0][0], self.user_id)

    def test_find_and_add_book_with_isbn(self):
        isbn = "1118051076"
        book_info = self.service.get_book_info_from_isbn(isbn)
        author = book_info["author"]
        title = book_info["title"]

        found_book = Book(author, title, isbn, "I found me a book")
        response = self.service.new_book(found_book, self.other_user_id)

        self.assertEqual(author, "Wallace Wang")
        self.assertEqual(title, "Beginning Programming For Dummies")
        self.assertTrue(response)

    def test_book_not_found_with_faulty_isbn(self):
        isbn = "666"
        book_info = self.service.get_book_info_from_isbn(isbn)

        self.assertEqual(book_info, None)
