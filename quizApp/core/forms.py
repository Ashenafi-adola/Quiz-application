from django.forms import ModelForm
from .models import Exam,Question,Student
from django.contrib.auth.models import User


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['name']

class ExamForm(ModelForm):
    class Meta:
        model = Exam
        fields = ['title']

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = '__all__'
        exclude = ['exam']