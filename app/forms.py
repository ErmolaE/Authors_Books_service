from django import forms
from django.core.exceptions import ValidationError
from .models import Author, Book


class AddAuthor(forms.Form): pass


class AddBook(forms.Form): pass
