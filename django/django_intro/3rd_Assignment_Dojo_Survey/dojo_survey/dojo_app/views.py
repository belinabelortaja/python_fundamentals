from django.shortcuts import render, redirect, HttpResponse
def index(request):
    return(request,'index.html')
def results(request):
    if request.method == 'POST':
        context = {
            'name': request.POST['name'],
            'gender': request.POST['gender'],
            'locations': request.POST['locations'],
            'system': request.POST['system'],
            'languages': request.POST['languages'],
            'comments': request.POST['comments']
        }
        return render(request, 'results.html', context)
    return render(request, 'results.html')
