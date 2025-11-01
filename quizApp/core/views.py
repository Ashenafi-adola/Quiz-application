from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Exam, Question
from django.contrib.auth.forms import UserCreationForm

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')
        
    context = {
        "form":form
    }
    return render(request, 'core/register_page.html',context)

def Signin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)

        if user != None:
            login(request, user)
            
    context = {

    }
    return render(request, 'core/login.html',context)

def home(request):

    context = {

    }
    return render(request, 'core/create_quiz.html',context)
