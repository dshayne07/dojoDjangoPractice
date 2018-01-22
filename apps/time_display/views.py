from django.shortcuts import render
from time import gmtime, strftime

def index(request):
    context = {
        "day": strftime("%b %d, %Y", gmtime()),
        "time": strftime("%I:%M %p", gmtime())
    }
    return render(request, "time_display/index.html", context)