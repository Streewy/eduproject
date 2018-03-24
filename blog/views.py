from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from blog.models import Blog
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import forms
from .forms import UserRegistrationForm
from django.contrib.auth import get_user_model
User = get_user_model()

def index(request):
    vals = Blog.objects.all()

    return render(request, 'index.html', locals())

def detail(request, url):
    val = Blog.objects.get(slug = url)

    return render(request, 'detail.html', locals())

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email =  userObj['email']
            password =  userObj['password']
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)
                user = authenticate(username = username, password = password)
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                raise forms.ValidationError('Looks like a username with that email or password already exists')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form' : form})
