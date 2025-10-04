from django.forms import ModelForm
from .models import Exam
class QuestionForm(ModelForm):

    class Meta:
        model = Exam
        fields = "__all__"