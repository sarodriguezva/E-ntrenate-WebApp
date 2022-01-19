from django.urls import path # Hay un problema con django.cong.urls import urls
# from mysite.settings import MEDIA_ROOT, MEDIA_URL
from . import views


urlpatterns = [
    path('', views.usuariosAPI, name="createAndGetAllUsers"),
    path('deleteMe/', views.deleteMe, name="deleteAccount"),
    path('updateMe/', views.updateMe, name="updateMyData"),
    path('<userId>/', views.usuariosAPI, name="getOneUpdateAndDeleteUser"),
    # path('<str:pk>/', views.usuariosAPI, name='userId'),
    # path('savefile', views.SaveFile)
]
