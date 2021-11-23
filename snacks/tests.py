from django.test import TestCase
from django.contrib.auth.models import User

from .models import Snack


class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a user
        testuser1 = User.objects.create_user(username="testuser1", password="abc123")
        testuser1.save()

        # Create a blog post
        test_post = Snack.objects.create(
            purchaser=testuser1, title="Blog title", description="Body content..."
        )
        test_post.save()

    def test_blog_content(self):
        post = Snack.objects.get(id=1)
        expected_purchaser = f"{post.purchaser}"
        expected_title = f"{post.title}"
        expected_description = f"{post.description}"
        self.assertEqual(expected_purchaser, "testuser1")
        self.assertEqual(expected_title, "Blog title")
        self.assertEqual(expected_description, "Body content...")
#========================================
from django.contrib.auth import get_user_model
class BlogTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser1', password='pass')
        testuser1.save()
        test_post = Snack.objects.create(title='Test Post', description='Test Post Body', purchaser=testuser1)
        test_post.save()
    
    def test_blog_content(self):
        post = Snack.objects.get(id=1)
        expected_purchaser = f'{post.purchaser}'
        expected_title = f'{post.title}'
        expected_description = f'{post.description}'
        self.assertEqual(expected_purchaser, 'testuser1')
        self.assertEqual(expected_title, 'Test Post')
        self.assertEqual(expected_description, 'Test Post Body')