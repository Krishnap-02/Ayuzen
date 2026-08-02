from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


def register(request):

    if request.method == 'POST':

        form = RegistrationForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']

            if password != confirm_password:
                form.add_error('confirm_password', 'Passwords do not match')

            elif User.objects.filter(username=username).exists():
                form.add_error('username', 'Username already exists')

            elif User.objects.filter(email=email).exists():
                form.add_error('email', 'Email already exists')

            else:
                User.objects.create_user(
                    username=username,
                    email=email,
                    password=password
                )

                return redirect('login')

    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})




def user_login(request):

    if request.method == 'POST':

        form = LoginForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(
                username=username,
                password=password
            )

            if user is not None:

                login(request, user)

                return redirect('home')

            else:

                form.add_error(None, 'Invalid username or password')

    else:

        form = LoginForm()

    return render(request, 'login.html', {'form': form})


@login_required
def profile(request):
    return render(request,'profile.html')



def user_logout(request):

    logout(request)

    return redirect('home')