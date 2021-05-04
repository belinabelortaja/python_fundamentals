from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from login_registration_app.models import *
import bcrypt
from django.core.exceptions import PermissionDenied

def index(request):
    if 'user_id' in request.session:
         return redirect('/wall')
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
        return redirect('/wall')

def wall(request):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'user': user,
        'messages': Message.objects.all(),
    }
    return render(request, 'wall.html', context)

def login(request):
    if request.method == "POST":
        errors = User.objects.login(request.POST)
        if len(errors) != 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        this_user = User.objects.filter(email=request.POST['email'])
        request.session['user_id'] = this_user[0].id
        return redirect('/wall')
    return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')

def post_message(request):
    user= User.objects.get(id= request.session['user_id'])
    messages= Message.objects.create(user=user, message= request.POST['message'])
    return redirect('/wall')
def post_comment(request, id):
    user= User.objects.get(id= request.session['user_id'])
    messages= Message.objects.get(id=id)
    comments= Comment.objects.create(message= messages, comment= request.POST['comment'], user=user)
    return redirect('/wall')

def destroy(request, id):
    destroy= Comment.objects.get(id=id)
    if destroy.user.id== request.session['user_id']:
        destroy.delete()
        return redirect('/wall')
    raise PermissionDenied('User do not have permission to delete this comment')