from django.shortcuts import render, HttpResponse, render, redirect
from .models import Users
def index(request):
    context = {
    	"all_the_users": Users.objects.all()
    }
    return render(request, "index.html", context)
def result(request):
    if request.method == 'POST':
        Users.objects.create(firstname=request.POST['firstname'], lastname=request.POST['lastname'],email=request.POST['email'],age=request.POST['age'])
    return redirect('/')
