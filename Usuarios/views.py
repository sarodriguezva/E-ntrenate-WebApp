from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt # Permite que otros dominios accedan a nuestros API methods
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from Usuarios.models import Usuario
from Usuarios.serializers import UsuarioSerializer

# import sys, os
# sys.path.append(os.path.abspath(os.path.join('..', 'utils')))

from handler_factory import deleteOne, createOne, updateOne, getAll, getOne

from utils import usuarios

from django.core.files.storage import default_storage # To store images

# Create your views here.
# Aqui van los API methods

@csrf_exempt
def usuariosAPI(request, userId=None):
    response = {'status': 'success'}
    if request.method == 'GET':
        if userId:
            user = getOne(usuarios, userId)
            users_serializer = UsuarioSerializer(data=user)
            response['data'] = user
            return JsonResponse(response, safe=False)
        users = getAll(usuarios)
        print(users, 'todos los usuarios')
        users_serializer = UsuarioSerializer(users, many=True) # Usamos el serializer para convetirlo en un modelo, con las validaciones de python que pusimos en models.py.
        response['data'] = users
        return JsonResponse(response, safe=False)
    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        users_serializer = UsuarioSerializer(data=user_data)
        users_serializer.is_valid()
        print(users_serializer.errors)
        if users_serializer.is_valid():
            print(type(users_serializer.data))
            print(users_serializer.data)
            createOne(usuarios, users_serializer.data)
            response['data'] = users_serializer.data
            return JsonResponse(response, safe=False)
        return JsonResponse(users_serializer.errors, safe=False)
    elif request.method == 'PATCH':
        user_data = JSONParser().parse(request)
        # user['pk'] = pk
        # users_serializer = UsuarioSerializer(user, data=user_data, partial=True)
        # print(type(user_data)) # dict
        updatedUser = updateOne(usuarios, userId, user_data)
        response['data'] = updatedUser
        return JsonResponse(response, safe=False)
    elif request.method == 'DELETE':
        deleteOne(usuarios, userId)
        return JsonResponse("Deleted Succesfully", safe=False)


        

@csrf_exempt
def SaveFile(request):
    file=request.FILES['file']
    file_name=default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)