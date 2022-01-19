from smtplib import SMTPException
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from Entrenate.apps.Usuarios.models import usuarios, changedPasswordAfter
from bson import json_util
import json
from bson.objectid import ObjectId
# from django.contrib.auth import authenticate
import jwt
from django.conf import settings
from datetime import datetime
from .models import get_hashed_password, correctPassword, createPasswordResetToken
import datetime
from Email import Email
import hashlib
from django.http import HttpResponse

res = {'status': 'success'}

def signToken(id):
    return jwt.encode({'id': str(id), "exp": datetime.datetime.now() + datetime.timedelta(days=10), "iat": datetime.datetime.now()}, settings.SECRET_KEY, algorithm='HS256')


def createSendToken(user, status, req, res):
    token = signToken(user["_id"]) #str
    if "contraseña" in user.keys():
        del user["contraseña"]
    res["data"] = json.loads(json_util.dumps(user))
    res["token"] = token
    response = JsonResponse(res, status= status, safe=False)
    response.set_cookie('jwt', token, 
    expires=datetime.datetime.now() + datetime.timedelta(days=10),
    # secure=True, # Only https (productions)
    httponly=True)
    return response


@csrf_exempt
def login(request):
    if request.method == "POST":
        # correo = request.data.get('correo', KeyError)
        user_data = JSONParser().parse(request)
        if "correo" not in user_data.keys() or "contraseña" not in user_data.keys():
            return JsonResponse({"status": "fail", 'message': 'Credenciales invalidas. Por favor intenta de nuevo'}, status=status.HTTP_400_BAD_REQUEST, safe=False)
        user = usuarios.find_one({"correo": user_data["correo"]}, {"activo": 0})
        if not user or not correctPassword(user_data["contraseña"], user["contraseña"]):
            return JsonResponse({"status": "fail", "message": "No se encontro ningun usuario con las credenciales dadas"}, status=status.HTTP_401_UNAUTHORIZED, safe=False)
        res['data'] = json.loads(json_util.dumps(user))
        res["message"] = "Has iniciado sesión"
        return createSendToken(user, status.HTTP_201_CREATED, request, res)
        
@csrf_exempt    
def logout(request):
    res = {'status': 'success'}
    HttpResponse.delete_cookie("jwt")
    return JsonResponse(res, status=status.HTTP_200_OK, safe=False)

@csrf_exempt
def signup(request): 
    if request.method == "POST": 
        # print(request.body, "data")
        # body = json.loads(request.body)
        # print(body, 'body')
        user_data = JSONParser().parse(request)
        # print(user_data, "SIGNUP BEFORE INSERT")
        contraseña = user_data["contraseña"]
        if contraseña != user_data['confirmar_contraseña']:
            return JsonResponse({'status': 'fail', 'message': 'Las campos no coinciden'}, status=status.HTTP_400_BAD_REQUEST, safe=False)
        del user_data["confirmar_contraseña"]
        user_data["contraseña"] = get_hashed_password(contraseña) 
        user_data["rol"] = "estudiante"
        user_data["activo"] = True
        usuarios.insert_one(user_data)
        # print(user_data, "SIGNUP AFTER INSERT")
        res['data'] = user_data
        url = f"{request.scheme}://{request.get_host()}/me"
        emailTitle = "Bienvenido a E-ntrenate"
        emailMessage = "Te damos la bienvenida a la plataforma número uno de cursos virtuales, que esperas empezemos a aprender!"
        Email(res["data"], url).send_email(emailTitle, emailMessage, "correo.html")
        res["message"] = "Has creado una nueva cuenta."
        return createSendToken(user_data, status.HTTP_201_CREATED, request, res)

@csrf_exempt
def protect(request):
    try:
        # request.headers
        token = None
        # print(request.headers)
        # print(request.headers["authorization"])
        # 1) Getting tokenand check if it´s there
        if ("authorization" in request.headers.keys() and request.headers["authorization"].startswith("Bearer")):
            token = request.headers["authorization"].split(" ")[1]
        # print(token)

        if not token:
            return JsonResponse({"status": "fail", "message": "No has ingresado con una cuenta. Por favor ingresa para tener acceso."}, status=status.HTTP_401_UNAUTHORIZED, safe=False)

        # 2) Verification token
        # 4) Check if user changed password after the token was issued
        decoded = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'], options={"require": ["exp", "iat"]})
        print(decoded)

        # 3) Check if user still exists
        # document = usuarios.find_one({"_id": ObjectId(decoded["id"])}, {"contraseña": 0})
        document = usuarios.find_one({"_id": ObjectId(decoded["id"])}, {"contraseña": 0, "activo": 0})
        currentUser = json.loads(json_util.dumps(document))
        print(currentUser, "CURRENT-USER PROTECT")
        if not currentUser:
            return JsonResponse({"status": "fail", "message": "El usuario perteneciente a este token ya no existe."}, status=status.HTTP_401_UNAUTHORIZED, safe=False)

        # 4) Check if user changed password after the token was issued
        if changedPasswordAfter(decoded["iat"], currentUser):
            return JsonResponse({"status": "fail", "message": "El usuario cambio la contraseña. Por favor ingrese de nuevo."}, status=status.HTTP_401_UNAUTHORIZED, safe=False)
        
        request.META["user"] = currentUser
    except jwt.ExpiredSignatureError:
        print("El token expiro")


