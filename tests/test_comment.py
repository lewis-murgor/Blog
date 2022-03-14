import unittest
from app.models import Comment,Blog,User
from app import db

class CommentTest(unittest.TestCase):
    """
    Test Class to test the behaviour of the Comment class
    """
    def setUp(self):
        self.user_James = User(username = "James",password = "potato",email = "james@ms.com")
        self.blog_legacy = Blog(title = "Legacy",text = "I am living to be more than just another boring eulogy")
        self.new_comment = Comment(comment = "This is a very beautiful blog.",user = self.user_James,blog = self.blog_legacy)

    def tearDown(self):
        Comment.query.delete()
        User.query.delete()
        Blog.query.delete()

    def test_check_instance_variables(self):
        self.assertEqual(self.new_comment.comment, "This is a very beautiful blog.")
        self.assertEqual(self.new_comment.user, self.user_James)
        self.assertEqual(self.new_comment.blog, self.blog_legacy)

    def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all()) > 0)

    def test_get_comments(self):
        self.new_comment.save_comment()
        got_comments = Comment.get_comments(40)
        self.assertTrue(len(got_comments) == 1)
