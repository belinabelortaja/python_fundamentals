from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from login_registration_app.models import *
import bcrypt

def index(request):
    if 'user_id' in request.session:
         return redirect('/friends')
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
        return redirect('/friends')

def login(request):
    if request.method == "POST":
        errors = User.objects.login(request.POST)
        if len(errors) != 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        this_user = User.objects.filter(email=request.POST['email'])
        request.session['user_id'] = this_user[0].id
        return redirect('/friends')
    return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')