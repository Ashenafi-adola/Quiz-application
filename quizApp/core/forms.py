from django.forms import ModelForm
from .models import Exam,Question
from django.contrib.auth.models import User

class ExamForm(ModelForm):
    class Meta:
        model = Exam
        fields = ['exam_title']

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = '__all__'
        exclude = ['exam']