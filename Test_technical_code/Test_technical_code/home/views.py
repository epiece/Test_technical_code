from django.shortcuts import render
from django.http import HttpResponse

def hometest(request):
    x = []
    return HttpResponse("This is input")
