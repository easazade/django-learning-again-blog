from django.views import View
from django.http import HttpResponse


def home(request):
    return HttpResponse('home page')
