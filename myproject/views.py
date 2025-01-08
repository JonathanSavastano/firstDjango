# from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    # return HttpResponse("Hello, World! Here we fucking go.")
    return render(request, 'home.html')

def about(request):
    # return HttpResponse("My About page.")
    return render(request, 'about.html')