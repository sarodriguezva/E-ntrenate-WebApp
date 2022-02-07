from typing import Any
from django.shortcuts import render
from bson.objectid import ObjectId
from rest_framework import status
# from .apps.Cursos.models import cursos
# from .apps.Inscripciones.models import inscripciones
# from .apps.Foros.models import foros
from bson import json_util
import json
from django.http.response import JsonResponse
from mongoConnection import db

def home(request: Any):
    """
    Vista de Home
    """
    courses = db.cursos.find({})
    print(courses)
    context = {'base_template': "basetemplate.html", "cursos": list(courses)}

    if request.user.is_authenticated:
        context['auth'] = "True"

    return render(request=request, template_name="home/home.html", context=context)

#tmp for login
def home_login(request: Any):
    context = {'base_template': "basetemplate.html"}

    return render(request=request, template_name="home/user_home.html", context=context)

#tmp for cursos
def cursos(request: Any):
    context = {'base_template': "basetemplate.html"}

    return render(request=request, template_name="cursos/cursos.html", context=context)

def foro(request: Any):
    context = {'base_template': "basetemplate.html"}

    return render(request=request, template_name="foro/foro.html", context=context)

def getMyCreatedCourses(request: Any):
    if request.method == 'GET':
        myCreatedCourses = db.cursos.aggregate([
            {
                "$match": {"creadoPor": ObjectId(request.META["user"]["_id"]["$oid"])}
            },
            {
                "$project": {
                    "_id": 0,
                    "activo": 0,
                    "slug": 0,
                    "creadoPor": 0
                }
            }
        ])
        myCreatedCourses = json.loads(json_util.dumps(myCreatedCourses))
        context = {"myCreatedCourses": myCreatedCourses}
        return render(request=request, template_name="", context=context)

def getMyCourses(request: Any):
    if request.method == "GET":
        # 1) Encontrar todos los cursos inscritos
        cursosInscritos = db.inscripciones.find({"usuario": ObjectId(request.META["user"]["_id"]["$oid"])}, {
            "usuario": 0
        })

        cursosInscritos = list(cursosInscritos)
        # 2) Encontrar cursos con los ID´s dados:
        courseIDs = []
        for course in cursosInscritos:
            courseIDs.append(course["curso"]) 
        
        myCourses = db.cursos.find({"_id": {"$in": courseIDs}})
        context = {"myCourses": myCourses}
        return render(request=request, template_name="", context=context)

def getCourse(request: Any, courseSlug: None):
    if request.method == "GET":
        course = db.cursos.find_one({"slug": courseSlug})
        if not course:
            return JsonResponse({"status": "fail", "message": "No se ha encontrado ningún curso"}, status=status.HTTP_404_NOT_FOUND, safe=False)
        reviews = db.foros.aggregate([
            {
                "$match": {"curso": course["_id"]}
            },
            {
                "$lookup": {
                    "from": "usuarios",
                    # "localField": "usuario",
                    # "foreignField": "_id",
                    "let": {"usuarioForo": "$usuario"},
                    "pipeline": [
                        {
                            "$match": {
                                "$expr": {
                                    "_id": "$$usuarioForo" 
                                }
                            }
                        },
                        {
                            "$project": {
                                "_id": 0,
                                "contraseña": 0,
                                "correo": 0,
                                "activo": 0,
                                "passwordResetExpires": 0,
                                "passwordResetToken": 0
                            }
                        }
                    ],
                    "as": "userData"
                }
            }
        ])
    context = {"course": course, "reviews": reviews}
    return render(request=request, template_name="", context=context)

def getLoginForm(request: Any):
    context = {"nombre": "David Stiven"}
    return render(request=request, template_name="authentication/login2.html", context=context)
