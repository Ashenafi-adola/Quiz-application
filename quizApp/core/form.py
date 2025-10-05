from django.forms import ModelForm
from .models import Exam,Question,ExamTaker
class QuestionForm(ModelForm):

    class Meta:
        model = Question
        fields = "__all__"