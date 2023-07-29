from django.db import models

# Create your models here.

class Author(models.Model):
    """
    Model representing an author.
    """

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    biography = models.TextField(blank=True)
    photo = models.ImageField(upload_to='upload', blank=True, default='app/img/not_avalaible.png')

    def __str__(self) -> str:
        """
        String for representing the Model object.
        """
        return f"{self.last_name}, {self.first_name}"

class Book(models.Model):
    """
    Model representing a book.
    """

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, help_text="Enter a brief description of the book")
    image = models.ImageField(upload_to='upload', blank=True, default='app/img/not_avalaible.png')
    genre = models.CharField(max_length=50)
    author = models.ManyToManyField(Author)   # ManyToManyField used because author can have many books. Books can have many authors.

    def display_author(self):
        """
        Creates a string for the Author.
        """
        return ', '.join([ f"{author.last_name} {author.first_name}" for author in self.author.all()[:3] ])
    
    display_author.short_description = 'Author'


    def __str__(self) -> str:
        """
        String for representing the Model object.
        """
        return self.title