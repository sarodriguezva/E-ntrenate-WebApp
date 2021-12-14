from django.http import response
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt # Permite que otros dominios accedan a nuestros API methods
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from Cursos.models import Curso
from Cursos.serializers import CursoSerializer

# import sys, os
# sys.path.append(os.path.abspath(os.path.join('..', 'utils')))

from handler_factory import deleteOne, createOne, updateOne, getAll, getOne

from utils import cursos

# Create your views here.

@csrf_exempt
def cursosAPI(request, courseId=None):
    response = {'status': 'success'}
    print(request.method)
    if request.method == 'GET':
        if courseId:
            course = getOne(cursos, courseId)
            courses_serializer = CursoSerializer(course, safe=False)
            response['data'] = course
            return JsonResponse(course, safe=False)
        courses = getAll(cursos)
        courses_serializer = CursoSerializer(courses, many=True) # Usamos el serializer para convetirlo en un modelo, con las validaciones de python que pusimos en models.py.
        response['data'] = courses
        return JsonResponse(response, safe=False)
    elif request.method == 'POST':
        course_data = JSONParser().parse(request)
        courses_serializer = CursoSerializer(data=course_data)
        courses_serializer.is_valid()
        print(courses_serializer.errors)
        if courses_serializer.is_valid():
            print(type(courses_serializer.data))
            createOne(cursos, courses_serializer.data)
            response['data'] = courses_serializer.data
            return JsonResponse(response, safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PATCH':
        course_data = JSONParser().parse(request)
        # print(type(course_data)) # dict
        updatedCourse = updateOne(cursos, courseId, course_data)
        response['data'] = updatedCourse
        return JsonResponse(response, safe=False)
    elif request.method == 'DELETE':
        deleteOne(cursos, courseId)
        return JsonResponse("Deleted Succesfully", safe=False)


        

