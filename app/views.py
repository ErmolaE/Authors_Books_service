from django.shortcuts import redirect, render
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


def authors(request): 

    authors = Author.objects.all()

    return render(request, 'authors.html', {"authors": authors})

def author(request, id): 
    try:
        a = Author.objects.get(id=id)
    except:
        raise Http404
    authors_books = Book.objects.filter(author = a)
    
    return render(request, 'author.html', {"author": a, "authors_books": authors_books})


def add_book(request): 

    if request.method == "POST": 
        form = AddBook(request.POST, request.FILES)

        if form.is_valid():
            book_ent = Book()
            book_ent.title = form.cleaned_data['title']
            book_ent.description = form.cleaned_data['description']
            book_ent.book_text = form.cleaned_data['book_text']
            book_ent.cover = form.cleaned_data['cover']
            book_ent.genre = form.cleaned_data['genre']
            book_ent.isbn = form.cleaned_data['isbn']

            book_ent.save()
            authors = form.cleaned_data['author']
            for author in authors:
                book_ent.author.add(author)

            return redirect('books')


    else: 
        form = AddBook()

    return render(request, 'add_book.html', {'form': form})


def add_author(request): 
    
    if request.method == "POST": 
        form = AddAuthor(request.POST, request.FILES)

        if form.is_valid():
            author_ent = Author()
            author_ent.first_name = form.cleaned_data['first_name']
            author_ent.last_name = form.cleaned_data['last_name']
            author_ent.biography = form.cleaned_data['biography']
            author_ent.photo = form.cleaned_data['photo']

            author_ent.save()

            return redirect('authors')


    else: 
        form = AddAuthor()

    return render(request, 'add_author.html', {'form': form})