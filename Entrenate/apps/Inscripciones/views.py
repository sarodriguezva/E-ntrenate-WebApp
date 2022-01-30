import datetime
from .models import inscripciones
from django.http.response import JsonResponse
from bson.objectid import ObjectId
from bson import json_util
import json
from rest_framework import status
from rest_framework.parsers import JSONParser
# Create your views here.
from django.views.decorators.csrf import csrf_exempt # Permite que otros dominios accedan a nuestros API methods

from handler_factory import deleteOne, createOne, updateOne, getAll, getOne

response = {'status': 'success'}

@csrf_exempt
def joinCourse(request):
    if request.method == "POST":
        inscripcion_data = JSONParser().parse(request) # La request debe venir con el curso (ObjectId) y el precio
        inscripcion_data["usuario"] = ObjectId(request.META["user"]["_id"]["$oid"]),
        inscripcion_data["pagado"] = True
        inscripcion_data["fechaCreación"] = datetime.datetime.now()
        # print(request.path, "PATHHHHH") # /api/v1/inscripcion/joinCourse/
        # print(request.path.split("/")[-2]) # joinCourse
        return createOne(inscripciones, inscripcion_data)  
        

