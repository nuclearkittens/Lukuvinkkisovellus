import unittest
from repositories.user_repository import UserRepository
from repositories.tag_repository import TagRepository
from app import app
from db import db
from entities.user import User
from tests.database_test_helper import Database_test_helper as dth


class TestpodcastRepository(unittest.TestCase):
    def setUp(self):
        pass
        self.dth = dth(db)
        self.dth.delete()
        self.tag_repository = TagRepository(db)
        self.user_repository = UserRepository(db)
        self.test_user = User("tester", "tester123")
        self.other_user = User("other", "other123")
        self.user_repository.add_user(self.test_user)
        self.user_repository.add_user(self.other_user)
        self.test_user_id = self.user_repository.get_user(self.test_user)[0]
        self.other_user_id = self.user_repository.get_user(self.other_user)[0]
    
    def test_get_tags_returns_correct_list_of_tags(self):
        self.tag_repository.add_tag("test", self.test_user_id)
        self.tag_repository.add_tag("testtwo", self.test_user_id)
        self.tag_repository.add_tag("wrong", self.other_user_id)
        self.assertEqual(len(self.tag_repository.get_tags(self.test_user_id)), 2)

    def test_add_tag_increases_amount_of_tags(self):
        self.tag_repository.add_tag("test", self.test_user_id)
        self.assertEqual(len(self.tag_repository.get_tags(self.test_user_id)), 1)

    def test_edit_tag_changes_content(self):
        self.tag_repository.add_tag("test", self.test_user_id)
        tags = self.tag_repository.get_tags(self.test_user_id)
        tag_id = tags[0].get_id()
        self.tag_repository.edit_tag(tag_id, "edited")
        tags = self.tag_repository.get_tags(self.test_user_id)
        self.assertEqual(tags[0].get_name(), "edited")

    def test_delete_tag_decreases_amount_of_tags(self):
        self.tag_repository.add_tag("test", self.test_user_id)
        self.tag_repository.add_tag("testtwo", self.test_user_id)
        tags = self.tag_repository.get_tags(self.test_user_id)
        tag_id = tags[0].get_id()
        self.tag_repository.delete_tag(tag_id)
        self.assertEqual(len(self.tag_repository.get_tags(self.test_user_id)), 1)