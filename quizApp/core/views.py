from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Exam, Question
from django.contrib.auth.forms import UserCreationForm
from .forms import ExamForm, QuestionForm
from datetime import date

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
    form2 = ExamForm()
    if request.method == 'POST':
        form2 = ExamForm(request.POST)
        if form2.is_valid() and form1.is_valid():
            Exa = form2.save(commit=False)
            Exa.published_date = date.today()
            Exa.save()
            return redirect('home')
    context = {
        'form2':form2,
    }
    return render(request, 'core/add_exam.html', context)
def home(request):

    context = {

    }
    return render(request, 'core/home.html',context)
