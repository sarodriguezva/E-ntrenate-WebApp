from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.getAllReviews, name="getAllReviews"),
    path("get/<reviewId>", views.getReview, name="getReview"),
    path('post/', views.createReview, name="createReview"),
    path('<reviewId>/', views.forosAPI, name="updateAndDeleteReview"),
]
