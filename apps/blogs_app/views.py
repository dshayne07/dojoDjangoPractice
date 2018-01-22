from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, "blogs_app/index.html")

def new(request):
    response = "placeholder to display a new form to create a new blog"
    return HttpResponse(response)

def create(request):
    return redirect('/')

def show(request, number=1):
    response = "placeholder to display blog "+number
    return HttpResponse(response)

def edit(request, number=1):
    response = "placeholder to edit blog "+number
    return HttpResponse(response)

def destroy(request):
    return redirect('/')