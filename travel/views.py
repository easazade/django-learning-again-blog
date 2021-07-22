from django.shortcuts import render, redirect
from travel.models import Destination

# Create your views here.


def travelHome(request):
    return redirect('main')


def main(request):
    dest1 = Destination()
    dest1.id = 0
    dest1.name = 'rasht'
    dest1.distance = 150

    dest2 = Destination()
    dest2.id = 0
    dest2.name = 'tabriz'
    dest2.distance = 500

    dest3 = Destination()
    dest3.id = 0
    dest3.name = 'tehran'
    dest3.distance = 200

    destinations = [dest1, dest2, dest3]
    return render(request, 'travel-main.html', {'destinations': destinations})
