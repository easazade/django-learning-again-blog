from django.views import View
from django.http import HttpResponse
from django.shortcuts import render


# def home(request):
#     return HttpResponse('home page')

def home(request):
    return render(request, 'index.html')
