from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from courses_app.models import *
def index(request):
    context={
        'course' : Course.objects.all(),
    }
    return render(request,"index.html", context)
def new(request):
    context={
        "courses": Course.objects.all()
    }

    return render(request,"index.html", context)
def show(request, id):
    context={
        'course' : Course.objects.all(),
    }
    return render(request,"index.html", context)
def create(request):
    errors = Course.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/courses/new')
    else:
        description = Description.objects.create(description = request.POST['description'])
        course = Course.objects.create(name = request.POST['name'], description_id = description.id)

        return redirect('/courses/new')
def destroy(request,id):
    context={
        'course': Course.objects.get(id=id)
    }

    return render(request,"delete.html", context)

def delete(request,id):
    if request.method == 'POST':
        del_course = Course.objects.get(id=id)
        del_course.delete()

    return redirect('/courses/new')

def add_comment(request,id):
    context={
        'course': Course.objects.get(id=id)
    }

    return render(request,"comments.html", context)

def view_comment(request,id):
     if request.method == 'POST':
         comment = Comment.objects.create(comment=request.POST['comment'], course=Course.objects.get(id=id))


     return redirect(f"/courses/{id}/comment")