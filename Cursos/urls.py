from django.urls import path # Hay un problema con django.cong.urls import urls
# from mysite.settings import MEDIA_ROOT, MEDIA_URL
from Cursos import views


urlpatterns = [
    path('', views.cursosAPI),
    path('<courseId>/', views.cursosAPI),
    # path('<str:pk>/', views.usuariosAPI, name='userId'),
    # path('savefile', views.SaveFile)
]