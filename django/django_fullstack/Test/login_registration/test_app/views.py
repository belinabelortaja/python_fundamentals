from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from login_registration_app.models import *
import bcrypt

def friends(request):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    other_users =  User.objects.exclude(id= request.session['user_id'])
    added_user = User.objects.exclude(id= request.user.id)
    context = {
        'user' : user,
        'all_users': User.objects.all(),
        'other_users': other_users,
        'added_user': added_user
    }
    return render(request, 'friends.html', context)
def add_friend(request, id):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    added_user = User.objects.get(id=id)
    user.friends.add(added_user)
    return redirect("/friends")

def view_profile(request, id):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        'user' : User.objects.get(id=id),
    
    }
    return render(request, 'profile.html', context)

def remove_friend(request, id):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    deleted_user = User.objects.get(id=id)
    user.friends.remove(deleted_user)
    return redirect("/friends")
