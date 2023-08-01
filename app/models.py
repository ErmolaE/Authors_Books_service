from django.db import models

# Create your models here.


class Author(models.Model):
    """
    Model representing an author.
    """

    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    biography = models.TextField(blank=True)
    photo = models.ImageField(upload_to='authors/', blank=True, default='app/img/not_avalaible.png')

    def __str__(self) -> str:
        """
        String for representing the Model object.
        """
        return f"{self.last_name}, {self.first_name}"


class Book(models.Model):
    """
    Model representing a book.
    """

    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=True, help_text="Enter a brief description of the book")
    book_text = models.FileField(blank=False, upload_to='books/')
    cover = models.ImageField(upload_to='covers/', blank=True, default='app/img/not_avalaible.png')
    genre = models.CharField(max_length=50, blank=True)
    isbn = models.CharField('ISBN', max_length=13, blank=True, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    author = models.ManyToManyField(Author)
    # ManyToManyField used because author can have many books. Books can have many authors.

    def display_author(self):
        """
        Creates a string for the Author.
        """
        return ', '.join([f"{author.last_name} {author.first_name}" for author in self.author.all()[:3]])

    def list_authors(self):
        """
        Create a list of authors.
        """
        return self.author.all()

    def __str__(self) -> str:
        """
        String for representing the Model object.
        """
        return self.title
