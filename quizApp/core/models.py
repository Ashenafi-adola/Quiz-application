from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Exam(models.Model):
    title = models.CharField(max_length=30)
    def __str__(self):
        return self.title

class ExamTaker(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    mark = models.IntegerField()

    def __str__(self):
        return self.full_name

class Question(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE,null=True,blank=True)
    question = models.TextField()
    A = models.CharField(max_length=255)
    B = models.CharField(max_length=255)
    C = models.CharField(max_length=255)
    D = models.CharField(max_length=255)
    Answer = models.CharField(max_length=1)

    def __str__(self):
        return f"{self.question} {self.exam}"
    
class Mark(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    mark = models.IntegerField()

    def __str__(self):
        return f"{self.mark}"