from django.shortcuts import render
from django.http import HttpResponse
from .forms import InputForm

def index(request):
    context = {}
    context['form'] = InputForm()

    return render(request, 'home.html', context)
