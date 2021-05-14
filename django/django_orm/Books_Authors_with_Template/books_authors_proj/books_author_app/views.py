from django.shortcuts import render, redirect, HttpResponse
from books_author_app.models import *

def index(request):
    if request.method == "POST":
        book = Book.objects.create(title=request.POST['title'], description=request.POST['description'])
        return redirect("/")
    context={
        "books":Book.objects.all(),
    }
    return render(request, "index.html", context)

def authors(request):
    if request.method == "POST":
        authors = Author.objects.create(firstname=request.POST['firstname'], lastname=request.POST['lastname'], notes=request.POST['notes'])
        return redirect("/authors")
    context={
        "authors":Author.objects.all(),
    }
    return render(request, "authors.html", context)

def book(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        author = Author.objects.get(id=request.POST['author_id'])
        book.authors.add(author)
        return redirect('/book/' + str(book.id))
    context={
        "book": book,
        "authors": Author.objects.all(),
    }
    print(Author.objects.all())
    return render(request, "book.html", context)

def author2(request, id):
    author2 = Author.objects.get(id=id)
    if request.method == 'POST':
        book2 = Book.objects.get(id=request.POST['book_id'])
        author2.books.add(book2)
        return redirect('/author/' + str(author2.id))
    context={
        "author2": author2,
        "books": Book.objects.all(),
    }
    print(Book.objects.all())
    return render(request, "author_2.html", context)
