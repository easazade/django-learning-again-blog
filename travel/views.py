from django.shortcuts import render, redirect
from travel.models import Destination

# Create your views here.


def travelHome(request):
    return redirect('main')


def main(request):
    destinations = Destination.objects.all()
    return render(request, 'travel-main.html', {'destinations': destinations})
