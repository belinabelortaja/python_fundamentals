from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from favorite_book_app.models import *
from login_registration_app.models import *
import bcrypt
from django.core.exceptions import PermissionDenied

def books(request):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        'books': Book.objects.all(),
        'user': User.objects.get(id=request.session['user_id'])
        }
    return render(request, 'books.html', context)

def create(request):
    errors = Book.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/books')
    user= User.objects.get(id= request.session['user_id'])
    book= Book.objects.create(title=request.POST['title'], user=user)
    return redirect('/books')

def show(request,book_id):
    context={
        'books': Book.objects.all(),
        'book': Book.objects.get(id=book_id),
        'user': User.objects.get(id= request.session['user_id'])
    }
    return render(request, 'one_book.html', context)

def add_favorite(request, book_id):
    user = User.objects.get(id=request.session['user_id'])
    book = Book.objects.get(id=book_id)
    user.fav_books.add(book)
    return redirect("/books")

def un_favorite(request, book_id):
    user = User.objects.get(id=request.session['user_id'])
    book = Book.objects.get(id=book_id)
    user.fav_books.remove(book)
    return redirect('/books/show/'+str(book_id))


def update(request,book_id):
    book = Book.objects.get(id=book_id)
    book.description = request.POST['description']
    book.save()

    return redirect("/books/show/"+str(book_id))

def delete(request,book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return redirect('/books')
