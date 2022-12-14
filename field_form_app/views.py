from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserForm

def index(request):
    posts = [{'title': 'Name_Post', 'text': 'Text_Post',
              'image': 'https://avatarko.ru/img/kartinka/33/multfilm_lyagushka_32117.jpg'}]
    return render(request, 'index.html', {'posts': posts})

def main(request):
    userform = UserForm()
    return render(request, 'main.html', {'form': UserForm()})