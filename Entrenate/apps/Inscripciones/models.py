from mongoConnection import db

inscripcionSchema = {
    '$jsonSchema': {
        'bsonType': 'object',
        'additionalProperties': True,
        'required': ['curso', 'precio', 'usuario'],
        'properties': {
            'curso': {
                'bsonType': 'objectId',
            },
            'precio':{
                'bsonType': 'double',
            },
            'usuario': {
                'bsonType': 'objectId'
            },
            'fechaCreación': {
                'bsonType': 'date'
            },
            "pagado": {
                "bsonType": "bool"
            }
        }
    }
}




if 'inscripciones' not in db.list_collection_names():
    inscripciones = db.create_collection('inscripciones', validator = inscripcionSchema)
else:
    inscripciones = db.get_collection('inscripciones')
