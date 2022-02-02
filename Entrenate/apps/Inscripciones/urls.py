from django.urls import path
from . import views

urlpatterns = [
    path('joinCourse/', views.joinCourse, name="joinCourse"),
]