from django import forms
from .models import Author
from django.contrib.auth.models import User


class AddAuthor(forms.Form):
    """
    Form for adding a author.
    """

    first_name = forms.CharField(max_length=50, label='First name')
    last_name = forms.CharField(max_length=50, label='Last name')
    biography = forms.CharField(widget=forms.Textarea, label='Authors biography', required=False)
    photo = forms.ImageField(label='Authors photo', required=False)


class AddBook(forms.Form):
    """
    Form for adding a book.
    """

    title = forms.CharField(max_length=50, label='Books title')
    description = forms.CharField(widget=forms.Textarea, label='Description of the book', required=False)
    book_text = forms.FileField(label='Books upload')
    cover = forms.ImageField(label='Books cover', required=False)
    genre = forms.CharField(max_length=50, label='Books genre', required=False)
    isbn = forms.CharField(label='ISBN', required=False)
    author = forms.ModelMultipleChoiceField(queryset=Author.objects.all())


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']