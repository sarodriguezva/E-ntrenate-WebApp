from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from mongoConnection import db
# Create your views here.

@login_required()
def perfil(request):
    context = {'base_template': "basetemplate.html"}
    user_email = request.user.email
    datos = db.usuarios.find_one({"email": user_email})
    context['datos'] = datos
    return render(request=request, template_name="perfil/perfil.html", context=context)
