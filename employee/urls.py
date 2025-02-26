from django.contrib import admin
from django.urls import path,include

from employee import views

urlpatterns = [
    # path('employees/', views.home , name='home'),
     path('reg/', views.RegisterView.as_view()),
     path('login/', views.LoginView.as_view()),
     path('emp_details/', views.DetailsViews.as_view())
]
