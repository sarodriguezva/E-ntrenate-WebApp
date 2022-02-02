from pymongo import MongoClient, cursor, errors
from bson import json_util
import json
from bson.objectid import ObjectId

connection_string = "mongodb+srv://dapstab:kidAmnesia@e-ntrenate.nnlqu.mongodb.net/E-ntrenate?retryWrites=true&w=majority"

client = MongoClient(connection_string)
db = client["E-ntrenate"]

# users = db.usuarios.find({})
# users = [json.dumps(doc, default=json_util.default) for doc in users]
# users = list(users)
# userIDs = []
# for i in users:
#     userIDs.append(i["nombre"])

# print(userIDs)
# user = db.usuarios.find_one({"nombre": "David"})
# print(user["_id"])

# course = db.cursos.find_one({"nombre": "Curso de ciencias avanzadas"})
#         # review = foros.find({"curso": course["_id"]}, {"autor": 0, "curso": 0})

# reviews = db.foros.aggregate([
#     {
#         "$match": {"curso": course["_id"]}
#     },
#     {
#         "$lookup": {
#             "from": "usuarios",
#             # "localField": "usuario",
#             # "foreignField": "_id",
#             "let": {"usuarioForo": "$usuario"},
#             "pipeline": [
#                 {
#                     "$match": {
#                         "$expr": {
#                             "_id": "$$usuarioForo" 
#                         }
#                     }
#                 },
#                 {
#                     "$project": {
#                         "_id": 0,
#                         "contraseña": 0,
#                         "correo": 0,
#                         "activo": 0,
#                         "passwordResetExpires": 0,
#                         "passwordResetToken": 0
#                     }
#                 }
#             ],
#             "as": "userData"
#         }
#     }
# ])
# print(course)
# print(list(reviews))

# myCreatedCourses = db.cursos.aggregate([
#             {
#                 "$match": {"creadoPor": ObjectId("61e8b404b9c2aba24df23468")}
#             },
#             {
#                 "$project": {
#                     "_id": 0,
#                     "activo": 0,
#                     "slug": 0,
#                     "creadoPor": 0
#                 }
#             }
#         ])

# myCreatedCourses = json.loads(json_util.dumps(myCreatedCourses))
# print(myCreatedCourses, "ESTE PRINT ESTA BIEN")