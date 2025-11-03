from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Exam(models.Model):
    instractor = models.ForeignKey(User, on_delete=models.CASCADE)
    exam_title = models.CharField(max_length=255)
    published_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.exam_title

class Question(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE,null=True,blank=True)
    question = models.TextField()
    A = models.CharField(max_length=255)
    B = models.CharField(max_length=255)
    C = models.CharField(max_length=255)
    D = models.CharField(max_length=255)
    Answer = models.CharField(max_length=1)

    def __str__(self):
        return f'{self.question}'
    