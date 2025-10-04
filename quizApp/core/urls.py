from django.urls import path
from . import views

urlpatterns = [
    path('',views.Signin,name='signin'),
    path('start-quiz/',views.start_quiz, name='start-quiz'),
    path('create-quiz/<int:num>/<int:no>',views.create_quiz, name='create-quiz'),
    path('complete/', views.complete,name="complete")
]