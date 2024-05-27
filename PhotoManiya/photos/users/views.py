from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth
from photography.models import PhotoCategory

from users.forms import UserLoginForm, UserRegistrationForm
def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data= request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username = username, password = password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('photography:index'))
    else:
        form = UserLoginForm()
    context = {
        'title': 'Авторизация',
        'form': form,
    }
    return render(request, 'users/login.html', context)


def profile(request):
    context = {
        'title': 'Профиль',
    }
    return render(request, 'users/profile.html', context)

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
    context = {
        'title': 'Регистрация','form': form
    }
    return render(request, 'users/registration.html', context)

def new_photo(request):
    context = {
        'title': 'Новое изображение',
        'categorys': PhotoCategory.objects.all()
    }
    return render(request, 'users/profile.html', context)



