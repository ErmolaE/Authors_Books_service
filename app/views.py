from django.shortcuts import render
from django.http import Http404
from app.forms import AddAuthor, AddBook
from .models import Author, Book

# Create your views here.

def books(request):

    books = Book.objects.all()
    viewed_books = request.session.get("viewed_books", {})

    return render(request, 'books.html', {"books": books, "viewed_books": viewed_books})


def book(request, id):
    try:
        b = Book.objects.get(id=id)
    except:
        raise Http404

    viewed_books = request.session.get("viewed_books", {})
    viewed_books[b.id] = b.id
    request.session["viewed_books"] = viewed_books

    return render(request, 'book.html', {"book": b, "viewed_books": viewed_books})


def authors(request): pass


def author(request, id): pass


def add_book(request): pass


def add_author(request): pass