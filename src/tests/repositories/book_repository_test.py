import unittest
from repositories.user_repository import UserRepository
from repositories.book_repository import BookRepository
from repositories.tag_repository import TagRepository
from app import app
from db import db
from entities.book import Book
from entities.user import User
from tests.database_test_helper import Database_test_helper as dth


class TestBookRepository(unittest.TestCase):
    def setUp(self):
        empty_database = dth(db).delete()
        self.book_repository = BookRepository(db)
        self.user_repository = UserRepository(db)
        self.tag_repository = TagRepository(db)
        self.test_book = Book("test_author", "test_title", "1234")
        self.small_book = Book("small_author", "small_title", "4321")
        self.empty_book = None
        self.test_user = User("tester", "tester123")
        self.other_user = User("other", "other123")
        self.user_repository.add_user(self.test_user)
        self.user_repository.add_user(self.other_user)
        self.user_id = self.user_repository.get_user(self.test_user)[0]
        self.other_id = self.user_repository.get_user(self.other_user)[0]

    def test_add_book_with_valid_params(self):
        self.assertTrue(self.book_repository.add_book(self.test_book, self.user_id))

    def test_add_book_with_invalid_params(self):
        self.assertFalse(self.book_repository.add_book(self.empty_book, self.user_id))

    def test_user_gets_all_books(self):
        self.book_repository.add_book(self.test_book, self.user_id)
        self.book_repository.add_book(self.small_book, self.user_id)
        books = self.book_repository.get_users_books(self.user_id)

        self.assertTrue(len(books), 2)

    def test_user_gets_does_not_get_others_books(self):
        self.book_repository.add_book(self.test_book, self.user_id)
        self.book_repository.add_book(self.small_book, self.other_id)
        books = self.book_repository.get_users_books(self.user_id)

        self.assertTrue(len(books), 1)
    
    def test_user_marks_book_finished_and_it_is(self):
        self.book_repository.add_book(self.test_book, self.user_id)
        
        books = self.book_repository.get_users_books(self.user_id)
        book_id = books[0].get_id()
        self.book_repository.mark_finished(book_id)
        
        books = self.book_repository.get_users_books(self.user_id)
        book = books[0]
        time_stamp = book.get_read()
        
        self.assertIsNotNone(time_stamp)
    
    def test_is_user_owner_of_book(self):
        self.book_repository.add_book(self.test_book, self.user_id)

        books = self.book_repository.get_users_books(self.user_id)
        book = books[0]
        
        result = self.book_repository.is_owner(self.user_id, book.get_id())
        
        self.assertTrue(result)
        
    def test_user_is_not_owner_of_book(self):
        self.book_repository.add_book(self.test_book, self.other_id)

        books = self.book_repository.get_users_books(self.other_id)
        book = books[0]
        
        result = self.book_repository.is_owner(self.user_id, book.get_id())
        
        self.assertFalse(result)
    
    def test_get_books_by_tag_returns_correct_amount(self):
        self.book_repository.add_book(self.test_book, self.user_id)
        self.tag_repository.add_tag("test", self.user_id)
        tags = self.tag_repository.get_tags(self.user_id)
        tag_id = tags[0].get_id()
        books = self.book_repository.get_users_books(self.user_id)
        book_id = books[0].get_id()
        self.book_repository.attach_tag(tag_id, book_id)
        self.book_repository.add_book(self.small_book, self.user_id)
        self.assertEqual(len(self.book_repository.get_books_by_tag(tag_id)), 1)

    def test_tags_by_book_returns_correct_amount(self):
        self.book_repository.add_book(self.test_book, self.user_id)
        self.tag_repository.add_tag("test", self.user_id)
        self.tag_repository.add_tag("testtwo", self.user_id)
        tags = self.tag_repository.get_tags(self.user_id)
        tag_id = tags[0].get_id()
        books = self.book_repository.get_users_books(self.user_id)
        book_id = books[0].get_id()
        self.book_repository.attach_tag(tag_id, book_id)
        self.assertEqual(len(self.book_repository.get_tags_by_book(book_id)), 1)

    def test_tag_attaches_succesfully(self):
        self.book_repository.add_book(self.test_book, self.user_id)
        self.tag_repository.add_tag("test", self.user_id)
        tags = self.tag_repository.get_tags(self.user_id)
        tag_id = tags[0].get_id()
        books = self.book_repository.get_users_books(self.user_id)
        book_id = books[0].get_id()
        current_tags = len(self.book_repository.get_tags_by_book(book_id))
        self.book_repository.attach_tag(tag_id, book_id)
        self.assertFalse(len(self.book_repository.get_tags_by_book(book_id)) == current_tags)

    def test_tag_removed_succesfully(self):
        self.book_repository.add_book(self.test_book, self.user_id)
        self.tag_repository.add_tag("test", self.user_id)
        tags = self.tag_repository.get_tags(self.user_id)
        tag_id = tags[0].get_id()
        books = self.book_repository.get_users_books(self.user_id)
        book_id = books[0].get_id()
        self.book_repository.attach_tag(tag_id, book_id)
        self.book_repository.remove_tag(tag_id, book_id)
        self.assertFalse(len(self.book_repository.get_tags_by_book(book_id)))

    def test_book_is_found_with_id(self):
        self.book_repository.add_book(self.test_book, self.user_id)
        books = books = self.book_repository.get_users_books(self.user_id)
        book_title = books[0].get_title()

        self.assertEqual(book_title, self.test_book.get_title())

    def test_book_is_updated(self):
        self.book_repository.add_book(self.test_book, self.user_id)
        books = self.book_repository.get_users_books(self.user_id)
        book_id = books[0].get_id()

        self.book_repository.update_book(
            author="new author", title="new title",
            isbn="1", description="new description", book_id=book_id
            )

        book = self.book_repository.get_book(book_id)

        self.assertEqual(book.get_author(), "new author")
        self.assertEqual(book.get_title(), "new title")
        self.assertEqual(book.get_isbn(), "1")
        self.assertEqual(book.get_description(), "new description")

    def test_deleting_removes_book(self):
        self.book_repository.add_book(self.test_book, self.user_id)
        self.book_repository.add_book(self.small_book, self.user_id)
        books = self.book_repository.get_users_books(self.user_id)
        book_id = books[0].get_id()
        self.book_repository.delete_book(book_id)
        self.assertFalse(
            len(books) == len(self.book_repository.get_users_books(self.user_id))
            )
