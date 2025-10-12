from django.forms import ModelForm
from .models import Exam,Question,ExamTaker


class StartForm(ModelForm):
    class Meta:
        model = Question
        fields = ['exam']

class TakeExamForm(ModelForm):
    class Meta:
        model = ExamTaker
        fields = "__all__"
        exclude = ['mark','user']