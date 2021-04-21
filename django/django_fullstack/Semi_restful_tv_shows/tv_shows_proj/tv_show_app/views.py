from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from tv_show_app.models import *
def new(request):
    return render(request, "new.html")

def create(request):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    show= Show.objects.create(title=request.POST['title'], network=request.POST['network'],release_date=request.POST['release_date'], description=request.POST['description'])
    return redirect('/shows/' + str(show.id))

def show(request, id):
    context={
        "show" : Show.objects.get(id=id)
    }
    return render(request, 'show.html', context)

def index(request):
    context={
        "shows" : Show.objects.all()
    }
    return render(request, 'index.html', context)

def edit(request, id):
    context={
        "show" : Show.objects.get(id=id)
    }
    return render(request, 'edit.html', context)

def update(request, id):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/'+str(id)+'/edit')
    else:
        show = Show.objects.get(id=id)
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.release_date = request.POST['release_date']
        show.description = request.POST['description']
        show.save()
        messages.success(request, "Blog successfully updated")
        return redirect ('/shows')

def destroy(request, id):
    del_show = Show.objects.get(id=id)
    del_show.delete()
    return redirect('/shows')