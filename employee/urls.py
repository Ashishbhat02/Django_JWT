from django.contrib import admin
from django.urls import path,include

from employee import views

urlpatterns = [
    # path('employees/', views.home , name='home'),
     path('sign_up/', views.RegisterView.as_view()),
     path('login/', views.LoginView.as_view()),
]
