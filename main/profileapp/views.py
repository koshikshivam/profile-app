from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateUserForm, ProfileForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user


@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')


@login_required(login_url='login')
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES,
                           instance=request.user.profile)
        if form.is_valid():
            form.save()

            username = request.user.username
            
            return redirect('/')
    else:
        form = ProfileForm(instance=request.user.profile)
    context = {'form': form}
    return render(request, 'profile.html', context)


@unauthenticated_user
def login_person(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return redirect('login')
    return render(request, 'login_page.html')


@unauthenticated_user
def registration(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile is created successfully')
            return redirect('login')
        else:
            context = {'form': form}
            
            return render(request, 'register_page.html', context)

    context = {'form': form}
    return render(request, 'register_page.html', context)


@login_required(login_url='login')
def logout_user(request):
    logout(request)

    return redirect('login')
