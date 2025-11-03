from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Exam, Question
from django.contrib.auth.forms import UserCreationForm
from .forms import ExamForm, StudentForm, QuestionForm

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
            return redirect('home')
            
    context = {

    }
    return render(request, 'core/login.html',context)
@login_required(login_url='signin')
def add_exam(request):
    form = StudentForm()
    context = {
        'form':form,
    }
    return render(request, 'core/add_exam.html', context)
def home(request):

    context = {

    }
    return render(request, 'core/home.html',context)
