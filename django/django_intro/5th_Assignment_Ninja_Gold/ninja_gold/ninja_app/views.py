from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
import pytz
from pytz import timezone
from random import randrange
def index(request):
    if 'gold_amount' not in request.session:
        request.session['gold_amount'] = 0
        request.session['activities'] = []
    context={
        'gold':request.session['gold_amount']
    }
    return render(request, 'index.html', context)
def reset(request):
    request.session.clear()
    return redirect('/')

def process_money(request):
    if request.method == 'POST':
        gold = request.session['gold_amount']
        activity = request.session['activities']
        location = request.POST['location']
    if location == 'farm':
        my_gold = randrange(10, 20)
    elif location == 'cave':
        my_gold = randrange(5, 10)
    elif location == 'house':
        my_gold = randrange(2, 5)
    else:
        my_gold = randrange(-50, 50)
    date_format='%m/%d/%Y %H:%M:%S %Z'
    date = datetime.now(tz=pytz.utc)
    date = date.astimezone(timezone('Europe/Paris'))
    myTime = date.strftime(date_format)
    
    request.session['gold_amount']+= my_gold
    if my_gold >= 0:
        activity= (f'Earned {my_gold} from the {location}...({myTime})')
        color= 'green'
    else:
        activity= (f'Entered a  {location} and lost {my_gold} golds... Ouch...({myTime})')
        color='red'
    
    request.session['activities'].append({'color': color, 'activity':activity})
    return redirect('/')