@csrf_exempt
def restricTo(request, roles):
    print(request.META["user"])
    if request.META["user"]["rol"] not in roles:
        return JsonResponse({"status": "fail", "message": "No tienes permiso para ejecutar esta acción"}, status=status.HTTP_403_FORBIDDEN, safe=False)

@csrf_exempt
def forgotPassword(request):
    res = {'status': 'success'}
    print("Entre a forgotPassword")
    if request.method == "POST":
        print("Entre a forgotPassword y es un post")
        user_data = JSONParser().parse(request)
        mail = user_data["correo"]
        print(mail, "Este es el mail para cambiar la contraseña")
        user = usuarios.find_one({"correo": user_data["correo"]}, {"contraseña": 0, "activo": 0})
        if not user:
            return JsonResponse({"status": "fail", "message": "No se encontro ningun usuario con las credenciales dadas"}, status=status.HTTP_404_NOT_FOUND, safe=False)
        resetToken = createPasswordResetToken(mail)
        try:
            user = json.loads(json_util.dumps(user))
            resetURL = f"{request.scheme}://{request.get_host()}/api/v1/auth/cambiarContraseña/{resetToken}"
            message = f"¿Olvidate tu contraseña? Ingresa tu nueva contraseña y confirmala usando el siguiente link: {resetURL}. \nSi no has olvidado tu contraseña por favor ignora este correo."
            emailTitle = 'Token para cambiar contraseña (Valido por 10 minutos)'
            Email(user, resetURL).send_email(emailTitle, message, "correo.html")
            res["message"] = "El token fue enviado al correo"
            return JsonResponse(res, status=status.HTTP_200_OK, safe=False)
        except SMTPException:
            usuarios.find_one_and_update({"correo": user_data["correo"]}, {"$unset":{"passwordResetToken": "", "passwordResetExpires": ""}})
            return JsonResponse({"status": "fail", "message": "Hubo un error enviando el correo. Por favor intenta de nuevo"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR, safe=False)

@csrf_exempt
def resetPassword(request, token=None):
    if request.method == "POST":
        user_data = JSONParser().parse(request)
        contraseña = user_data["contraseña"]
        if user_data['contraseña'] != user_data['confirmar_contraseña']:
            return JsonResponse({'status': 'fail', 'message': 'Las campos no coinciden'}, status=status.HTTP_400_BAD_REQUEST ,safe=False)
        resetToken = token
        hashResetToken = hashlib.sha256()
        hashResetToken.update(bytes(resetToken, encoding="utf8"))
        # print(hashResetToken.hexdigest(), "HASH-RESET AUTH-VIEW")
        # print(type(hashResetToken.hexdigest()), "TYPE OF HASH-RESET AUTH-VIEW")
        today = datetime.datetime.now()
        print(today, "TODAY")
        user = usuarios.find_one({"passwordResetToken": hashResetToken.hexdigest(), "passwordResetExpires": { "$gt": today}}, {"contraseña": 0, "activo": 0})
        if not user:
            return JsonResponse({"status": "fail", "message": "No se encontro ningun usuario con las credenciales dadas"}, status=status.HTTP_404_NOT_FOUND, safe=False)
        user_data["contraseña"] = get_hashed_password(contraseña)
        usuarios.find_one_and_update({"passwordResetToken": hashResetToken.hexdigest(), "passwordResetExpires": { "$gt": today }}, {"$unset":{"passwordResetToken": "", "passwordResetExpires": ""}, "$set": {"contraseña": user_data["contraseña"], "passwordChangedAt": today.timestamp()}})
        res["message"] = "La contraseña se ha cambiado correctamente."
        res['data'] = json.loads(json_util.dumps(user_data))
        return createSendToken(user, status.HTTP_200_OK, request, res)


@csrf_exempt
def updatePassword(request):
    res = {'status': 'success'}
    print(request.META["user"], "USER de PROTECT")
    if request.method == "POST":
        user_data = JSONParser().parse(request)
        contraseña = user_data["contraseña"]
        if user_data['contraseña'] != user_data['confirmar_contraseña']:
            return JsonResponse({'status': 'fail', 'message': 'Las campos no coinciden'}, status=status.HTTP_400_BAD_REQUEST ,safe=False)
        user = usuarios.find_one({"_id": ObjectId(request.META["user"]["_id"]["$oid"])}, {"activo": 0})
        if not user or not correctPassword(user_data["contraseña_actual"], user["contraseña"]):
                return JsonResponse({"status": "fail", "message": "Tu contraseña actual es incorrecta"}, status=status.HTTP_401_UNAUTHORIZED, safe=False)
        user_data["contraseña"] = get_hashed_password(contraseña)
        today = datetime.datetime.now()
        usuarios.find_one_and_update({'_id': ObjectId(request.META["user"]["_id"]["$oid"])}, {"$set": {"contraseña": user_data["contraseña"], "passwordChangedAt": today.timestamp()}})
        res["message"] = "Se actualizo la contraseña"
        return createSendToken(user, status.HTTP_200_OK, request, res)
        
