from django.urls import path, include # Hay un problema con django.cong.urls import urls
# from mysite.settings import MEDIA_ROOT, MEDIA_URL
from . import views


urlpatterns = [
    path('', views.cursos, name="createUpdateAndDeleteCourses"),
    path("<courseId>/reviews/", include("Entrenate.apps.Foros.urls"), name="Foros"),
    path('<courseId>/', views.cursosAPI, name="UpdateAndDeleteCourse"),
    # path('<str:pk>/', views.usuariosAPI, name='userId'),
    # path('savefile', views.SaveFile)
]
