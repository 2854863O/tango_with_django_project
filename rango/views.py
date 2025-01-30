from django.shortcuts import render
from django.http import HttpResponse

def index (request):
    about_link = "<a href='/rango/about'>About</a>"
    return HttpResponse("Rango says hey there partner! Here is a link to the about page - " +about_link)

def about (request):
    rango_link = "<a href='/rango/'>Rango</a>"
    return HttpResponse('Rango says here is the about page.'+ rango_link)