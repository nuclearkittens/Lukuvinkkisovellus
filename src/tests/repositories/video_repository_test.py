import unittest
from repositories.user_repository import UserRepository
from repositories.video_repository import VideoRepository
from repositories.tag_repository import TagRepository
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
        self.tag_repository = TagRepository(db)
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
    
    def test_get_videos_by_tag_returns_correct_amount(self):
        self.video_repository.add_video(self.test_video, self.user_id)
        self.tag_repository.add_tag("test", self.user_id)
        tags = self.tag_repository.get_tags(self.user_id)
        tag_id = tags[0].get_id()
        videos = self.video_repository.get_users_videos(self.user_id)
        video_id = videos[0].get_id()
        self.video_repository.attach_tag(tag_id, video_id)
        self.video_repository.add_video(self.small_video, self.user_id)
        self.assertEqual(len(self.video_repository.get_videos_by_tag(tag_id)), 1)

    def test_tags_by_video_returns_correct_amount(self):
        self.video_repository.add_video(self.test_video, self.user_id)
        self.tag_repository.add_tag("test", self.user_id)
        self.tag_repository.add_tag("testtwo", self.user_id)
        tags = self.tag_repository.get_tags(self.user_id)
        tag_id = tags[0].get_id()
        videos = self.video_repository.get_users_videos(self.user_id)
        video_id = videos[0].get_id()
        self.video_repository.attach_tag(tag_id, video_id)
        self.assertEqual(len(self.video_repository.get_tags_by_video(video_id)), 1)

    def test_tag_attaches_succesfully(self):
        self.video_repository.add_video(self.test_video, self.user_id)
        self.tag_repository.add_tag("test", self.user_id)
        tags = self.tag_repository.get_tags(self.user_id)
        tag_id = tags[0].get_id()
        videos = self.video_repository.get_users_videos(self.user_id)
        video_id = videos[0].get_id()
        current_tags = len(self.video_repository.get_tags_by_video(video_id))
        self.video_repository.attach_tag(tag_id, video_id)
        self.assertFalse(len(self.video_repository.get_tags_by_video(video_id)) == current_tags)

    def test_tag_removed_succesfully(self):
        self.video_repository.add_video(self.test_video, self.user_id)
        self.tag_repository.add_tag("test", self.user_id)
        tags = self.tag_repository.get_tags(self.user_id)
        tag_id = tags[0].get_id()
        videos = self.video_repository.get_users_videos(self.user_id)
        video_id = videos[0].get_id()
        self.video_repository.attach_tag(tag_id, video_id)
        self.video_repository.remove_tag(tag_id, video_id)
        self.assertFalse(len(self.video_repository.get_tags_by_video(video_id)))

    def test_video_is_found_with_id(self):
        self.video_repository.add_video(self.test_video, self.user_id)
        videos = self.video_repository.get_users_videos(self.user_id)
        video_title = videos[0].get_title()

        self.assertEqual(video_title, self.test_video.get_title())

    def test_video_is_updated(self):
        self.video_repository.add_video(self.test_video, self.user_id)
        videos = self.video_repository.get_users_videos(self.user_id)
        video_id = videos[0].get_id()

        self.video_repository.update_video(
            title="new title", url="juu.tuubi", 
            description="new description", video_id=video_id
            )

        video = self.video_repository.get_video(video_id)

        self.assertEqual(video.get_title(), "new title")
        self.assertEqual(video.get_url(), "juu.tuubi")
        self.assertEqual(video.get_description(), "new description")

    def test_deleting_removes_video(self):
        self.video_repository.add_video(self.test_video, self.user_id)
        self.video_repository.add_video(self.small_video, self.user_id)
        videos = self.video_repository.get_users_videos(self.user_id)
        video_id = videos[0].get_id()
        self.video_repository.delete_video(video_id)
        self.assertFalse(
            len(videos) == len(self.video_repository.get_users_videos(self.user_id))
            )
