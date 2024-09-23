from django.shortcuts import render

from random import randint

# Create your views here.

def index(request):
    lista = []
    for x in range(10):
        lista.append(randint(0, 100))
    return render(request, 'index.html', context={'elementy': lista})