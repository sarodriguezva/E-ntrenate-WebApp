from django.db import models

from mongoConnection import db

foroSchema = {
    '$jsonSchema': {
        'bsonType': 'object',
        'additionalProperties': True,
        'required': ['titulo', 'curso', 'autor', 'rol_autor', 'fechaCreacion', 'contenido_foro'],
        'properties': {
            'titulo': {
                'bsonType': 'string',
                'maxLength': 30,
                'minLength': 3,
                # unique index
                # trim
            },  
            'curso': {
                'bsonType': 'string',
                # default con triggers
            },
            'autor':{
                'bsonType': 'string',
            },
            'autor': {
                'bsonType': 'objectId'
            },
            'fechaCreación': {
                'bsonType': 'date'
            },
            'contenido_foro': {
                'bsonType': 'objectId'
            }
        }
    }
}




if 'cursos' not in db.list_collection_names():
    cursos = db.create_collection('foros', validator = foroSchema)
else:
    cursos = db.get_collection('foros')
