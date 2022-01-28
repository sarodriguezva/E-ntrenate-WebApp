from django.http.response import JsonResponse

from Usuarios.models import usuarios, get_hashed_password

from handler_factory import deleteOne, createOne, updateOne, getAll, getOne

from django.core.files.storage import default_storage # To store images
from bson import json_util
import json
from rest_framework import status
 


# Create your views here.
