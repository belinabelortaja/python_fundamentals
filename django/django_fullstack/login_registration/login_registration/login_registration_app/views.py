from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from login_registration_app.models import *
import bcrypt

def index(request):
    if 'user_id' in request.session:
         return redirect('/success')
    context = {
    	"users": User.objects.all()
    }
    return render(request, "index.html", context)

def registration(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        hash1 = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        user= User.objects.create(firstname=request.POST['firstname'], lastname= request.POST['lastname'], email= request.POST['email'], birthdate= request.POST['birthdate'], password=hash1)
        request.session['user_id']=user.id
        return redirect('/success')

def success(request):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'user': user
    }
    return render(request, 'success.html', context)

def login(request):
    if request.method == "POST":
        errors = User.objects.login(request.POST)
        if len(errors) != 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        this_user = User.objects.filter(email=request.POST['email'])
        request.session['user_id'] = this_user[0].id
        return redirect('/success')
    return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')