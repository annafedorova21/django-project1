from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile
from django.contrib.auth.forms import UserCreationForm


def register_user(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'User created!')
            login(request, user)
            return redirect('profiles')
        else:
            messages.success(request, 'Something went wrong occurred during registration')

    page = 'register'
    context = {'page': page, 'form': form}
    return render(request, 'users/login_register.html', context)


def logout_user(request):
    logout(request)
    messages.error(request, 'The user is logout')
    return redirect('login-user')


def login_user(request):
    page = 'login'
    if request.user.is_authenticated:
        return render('profiles')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'There is no such a user')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                redirect('loggined')
            else:
                messages.error(request, 'username or password is incorrect')

    return render(request, 'users/login_register.html')


def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'users/profiles.html', context)


def user_profile(request, pk):
    profile = Profile.objects.get(id=pk)
    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")

    context = {'profile': profile, 'topSkills': topSkills,
               "otherSkills": otherSkills}
    return render(request, 'users/user-profile.html', context)
