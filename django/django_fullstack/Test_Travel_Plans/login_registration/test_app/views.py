from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from login_registration_app.models import *
from test_app.models import *
import bcrypt


def travel_index(request):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    other_users =  User.objects.exclude(id= request.session['user_id']).difference(User.objects.get(id = request.session['user_id']).travels.all())
    context = {
        'user' : user,
        'all_users': User.objects.all(),
        'other_users': other_users,
        'travels': Travel.objects.all()
    }
    return render(request, 'travels.html', context)
    
def join_travel(request, id):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    joined_travel = User.objects.get(id=id)
    user.friends.add(joined_travel)
    return redirect("/travels")

def create_travel(request):
    errors = Travel.objects.basic_validator(request.POST)
    time_errors= Travel.objects.clean()
    if len(errors) > 0 and len(time_errors)>0:
        for key, value in errors.items() and time_errors.items():
            messages.error(request, value)
        return redirect('/travels/new')
    user= User.objects.get(id= request.session['user_id'])
    travel= Travel.objects.create(destination=request.POST['destination'], plan=request.POST['plan'],startdate=request.POST['startdate'], end_date=request.POST['end_date'], user=user)
    return redirect('/travels')


def show_travel(request, travel_id):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        'user' : User.objects.get(id= request.session['user_id']),
        'travels': Travel.objects.all(),
        'travel': Travel.objects.get(id=travel_id),
    
    }
    return render(request, 'destinations.html', context)

def new_travel(request):
    return render(request, "add_travel.html")
