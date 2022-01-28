from typing import Any
from django.shortcuts import render

def home(request: Any):
    """
    Vista de Home
    """
    context = {'base_template': "basetemplate.html"}

    if request.user.is_authenticated:
        context['base_template'] = "basetemplate_loggedin.html"

    return render(request=request, template_name="home/home.html", context=context)

#tmp for login
def home_login(request: Any):
    context = {'base_template': "basetemplate.html"}

    return render(request=request, template_name="home/user_home.html", context=context)

#tmp for cursos
def cursos(request: Any):
    context = {'base_template': "basetemplate.html"}

    return render(request=request, template_name="cursos/cursos.html", context=context)

#tmp for perfil
def perfil(request: Any):
    context = {'base_template': "basetemplate.html"}

    return render(request=request, template_name="perfil/perfil.html", context=context)

#tmp for perfil
def foro(request: Any):
    context = {'base_template': "basetemplate.html"}

    return render(request=request, template_name="foro/foro.html", context=context)

