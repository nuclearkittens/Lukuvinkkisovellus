import unittest
from repositories.user_repository import UserRepository
from repositories.podcast_repository import PodcastRepository
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
    
