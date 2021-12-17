from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt # Permite que otros dominios accedan a nuestros API methods
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.utils import json

from Usuarios.models import usuarios
from bson import json_util
import json

from handler_factory import deleteOne, createOne, updateOne, getAll, getOne

from django.core.files.storage import default_storage # To store images


# import sys, os
# sys.path.append(os.path.abspath(os.path.join('..', 'utils')))

# Create your views here.
# Aqui van los API methods

@csrf_exempt
def usuariosAPI(request, userId=None):
    response = {'status': 'success'}
    if request.method == 'GET':
        if userId:
            user = getOne(usuarios, userId)
            response['data'] = user
            return JsonResponse(response, safe=False)
        users = getAll(usuarios)
        response['data'] = users
        return JsonResponse(response, safe=False)
    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        if user_data['contraseña'] != user_data['confirmar_contraseña']:
            return JsonResponse({'status': 'fail', 'message': 'Las campos no coinciden'}, safe=False)
        print(user_data)
        createOne(usuarios, user_data)
        response['data'] = json.loads(json_util.dumps(user_data))
        return JsonResponse(response, safe=False)
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