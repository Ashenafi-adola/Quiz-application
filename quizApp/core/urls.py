from django.urls import path
from . import views

urlpatterns = [
    path('',views.Signin,name='signin'),
    path('create-quiz/',views.start_quiz, name='start-quiz'),
    path('create-quiz/<str:exam>/<int:num>/<int:no>',views.create_quiz, name='create-quiz'),
    path('complete/', views.complete,name="complete"),
    path('start-quiz/', views.takeExam,name='')
]