from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# def index(request):
#     return HttpResponse("poll app index page")


# def index(request):
#     return render(request, 'home.html')


def index(request):
    return render(request, 'home.html', {'name': 'alireza'})


def form(request):
    return render(request, 'form.html')


def add(request):
    num1 = int(request.GET["num1"])
    num2 = int(request.GET["num2"])
    sum = num1 + num2
    print(sum)
    return render(request, 'result.html', {'result': sum})

def subtract(request):
    num1 = int(request.POST["num1"])
    num2 = int(request.POST["num2"])
    sum = num1 + num2
    print(sum)
    return render(request, 'result.html', {'result': sum})
