from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
import json
from .models import Exam, ExamTaker
from .form import QuestionForm, StartForm


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
            return redirect()
    context = {

    }
    return render(request, 'core/login.html',context)
@login_required(login_url='signin')
def start_quiz(request):
    start = 'no'
    form = StartForm()
    if request.GET.get('start') == 'start':
        id = request.GET.get('exam')
        exam = Exam.objects.get(id=id)
        number_of_questions = int(request.GET.get('num_of_questions'))
        if number_of_questions >= 5:
            begin = 1
            return redirect(f'/create-quiz/{exam}/{number_of_questions}/{begin}')
    
    context = {
        "start":start,
        "form":form,
    }
    return render(request, 'core/create_quiz.html',context)

@login_required(login_url='signin')
def create_quiz(request,exam,num,no):
    start = 'yes'
    if no <= num:
        form = QuestionForm()
        if request.method == "POST":
            form = QuestionForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.Exam = exam
                no+=1
                return redirect(f'/create-quiz/{exam}/{num}/{no}')
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
    
    context = {

    }
    return render(request,'core/start-exam.html',context)