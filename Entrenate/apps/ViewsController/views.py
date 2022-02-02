from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt # Permite que otros dominios accedan a nuestros API methods
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.utils import json
from bson.objectid import ObjectId

from .models import cursos
from bson import json_util
import json

# from handler_factory import deleteOne, createOne, updateOne, getAll, getOne
from rest_framework import status

response = {'status': 'success'}
# Create your views here.
@csrf_exempt
def getMyCourses(request):
    if request.method == 'GET':
        myCourses = cursos.aggregate([
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
        response["data"] = json.loads(json_util.dumps(myCourses))
        return JsonResponse(response, status=status.HTTP_200_OK ,safe=False)