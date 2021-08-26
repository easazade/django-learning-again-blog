from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            print('logged in user')
            return redirect('/')
        else:
            messages.info(request, 'invalid credentials')
            print('invalid credentials')
            return redirect('login')

    else:
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        if password1 != password2:
            messages.info(request, 'passwords does not match')
            print('passwords does not match')
            return redirect('register')
        elif User.objects.filter(username=username).exists():
            messages.info(request, 'username already exists')
            print('username already exists')
            return redirect('register')
        user = User.objects.create_user(
            username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
        user.save()
        print('user created')
        return redirect('/')
    else:
        return render(request, 'register.html')
