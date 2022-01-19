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
from django.urls import path
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="Homepage"),
    #tmp for log in
    path('home_login/', views.home_login, name="home_login"),
    # path('auth/', include('entrenatewebapp.apps.authentication.urls', namespace='authentication')),
    path('api/v1/usuarios/', include('Entrenate.apps.Usuarios.urls'), name="Usuarios"),
    path('api/v1/cursos/', include('Entrenate.apps.Cursos.urls'), name="Cursos"),
    path('api/v1/auth/', include('Entrenate.apps.Autenticacion.urls'), name="Autenticación")
]
