import unittest
from repositories.user_repository import UserRepository
from repositories.video_repository import VideoRepository
from app import app
from db import db
from entities.video import Video
from entities.user import User
from tests.database_test_helper import Database_test_helper as dth


class TestvideoRepository(unittest.TestCase):
    def setUp(self):
        empty_database = dth(db).delete()
        self.video_repository = VideoRepository(db)
        self.user_repository = UserRepository(db)
        self.test_video = Video("test_title", "www.oneurl.com", "funny catvideo")
        self.small_video = Video("small_title", "www.anotherurl.com", "even funnier dogvideo")
        self.empty_video = None
        self.test_user = User("tester", "tester123")
        self.other_user = User("other", "other123")
        self.user_repository.add_user(self.test_user)
        self.user_repository.add_user(self.other_user)
        self.user_id = self.user_repository.get_user(self.test_user)[0]
        self.other_id = self.user_repository.get_user(self.other_user)[0]

    def test_add_video_with_valid_params(self):
        self.assertTrue(self.video_repository.add_video(self.test_video, self.user_id))

    def test_add_video_with_invalid_params(self):
        self.assertFalse(self.video_repository.add_video(self.empty_video, self.user_id))

    def test_user_gets_all_videos(self):
        self.video_repository.add_video(self.test_video, self.user_id)
        self.video_repository.add_video(self.small_video, self.user_id)
        videos = self.video_repository.get_users_videos(self.user_id)

        self.assertTrue(len(videos), 2)

    def test_user_gets_does_not_get_others_videos(self):
        self.video_repository.add_video(self.test_video, self.user_id)
        self.video_repository.add_video(self.small_video, self.other_id)
        videos = self.video_repository.get_users_videos(self.user_id)

        self.assertTrue(len(videos), 1)
    
    def test_user_marks_video_finished_and_it_is(self):
        self.video_repository.add_video(self.test_video, self.user_id)
        
        videos = self.video_repository.get_users_videos(self.user_id)
        video_id = videos[0].get_id()
        self.video_repository.mark_finished(video_id)
        
        videos = self.video_repository.get_users_videos(self.user_id)
        print(videos)
        video = videos[0]
        time_stamp = video.get_read()
        
        self.assertIsNotNone(time_stamp)
    
    def test_is_user_owner_of_video(self):
        self.video_repository.add_video(self.test_video, self.user_id)

        videos = self.video_repository.get_users_videos(self.user_id)
        video = videos[0]
        
        result = self.video_repository.is_owner(self.user_id, video.get_id())
        
        self.assertTrue(result)
        
    def test_user_is_not_owner_of_video(self):
        self.video_repository.add_video(self.test_video, self.other_id)

        videos = self.video_repository.get_users_videos(self.other_id)
        video = videos[0]
        
        result = self.video_repository.is_owner(self.user_id, video.get_id())
        
        self.assertFalse(result)
    
