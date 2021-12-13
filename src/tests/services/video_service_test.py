import unittest
from services.video_service import VideoService

class StubRepo:
    def __init__(self):
        pass

class TestVideoService(unittest.TestCase):
    def setUp(self):
        self.repo = StubRepo()
        self.service = VideoService(self.repo)

    def test_url_returns_title(self):
        url = "https://www.youtube.com/watch?v=DRnMwtdegII"
        title = "Super Donkey Kong Shake"
        self.assertEqual(self.service.get_title_from_url(url), title)
