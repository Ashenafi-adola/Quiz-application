from django.urls import path
from . import views

urlpatterns = [
    path('',views.Signin,name='signin'),
    path('signup/', views.register, name="register"),
    path('home/', views.home, name='home'),
    path('add_exam/', views.add_exam, name='add_exam')
]