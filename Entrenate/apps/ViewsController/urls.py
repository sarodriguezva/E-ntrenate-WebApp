from django.urls import path # Hay un problema con django.cong.urls import urls
# from mysite.settings import MEDIA_ROOT, MEDIA_URL
from . import views


urlpatterns = [
    path('myCourses/', views.getMyCourses, name="myCourses"),
]
