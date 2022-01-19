import datetime
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt # Permite que otros dominios accedan a nuestros API methods
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.utils import json
from bson.objectid import ObjectId

from .models import cursos
from bson import json_util
import json
from slugify import slugify

from handler_factory import deleteOne, createOne, updateOne, getAll, getOne

# from django.core.files.storage import default_storage # To store images
from rest_framework import status


# import sys, os
# sys.path.append(os.path.abspath(os.path.join('..', 'utils')))

# Create your views here.
# Aqui van los API methods
response = {'status': 'success'}

@csrf_exempt
def cursosAPI(request, courseId=None):    
    if request.method == 'GET':
        if courseId:
            return getOne(cursos, courseId)
        return getAll(cursos)
    elif request.method == 'POST':
        course_data = JSONParser().parse(request)
        course_data["creadoPor"] = ObjectId(request.META["user"]["_id"]["$oid"])
        course_data["activo"] = True
        course_data["fechaCreación"] = datetime.datetime.now()
        course_data["slug"] = slugify(course_data["nombre"])
        return createOne(cursos, course_data)
    elif request.method == 'PATCH':
        course_data = JSONParser().parse(request)
        return updateOne(cursos, courseId, course_data)
    elif request.method == 'DELETE':
        return deleteOne(cursos, courseId)

@csrf_exempt
def createMyCourse(request):
    if request.method == 'POST':
        course_data = JSONParser().parse(request)
        course_data["creadoPor"] = ObjectId(request.META["user"]["_id"]["$oid"])
        course_data["activo"] = True
        course_data["fechaCreación"] = datetime.datetime.now()
        course_data["slug"] = slugify(course_data["nombre"])
        return createOne(cursos, course_data)

def editMyCourse(request, courseId=None):
    response = {'status': 'success'}
    if request.method == 'POST': 
        curso = cursos.find_one({"_id": ObjectId(courseId)})
        if not curso:
            return JsonResponse({"status": "fail", "message": "No se encontro ningun curso"}, status=status.HTTP_404_NOT_FOUND, safe=False)
        course_data = JSONParser().parse(request)

        
            




# @csrf_exempt
# def SaveFile(request):
#     file=request.FILES['file']
#     file_name=default_storage.save(file.name, file)
#     return JsonResponse(file_name, safe=False)
