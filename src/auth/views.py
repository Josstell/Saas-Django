from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if all([username, password]):
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print("Logged in")
                return redirect('/')
    return render(request, 'auth/login.html', {})


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        try:

            if all([username, password, email]):
                user = User.objects.create_user(
                    username=username, password=password, email=email)
                if user is not None:
                    login(request, user)
                    print("Logged in")
                    return redirect('/')
        except:
            pass

    return render(request, 'auth/register.html', {})
