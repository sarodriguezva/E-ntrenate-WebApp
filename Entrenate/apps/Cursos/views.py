import datetime
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from bson.objectid import ObjectId

from .models import cursos
from slugify import slugify

from handler_factory import deleteOne, createOne, updateOne, getAll, getOne

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
        course_data["slug"] = slugify(course_data["nombre"], to_lower=True)
        course_data["ratingAverage"] = 4.5
        return createOne(cursos, course_data)   
    elif request.method == 'PATCH':
        course_data = JSONParser().parse(request)
        return updateOne(cursos, courseId, course_data)
    elif request.method == 'DELETE':
        return deleteOne(cursos, courseId)     
        

def cursos(request):
    context = {}
    if request.method == "GET":
        return render(request = request, template_name = "cursos/cursos.html", context = context)
