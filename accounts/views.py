from django.shortcuts import render, redirect
# import requests
from .forms import RegistrationForm, LoginForm
from .models import Account
# from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']  # cleaned_data is used to get the data from the form
            last_name = form.cleaned_data['last_name']  # cleaned_data is used to get the data from the form
            email = form.cleaned_data['email']  # cleaned_data is used to get the data from the form
            password = form.cleaned_data['password']  # cleaned_data is used to get the data from the form
            username = form.cleaned_data['username']  # this is used to get the username from the email

            user = Account.objects.create_user(first_name=first_name, last_name=last_name, email=email,
                                               username=username, password=password)  # this is used to create a new user
            user.save()  # this is used to save the user in the database
            return redirect('login')
        
    else:
        form = RegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/register.html', context)

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']  # this is used to get the email 
            password = form.cleaned_data['password']  # cleaned_data is used to get the data from the form
            remember_me = form.cleaned_data['remember_me']  # cleaned_data is used to get the data from the form
        if remember_me:
            # Set session expiry based on your requirement
            request.session.set_expiry(604800)  # One week in seconds
        else:
            # Keep default session behavior
            request.session.set_expiry(0)  # Session ends when browser closes
            
        user = authenticate(request, email=email, password=password)
        if user is not None:
            auth.login(request, user)
            # messages.success(request, 'You are now logged in')
            
            return redirect('index')

        else:
            # messages.error(request, 'Invalid login credentials')
            return redirect('login')
    else:
        form = LoginForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)
    

@login_required(login_url='login')  # this is used to make sure that the user is logged in before they can access the logout
def logout(request):
    auth.logout(request)
    # messages.success(request, 'You are logged out')
    return redirect('login')