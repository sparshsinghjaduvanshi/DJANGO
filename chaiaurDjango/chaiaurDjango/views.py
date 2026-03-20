from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello, World!. You are at the home page of ChaiaurDjango.")
    return render(request, 'website/index.html')


def about(request):
    return HttpResponse("This is the about page of ChaiaurDjango. about page")

def contact(request):
    return HttpResponse("This is the contact page of ChaiaurDjango. contact page")