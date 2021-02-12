from django.test import TestCase
from .models import Blog
# Create your tests here.

class BlogTestCase(TestCase):
    def testBlog(self):
        blog = Blog(title="My Title", description="Blurb", link="...")
        self.assertEqual(blog.title, "My Title")
        self.assertEqual(blog.description, "Blurb")
        self.assertEqual(blog.link, "...")
