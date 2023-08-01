from django import forms
from .models import Author


class AddAuthor(forms.Form): 

    first_name = forms.CharField(max_length=50, label='First name')
    last_name = forms.CharField(max_length=50, label='Last name')
    biography = forms.CharField(widget=forms.Textarea, label='Authors biography', required=False)
    photo = forms.ImageField(label='Authors photo', required=False)


class AddBook(forms.Form): 

    title = forms.CharField(max_length=50, label='Books title')
    description = forms.CharField(widget=forms.Textarea, label='Description of the book', required=False)
    book_text = forms.FileField(label='Books upload')
    cover = forms.ImageField(label='Books cover', required=False)
    genre = forms.CharField(max_length=50, label='Books genre', required=False)
    isbn = forms.CharField(label='ISBN', required=False)
    author = forms.ModelMultipleChoiceField(queryset = Author.objects.all())
    
