from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
import json
from .models import Exam, ExamTaker
from .form import QuestionForm


question = {}
def Signin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user.is_superuser:
            login(request,user)
            return redirect('start-quiz')
        elif user is not None:
            login(request,user)
    context = {

    }
    return render(request, 'core/login.html',context)
@login_required(login_url='signin')
def start_quiz(request):
    start = 'no'
    if request.GET.get('start') == 'start':
        number_of_questions = int(request.GET.get('num_of_questions'))
        if number_of_questions >= 5:
            begin = 1
            return redirect(f'/create-quiz/{number_of_questions}/{begin}')
    
    context = {
        "start":start,
    }
    return render(request, 'core/create_quiz.html',context)

@login_required(login_url='signin')
def create_quiz(request,num,no):
    start = 'yes'
    
    if no <= num:
        form = QuestionForm()
        if request.method == "POST":
            form = QuestionForm(request.POST)
            if form.is_valid():
                #form.save()
                no+=1
                return redirect(f'/create-quiz/{num}/{no}')
    else:
        return redirect('complete')
    context = {
        "start":start,
        "form": form,
    }
    return render(request, 'core/create_quiz.html',context)

@login_required(login_url='signin')
def complete(request):

    return render(request,'core/complete.html',{})

def takeExam(request):
    questions = Exam.objects.all()
    

    return render(request,'core/')