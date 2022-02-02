from mongoConnection import db

foroSchema = {
    '$jsonSchema': {
        'bsonType': 'object',
        'additionalProperties': True,
        'required': ['titulo', 'curso', 'usuario', 'comentario'],
        'properties': {
            'titulo': {
                'bsonType': 'string',
                'maxLength': 30,
                'minLength': 3,
                # unique index
                # trim
            },  
            'curso': {
                'bsonType': 'objectId',
                # default con triggers
            },
            'autor':{
                'bsonType': 'string',
            },
            'usuario': {
                'bsonType': 'objectId'
            },
            'fechaCreación': {
                'bsonType': 'date'
            },
            # 'contenido_foro': {
            #     'bsonType': 'objectId'
            # }
            'comentario': {
                "bsonType": "string",
                'maxLength': 500
            },
            "likes": {
                "bsonType": "int",
                'minimum': 0,
            },
            "dislikes": {
                "bsonType": "int",
                'minimum': 0,
            },
        }
    }
}




if 'foros' not in db.list_collection_names():
    foros = db.create_collection('foros', validator = foroSchema)
else:
    foros = db.get_collection('foros')
