from django.http.response import HttpResponse, JsonResponse
from bson.objectid import ObjectId

def deleteOne(col_name, id):
    document = col_name.find_one_and_delete({'_id': ObjectId(id)})
    if not document:
        HttpResponse(status=404)
        return "No document found with the given ID"
    HttpResponse(status=200)
    return 'Something'
    # return JsonResponse("success", safe=False) 

def updateOne(col_name, id, req_body):
    document = col_name.find_one_and_update({'_id': ObjectId(id)}, {'$set': req_body})
    print(document)
    if not document:
        HttpResponse(status=404)
        return "No document found with the given ID"
    HttpResponse(status=200)
    return document
    # return JsonResponse({"status": "success"} | document, safe=False)

def createOne(col_name, req_body):
    document = col_name.insert_one(req_body)
    HttpResponse(status=201)
    return document
    # return JsonResponse({"status": "success"} | document, safe=False)

def getOne(col_name, id):
    document = col_name.find_one({"_id": ObjectId(id)})
    if not document:
        HttpResponse(status=404)
        return "No document found with the given ID"
    HttpResponse(status=200)
    return document
    # return JsonResponse({"status": "success"} | document, safe=False)

def getAll(col_name):
    documents = col_name.find({})
    HttpResponse(status=200)
    return documents
    # return JsonResponse({"status": "success", "results": len(list(documents))} | documents, safe=False)
