"""Entrenate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    #tmp for log in
    path('home_login/', views.home_login, name="home_login"),
    #path('auth/', include('Entrenate.apps.Autenticacion.urls', namespace='Autenticacion')),
    path('usuarios/', include('Entrenate.apps.Usuarios.urls'), name="Usuarios"),
    path('cursos/', include('Entrenate.apps.Cursos.urls'), name="Cursos"),
    path('auth/', include('Entrenate.apps.Autenticacion.urls'), name="Autenticacion"),
    path('inscripcion/', include('Entrenate.apps.Inscripciones.urls'), name="Inscripciones"),
    # path('api/v1/foros/', include('Entrenate.apps.Foros.urls'), name="Foros"),
    path('cursos/', views.cursos, name="cursos"),
    path('perfil/', include('Entrenate.apps.Perfil.urls'), name="Perfil"),
    path('login/', views.getLoginForm, name="getLoginForm"),
    path('foro/', views.foro, name="foro"),
    path('misCursosCreados/', views.getMyCreatedCourses, name="myCreatedCourses"),
    path('misCursos/', views.getMyCourses, name="myCourses"),
    path('curso/<courseSlug>/', views.getMyCourses, name="myCourses"),
]
