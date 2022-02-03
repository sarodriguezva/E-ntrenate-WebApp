from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.http import HttpResponse

@csrf_exempt
def login_view(request):
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
    logout(request)
    return redirect("home")

@csrf_exempt
def signup_view(request): 
    context = {}
    status = 'InitSignUp'
    form = None

    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        print("POST")
        form = forms.signup_form(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            username = data["username"]
            email = data["email"]
            password = data["password"]
            user = User.objects.create_user(username, email, password)
            print(data)
            user.save()
            #usuarios.insert_one(user)
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
