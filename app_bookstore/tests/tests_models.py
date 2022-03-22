from django.test import TestCase
from django.utils import timezone
from django.contrib.auth import get_user_model
from ..models import Author, Book


USER = get_user_model()


class TestAuthor(TestCase):
    def setUp(self):
        user = USER.objects.create_user(
            'admin@email.com',
            '1qa2ws3ed'
        )

        test_author = Author.objects.create(
            first_name = "Michael",
            last_name = "Connelly",
            gender = "Male",
            born = "1956-07-21",
            died = None,
            passed = False,
            user_created = user,
            date_created = timezone.now(),
            date_updated = timezone.now()
        )
        self.assertEqual(str(test_author), "Michael Connelly")

    def test_author_exists(self):
        authors = Author.objects.all().count()
        self.assertEqual(authors, 1)
        self.assertNotEqual(authors, 0)


class TestBook(TestCase):
    def setUp(self):
        user = USER.objects.create_user(
            'admin@email.com',
            '1qa2ws3ed'
        )

        author = Author.objects.create(
            first_name = "Micheal",
            last_name = "Connelly",
            gender = "Male",
            born = "1956-07-21",
            died = None,
            passed = False,
            user_created = user,
            date_created = timezone.now(),
            date_updated = timezone.now()
        )

        test_book = Book.objects.create(
            author = author,
            title = "Schwarzes Echo",
            genre = "Crime",
            published = "1992-01-21",
            user_created = user,
            date_created = timezone.now(),
            date_updated = timezone.now()
        )
        self.assertEqual(str(test_book), "Schwarzes Echo")

    def test_book_exists(self):
        books = Book.objects.all().count()
        self.assertEqual(books, 1)
        self.assertNotEqual(books, 0)