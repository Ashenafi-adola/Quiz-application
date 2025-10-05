from django.contrib import admin
from .models import Exam,ExamTaker,Question
# Register your models here.
admin.site.register(Exam)
admin.site.register(ExamTaker)
admin.site.register(Question)