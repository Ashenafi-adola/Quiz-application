from django.forms import ModelForm
from .models import Exam,Question,ExamTaker
class QuestionForm(ModelForm):

    class Meta:
        model = Question
        fields = "__all__"
        exclude = ["exam"]


class StartForm(ModelForm):
    class Meta:
        model = Question
        fields = ['exam']