from django.shortcuts import render, HttpResponse, redirect
from tv_show_app.models import *
def new(request):
    return render(request, "new.html")

def create(request):
    print(request.POST)
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
    show = Show.objects.get(id=id)

    show.title = request.POST['title']
    show.network = request.POST['network']
    show.release_date = request.POST['release_date']
    show.description = request.POST['description']
    show.save()
    return redirect ('/shows')

def destroy(request, id):
    del_show = Show.objects.get(id=id)
    del_show.delete()
    return redirect('/shows')
