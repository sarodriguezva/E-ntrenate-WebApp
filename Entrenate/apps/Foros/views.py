from django.views.decorators.csrf import csrf_exempt # Permite que otros dominios accedan a nuestros API methods
from rest_framework.parsers import JSONParser
from bson.objectid import ObjectId
from .models import foros
from handler_factory import deleteOne, createOne, updateOne, getAll, getOne
from rest_framework import status
from django.http.response import JsonResponse

# Create your views here.
@csrf_exempt
def forosAPI(request, reviewId=None, courseId=None): 
    if request.method == 'PATCH':
        review_data = JSONParser().parse(request) # Solo se puede cambiar el comentario
        return updateOne(foros, reviewId, review_data)
    elif request.method == 'DELETE':
        return deleteOne(foros, reviewId)     

@csrf_exempt
def createReview(request, courseId=None):
    if request.method == 'POST':
        print("ENTRO AQUIIII POST")
        review_data = JSONParser().parse(request)
        review_data["usuario"] = ObjectId(request.META["user"]["_id"]["$oid"])
        review_data["curso"] = ObjectId(courseId)
        return createOne(foros, review_data)   

@csrf_exempt
def getAllReviews(request, courseId=None):
    if request.method == 'GET':
        return getAll(foros)

@csrf_exempt
def getReview(request, reviewId=None, courseId=None):
    if request.method == 'GET':
        return getOne(foros, reviewId)