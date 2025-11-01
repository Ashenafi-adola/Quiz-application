from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Exam, Question


def Signin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        
    context = {

    }
    return render(request, 'core/login.html',context)

@login_required(login_url='signin')
def start_quiz(request):

    context = {

    }
    return render(request, 'core/create_quiz.html',context)

@login_required(login_url='signin')
def create_quiz(request,exam,num,no):
    
    context = {

    }
    return render(request, 'core/create_quiz.html',context)

@login_required(login_url='signin')
def complete(request):

    return render(request,'core/complete.html',{})

def startExam(request):

    context = {
       
    }
    return render(request,'core/start-exam.html',context)
def takeExam(request,title):
    
    context = {

    }
    return render(request,'core/take-exam.html', context)