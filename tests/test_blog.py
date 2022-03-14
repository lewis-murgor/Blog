import unittest
from app.models import Blog


class TestBlog(unittest.TestCase):
    def setUp(self):
        self.blog = Blog(comment='Beautiful!')
    
    def tearDown(self):
        Blog.query.delete()

    def test_save_blog(self):
        self.new_comment.save_blogs()
        self.assertTrue(len(Blog.query.all())>0)