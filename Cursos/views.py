from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt # Permite que otros dominios accedan a nuestros API methods
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.utils import json

from Cursos.models import cursos
from bson import json_util
import json

from handler_factory import deleteOne, createOne, updateOne, getAll, getOne

from django.core.files.storage import default_storage # To store images


# import sys, os
# sys.path.append(os.path.abspath(os.path.join('..', 'utils')))

# Create your views here.
# Aqui van los API methods

@csrf_exempt
def cursosAPI(request, courseId=None):    
    response = {'status': 'success'}
    if request.method == 'GET':
        if courseId:
            course = getOne(cursos, courseId)
            response['data'] = course
            return JsonResponse(response, safe=False)
        courses = getAll(cursos)
        response['data'] = [json.dumps(doc, default=json_util.default) for doc in courses]
        return JsonResponse(response, safe=False)
    elif request.method == 'POST':
        course_data = JSONParser().parse(request)
        createOne(cursos, course_data)
        response['data'] = json.loads(json_util.dumps(course_data))
        return JsonResponse(response, safe=False)
    elif request.method == 'PATCH':
        course_data = JSONParser().parse(request)
        updatedCourse = updateOne(cursos, courseId, course_data)
        response['data'] = updatedCourse
        return JsonResponse(response, safe=False)
    elif request.method == 'DELETE':
        deleteOne(cursos, courseId)
        return JsonResponse("Deleted Succesfully", safe=False)


        

@csrf_exempt
def SaveFile(request):
    file=request.FILES['file']
    file_name=default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)