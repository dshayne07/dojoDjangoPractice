from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def index(request):
    context = {
        'unique_id':get_random_string(length=32)
    }
    if "counter" not in request.session:
        request.session['counter'] = 1
    else:
        request.session['counter']+=1
    return render(request, "random_word/index.html", context)

def reset(request):
    request.session['counter'] = 0
    return redirect('/random_word/')