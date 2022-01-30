from rest_framework import status
from django.http.response import JsonResponse
from bson.objectid import ObjectId
from bson import json_util
import json




def deleteOne(col_name, id):
    response = {'status': 'success'}
    document = col_name.find_one_and_delete({'_id': ObjectId(id)})
    if not document:
        return JsonResponse({"status": "fail", "message": "No se encontro ningun usuario con el ID dado"}, status=status.HTTP_404_NOT_FOUND, safe=False)
    response["message"] = "Deleted Succesfully"
    return JsonResponse(response, status=status.HTTP_204_NO_CONTENT, safe=False)

def updateOne(col_name, id, req_body):
    response = {'status': 'success'}
    document = col_name.find_one_and_update({'_id': ObjectId(id)}, {'$set': req_body})
    if not document:
        return JsonResponse({"status": "fail", "message": "No se encontro ningun usuario con el ID dado"}, status=status.HTTP_404_NOT_FOUND, safe=False)
    # del req_body["contraseña"]
    # del req_body["confirmar_contraseña"]
    # response['data'] = json.loads(json_util.dumps(req_body))
    response['data'] = json.loads(json_util.dumps(document))
    return JsonResponse(response, status=status.HTTP_200_OK ,safe=False)

def createOne(col_name, req_body):
    response = {'status': 'success'}
    if col_name == "usuarios":
        del req_body["confirmar_contraseña"]
    col_name.insert_one(req_body)
    # del req_body["contraseña"]
    response['data'] = json.loads(json_util.dumps(req_body))
    return JsonResponse(response, status=status.HTTP_201_CREATED, safe=False)

def getOne(col_name, id, popOptions={"contraseña": 0}):
    response = {'status': 'success'}
    document = col_name.find_one({"_id": ObjectId(id)}, popOptions)
    if not document:
        return JsonResponse({"status": "fail", "message": "No se encontro ningun usuario con el ID dado"}, status=status.HTTP_404_NOT_FOUND, safe=False)
    response['data'] = json.loads(json_util.dumps(document))
    return JsonResponse(response, status=status.HTTP_200_OK ,safe=False)

def getAll(col_name):
    response = {'status': 'success'}
    documents = col_name.find({}, {"contraseña": 0})
    response['data'] = [json.dumps(doc, default=json_util.default) for doc in documents]
    response["results"] =  len(response["data"])
    return JsonResponse(response, status=status.HTTP_200_OK, safe=False)

