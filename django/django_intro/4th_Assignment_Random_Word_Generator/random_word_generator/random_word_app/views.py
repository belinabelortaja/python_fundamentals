from django.shortcuts import render, redirect, HttpResponse
from django.utils.crypto import get_random_string
def index(request):
    if 'counter' not in request.session:
        request.session['counter']=0
    else:
        request.session['counter']+=1
    context= {
        'rand_word': get_random_string(length=14),
        'counter': request.session['counter']
    }
    return render(request, 'index.html', context)

def generate(request):
    if request.method == 'POST':
        return redirect('/')
def reset(request):
    if request.method == 'POST':
        request.session['counter']=0
        return redirect('/')
