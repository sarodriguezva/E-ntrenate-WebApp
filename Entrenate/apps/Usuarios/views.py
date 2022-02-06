from datetime import datetime
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt # Permite que otros dominios accedan a nuestros API methods
from bson.objectid import ObjectId
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from handler_factory import deleteOne, createOne, updateOne, getAll, getOne

from django.core.files.storage import default_storage # To store images
from bson import json_util
import json
from rest_framework import status

# import sys, os
# sys.path.append(os.path.abspath(os.path.join('..', 'utils')))

# Create your views here.
# Aqui van los API methods

def filterDict(obj, allowedFields):
    newDict = {}
    for key in obj.keys():
        if key in allowedFields:
            newDict[key] = obj[key]
    return newDict
@csrf_exempt
def usuariosAPI(request, userId=None):    
    if request.method == 'GET':
        if userId:
            return getOne(usuarios, userId)
        return getAll(usuarios)
    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        contraseña = user_data["contraseña"]
        if user_data['contraseña'] != user_data['confirmar_contraseña']:
            return JsonResponse({'status': 'fail', 'message': 'Las campos no coinciden'}, status=status.HTTP_400_BAD_REQUEST ,safe=False)
        user_data["contraseña"] = get_hashed_password(contraseña)
        user_data["rol"] = "estudiante"
        user_data["activo"] = True
        return createOne(usuarios, user_data)
    elif request.method == 'PATCH':
        user_data = JSONParser().parse(request)
        # user['pk'] = pk
        # users_serializer = UsuarioSerializer(user, data=user_data, partial=True)
        # print(type(user_data)) # dict
        return updateOne(usuarios, userId, user_data)
    elif request.method == 'DELETE':
        return deleteOne(usuarios, userId)

@csrf_exempt
def updateMe(request):
    response = {'status': 'success'}
    if request.method == "POST":
        # 1) Create error if user POST password data
        user_data = JSONParser().parse(request)
        if "contraseña" in user_data.keys() or "confirmar-contraseña" in user_data.keys():
            return JsonResponse({"status": "fail", "message": "Esta ruta no se utiliza para cambiar contraseñas. Por favor utiliza /updateMyPassword"}, status=status.HTTP_400_BAD_REQUEST, safe=False)

        # 3) Filtered out unwanted fields names that are not allowed to be updated
        filteredBody = filterDict(user_data, ["nombre", "correo"])
        
        # 2) Update user document
        updatedUser = usuarios.find_one_and_update({"_id": ObjectId(request.META["user"]["_id"]["$oid"])}, {"$set": filteredBody}, {"returnOriginal": False})
        response["data"] = json.loads(json_util.dumps(updatedUser))
        return JsonResponse(response, status=status.HTTP_200_OK ,safe=False)

@csrf_exempt
def deleteMe(request):
    response = {'status': 'success'}
    usuarios.find_one_and_update({"_id": ObjectId(request.META["user"]["_id"]["$oid"])}, {"$set": {"activo": False}}, {"returnOriginal": False})
    return JsonResponse(response, status=status.HTTP_204_NO_CONTENT, safe=False)

# @csrf_exempt
# def SaveFile(request):
#     file=request.FILES['file']
#     file_name=default_storage.save(file.name, file)
#     return JsonResponse(file_name, safe=False)
