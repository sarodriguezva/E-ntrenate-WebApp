from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.http import HttpResponse
from pymongo import MongoClient, cursor, errors
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

    if request.method == "POST":
        print("POST")
        form = forms.login_form(request.POST)
        print(form)
        print(form.cleaned_data)
        if form.is_valid():
            data = form.cleaned_data

            print("User authenticate")
            user = authenticate(email=data["email"], password= data["password"])
            user = None

            if user is not None:
                login(request, user)
                print("LOGIn")
                redirect("home")
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
        print("POST")
        form = forms.signup_form(request.POST)
        print(form)
        if form.is_valid():
            data = form.cleaned_data
            username = data["username"]
            email = data["email"]
            password = data["password"]
            connection_string = "mongodb+srv://dapstab:kidAmnesia@e-ntrenate.nnlqu.mongodb.net/E-ntrenate?retryWrites=true&w=majority"

            client = MongoClient(connection_string)
            db = client["E-ntrenate"]
            user = User.objects.create_user(username, email, password)
            print(data)
            user.save()
            data["rol"]= 'estudiante'
            date_ = data["date"]
            data["date"] = date_.strftime('%m/%d/%Y')
            db.usuarios.insert_one(data)
            client.close()
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
