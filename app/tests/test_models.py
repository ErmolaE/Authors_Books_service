from django.test import TestCase
from app.models import Author, Book

class AuthorModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Author.objects.create(first_name='Big', last_name='Bob')

    def test_first_name_label(self):
        author=Author.objects.get(id=1)
        field_label = author._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label,'first name')

    def test_last_name_label(self):
        author=Author.objects.get(id=1)
        field_label = author._meta.get_field('last_name').verbose_name
        self.assertEquals(field_label,'last name')
    
    def test_first_name_max_length(self):
        author=Author.objects.get(id=1)
        max_length = author._meta.get_field('first_name').max_length
        self.assertEquals(max_length,50)

    def test_last_name_max_length(self):
        author=Author.objects.get(id=1)
        max_length = author._meta.get_field('last_name').max_length
        self.assertEquals(max_length,50)

    def test_object_name_is_last_name_comma_first_name(self):
        author=Author.objects.get(id=1)
        expected_object_name = f"{author.last_name}, {author.first_name}"
        self.assertEquals(expected_object_name,str(author))


class BookModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Book.objects.create(title='Test_book', genre='Test_genre', isbn='1234567890123')

    def test_title_label(self):
        book=Book.objects.get(id=1)
        field_label = book._meta.get_field('title').verbose_name
        self.assertEquals(field_label,'title')

    def test_genre_label(self):
        book=Book.objects.get(id=1)
        field_label = book._meta.get_field('genre').verbose_name
        self.assertEquals(field_label,'genre')
    
    def test_isbn_length(self):
        book=Book.objects.get(id=1)
        max_length = book._meta.get_field('isbn').max_length
        self.assertEquals(max_length,13)

    def test_object_name_is_title(self):
        book=Book.objects.get(id=1)
        expected_object_name = book.title
        self.assertEquals(expected_object_name,str(book))
