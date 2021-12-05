import unittest
from services.blog_service import BlogService
from entities.blog import Blog


class StubRepo:
    def __init__(self):
        self.blogs = []
        self.blog_id = 0

    def add_blog(self, blog, user_id):
        self.blogs.append((user_id, blog))
        self.blog_id += 1
        
        return True

    def get_users_blogs(self, user_id):
        return [blog for blog in self.blogs if blog[0] == user_id]    
    

class TestblogService(unittest.TestCase):
    def setUp(self):
        self.repo = StubRepo()
        self.service = BlogService(self.repo)
        self.test_blog = Blog("author", "title", "url", "a fine blog")
        self.user_id = 1
        self.other_user_id = 2
        self.service.new_blog(self.test_blog, self.user_id)
      
    def test_user_can_add_blog(self):
        a_blog = Blog("author2", "title2", "url2", "a fine blog")
        response = self.service.new_blog(a_blog, self.user_id)
        
        self.assertTrue(response)
    
    def test_user_can_get_list_of_their_blogs(self):
        blogs = self.service.get_my_blogs(self.user_id)
    
        self.assertEqual(len(blogs), 1)
        self.assertEqual(blogs[0][0], self.user_id)
    
    def test_user_only_gets_their_own_blogs(self):
        a_blog = Blog("another author2", "another tilte2", "some url", "a good read")
        self.service.new_blog(a_blog, self.other_user_id)
        blogs = self.service.get_my_blogs(self.user_id)
    
        self.assertEqual(len(blogs), 1)
        self.assertEqual(blogs[0][0], self.user_id)
