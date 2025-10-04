from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ExamTaker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    mark = models.IntegerField()

    def __str__(self):
        return self.full_name
    
class Exam(models.Model):
    question = models.TextField()
    choice1 = models.CharField(max_length=255)
    choice2 = models.CharField(max_length=255)
    choice3 = models.CharField(max_length=255)
    choice4 = models.CharField(max_length=255)

    def __str__(self):
        return self.question