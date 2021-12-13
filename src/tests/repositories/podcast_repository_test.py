import unittest
from repositories.user_repository import UserRepository
from repositories.podcast_repository import PodcastRepository
from repositories.tag_repository import TagRepository
from app import app
from db import db
from entities.podcast import Podcast
from entities.user import User
from tests.database_test_helper import Database_test_helper as dth


class TestpodcastRepository(unittest.TestCase):
    def setUp(self):
        empty_database = dth(db).delete()
        self.podcast_repository = PodcastRepository(db)
        self.user_repository = UserRepository(db)
        self.tag_repository = TagRepository(db)
        self.test_podcast = Podcast("test_title", "test_episode", "www.oneurl.com")
        self.small_podcast = Podcast("small_title", "small_episode", "www.anotherurl.com")
        self.empty_podcast = None
        self.test_user = User("tester", "tester123")
        self.other_user = User("other", "other123")
        self.user_repository.add_user(self.test_user)
        self.user_repository.add_user(self.other_user)
        self.user_id = self.user_repository.get_user(self.test_user)[0]
        self.other_id = self.user_repository.get_user(self.other_user)[0]

    def test_add_podcast_with_valid_params(self):
        self.assertTrue(self.podcast_repository.add_podcast(self.test_podcast, self.user_id))

    def test_add_podcast_with_invalid_params(self):
        self.assertFalse(self.podcast_repository.add_podcast(self.empty_podcast, self.user_id))

    def test_user_gets_all_podcasts(self):
        self.podcast_repository.add_podcast(self.test_podcast, self.user_id)
        self.podcast_repository.add_podcast(self.small_podcast, self.user_id)
        podcasts = self.podcast_repository.get_users_podcasts(self.user_id)

        self.assertTrue(len(podcasts), 2)

    def test_user_gets_does_not_get_others_podcasts(self):
        self.podcast_repository.add_podcast(self.test_podcast, self.user_id)
        self.podcast_repository.add_podcast(self.small_podcast, self.other_id)
        podcasts = self.podcast_repository.get_users_podcasts(self.user_id)

        self.assertTrue(len(podcasts), 1)
    
    def test_user_marks_podcast_finished_and_it_is(self):
        self.podcast_repository.add_podcast(self.test_podcast, self.user_id)
        
        podcasts = self.podcast_repository.get_users_podcasts(self.user_id)
        podcast_id = podcasts[0].get_id()
        self.podcast_repository.mark_finished(podcast_id)
        
        podcasts = self.podcast_repository.get_users_podcasts(self.user_id)
        podcast = podcasts[0]
        time_stamp = podcast.get_read()
        
        self.assertIsNotNone(time_stamp)
    
    def test_is_user_owner_of_podcast(self):
        self.podcast_repository.add_podcast(self.test_podcast, self.user_id)

        podcasts = self.podcast_repository.get_users_podcasts(self.user_id)
        podcast = podcasts[0]
        
        result = self.podcast_repository.is_owner(self.user_id, podcast.get_id())
        
        self.assertTrue(result)
        
    def test_user_is_not_owner_of_podcast(self):
        self.podcast_repository.add_podcast(self.test_podcast, self.other_id)

        podcasts = self.podcast_repository.get_users_podcasts(self.other_id)
        podcast = podcasts[0]
        
        result = self.podcast_repository.is_owner(self.user_id, podcast.get_id())
        
        self.assertFalse(result)
    
    def test_get_podcasts_by_tag_returns_correct_amount(self):
        self.podcast_repository.add_podcast(self.test_podcast, self.user_id)
        self.tag_repository.add_tag("test", self.user_id)
        tags = self.tag_repository.get_tags(self.user_id)
        tag_id = tags[0].get_id()
        podcasts = self.podcast_repository.get_users_podcasts(self.user_id)
        podcast_id = podcasts[0].get_id()
        self.podcast_repository.attach_tag(tag_id, podcast_id)
        self.podcast_repository.add_podcast(self.small_podcast, self.user_id)
        self.assertEqual(len(self.podcast_repository.get_podcasts_by_tag(tag_id)), 1)

    def test_tags_by_podcast_returns_correct_amount(self):
        self.podcast_repository.add_podcast(self.test_podcast, self.user_id)
        self.tag_repository.add_tag("test", self.user_id)
        self.tag_repository.add_tag("testtwo", self.user_id)
        tags = self.tag_repository.get_tags(self.user_id)
        tag_id = tags[0].get_id()
        podcasts = self.podcast_repository.get_users_podcasts(self.user_id)
        podcast_id = podcasts[0].get_id()
        self.podcast_repository.attach_tag(tag_id, podcast_id)
        self.assertEqual(len(self.podcast_repository.get_tags_by_podcast(podcast_id)), 1)

    def test_tag_attaches_succesfully(self):
        self.podcast_repository.add_podcast(self.test_podcast, self.user_id)
        self.tag_repository.add_tag("test", self.user_id)
        tags = self.tag_repository.get_tags(self.user_id)
        tag_id = tags[0].get_id()
        podcasts = self.podcast_repository.get_users_podcasts(self.user_id)
        podcast_id = podcasts[0].get_id()
        current_tags = len(self.podcast_repository.get_tags_by_podcast(podcast_id))
        self.podcast_repository.attach_tag(tag_id, podcast_id)
        self.assertFalse(len(self.podcast_repository.get_tags_by_podcast(podcast_id)) == current_tags)

    def test_tag_removed_succesfully(self):
        self.podcast_repository.add_podcast(self.test_podcast, self.user_id)
        self.tag_repository.add_tag("test", self.user_id)
        tags = self.tag_repository.get_tags(self.user_id)
        tag_id = tags[0].get_id()
        podcasts = self.podcast_repository.get_users_podcasts(self.user_id)
        podcast_id = podcasts[0].get_id()
        self.podcast_repository.attach_tag(tag_id, podcast_id)
        self.podcast_repository.remove_tag(tag_id, podcast_id)
        self.assertFalse(len(self.podcast_repository.get_tags_by_podcast(podcast_id)))
        
    
    def test_podcast_is_found_with_id(self):
        self.podcast_repository.add_podcast(self.test_podcast, self.user_id)
        podcasts = podcasts = self.podcast_repository.get_users_podcasts(self.user_id)
        podcast_title = podcasts[0].get_title()

        self.assertEqual(podcast_title, self.test_podcast.get_title())

    def test_podcast_is_updated(self):
        self.podcast_repository.add_podcast(self.test_podcast, self.user_id)
        podcasts = self.podcast_repository.get_users_podcasts(self.user_id)
        podcast_id = podcasts[0].get_id()

        self.podcast_repository.update_podcast(
            title="new title", episode="1", 
            description="new description", podcast_id=podcast_id
            )

        podcast = self.podcast_repository.get_podcast(podcast_id)

        self.assertEqual(podcast.get_title(), "new title")
        self.assertEqual(podcast.get_episode(), "1")
        self.assertEqual(podcast.get_description(), "new description")

    def test_deleting_removes_podcast(self):
        self.podcast_repository.add_podcast(self.test_podcast, self.user_id)
        self.podcast_repository.add_podcast(self.small_podcast, self.user_id)
        podcasts = self.podcast_repository.get_users_podcasts(self.user_id)
        podcast_id = podcasts[0].get_id()
        self.podcast_repository.delete_podcast(podcast_id)
        self.assertFalse(
            len(podcasts) == len(self.podcast_repository.get_users_podcasts(self.user_id))
            )
