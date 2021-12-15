from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "authentication"
urlpatterns = [
        path('login', views.login, name="login"),
        path('singin', views.sign_up, name='sign up')
        ]
