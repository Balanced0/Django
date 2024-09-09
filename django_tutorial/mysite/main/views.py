from django.shortcuts import render
from django.http import HttpResponse

def index(response):
    return HttpResponse("Hello, World!")

def page2(response):
    return HttpResponse("This is page 2")
