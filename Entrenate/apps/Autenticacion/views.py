from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.http import HttpResponse
from pymongo import MongoClient, cursor, errors
from mongoConnection import db
import datetime

@csrf_exempt
def login_view(request):
    '''
    Vista del login, funcion a traves de la cual
    se haran las request de login
    '''
    context = {'title':'Login'}
    status = 'InitLogin'
    form = None

    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = forms.login_form(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data["username"], password= data["password"])
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                status = "LoginFail"
    else:
        form = forms.login_form()

    context['status'] = status
    context['form'] = form

    return render(request = request, template_name = "authentication/login.html", context = context)

@csrf_exempt
def logout_view(request):
    '''
    Funcion encargada unicamente de hacer el logout y redirigir a home
    '''
    logout(request)
    return redirect("home")

@csrf_exempt
def signup_view(request):
    '''
    Vista del signup, funcion a traves de la cual
    se haran las request de signup
    '''
    context = {}
    status = 'InitSignUp'
    form = None
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = forms.signup_form(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            username = data["username"]
            email = data["email"]
            password = data["password"]
            if 'usuarios' not in db.list_collection_names():
                usuarios = db.create_collection('usuarios')
            data["rol"]= 'estudiante'
            date_ = data["date"]
            data["date"] = date_.strftime('%m/%d/%Y')
            db.usuarios.insert_one(data)
            user = User.objects.create_user(username, email, password)
            user.save()
            login(request, user)
            return redirect("home")
        else:
            print("Invalid form")
            status = "SignUpFail"

    else:
        form = forms.signup_form()

    context['status'] = status
    context['form'] = form
    return render(request = request, template_name = "authentication/signup.html", context = context)

@csrf_exempt
def change_password(request):
    '''
    Cambia el password
    '''
    current_user = request.user
    current_user.set_password('')
    current_user.save()
    return redirect('perfil')

@csrf_exempt
def delete_account(request):
    '''
    Elimina la cuenta del request
    '''
    current_user = request.user
    logout(request)
    db.usuarios.delete_one({"username" : current_user.username})
    current_user.delete()
    return redirect("home")
