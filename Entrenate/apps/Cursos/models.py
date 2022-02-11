from mongoConnection import db

cursoSchema = {
    '$jsonSchema': {
        'bsonType': 'object',
        'additionalProperties': True,
        'required': ['nombre', 'creadoPor', 'fechaCreación', 'duración', 'lecturas', 'lenguajes', 'nivelCurso'],
        'properties': {
            'nombre': {
                'bsonType': 'string',
                'maxLength': 20,
                'minLength': 3,
                # unique index
                # trim
            },
            'imagenPrincipal': {
                'bsonType': 'string',
                # default con triggers
            },
            'creadoPor': {
                'bsonType': 'objectId'
            },
            'fechaCreación': {
                'bsonType': 'date'
            },
            'secciones': {
                'bsonType': 'objectId'
            },
            'duración': {
                'bsonType': 'int'
            },
            'activo': {
                'bsonType': 'bool'
            },
            'descripción': {
                'bsonType': 'string',
                'maxLength': 2000,
            },
            'instructorInfo': {
                'bsonType': 'string',
                'maxLength': 2000,
            },
            'tags': {
                'bsonType': ['string']
            },
            'lecturas': {
                'bsonType': 'int'
            },
            'lenguajes': {
                'bsonType': ['string']
            },
            'subtitulos': {
                'bsonType': 'bool'
            },
            'estudiantes': {
                'bsonType': 'int'
            },
            'nivelCurso': {
                'bsonType': 'string',
                'enum': ['All Levels', 'Beginner', 'Intermediate', 'Expert']
            },
            'ratingQuantity': {
                'bsonType': 'int'
            },
            'ratingAverage': {
                'bsonType': 'double',
                'minimum': 1,
                'maximum': 5
            },
            'resumen': {
                'bsonType': 'string',
                'maxLength': 500
            },
            'precio': {
                'bsonType': 'double'
            },
            'descuento': {
                'bsonType': 'int'
            },
            "slug": {
                'bsonType': 'string'
            }
        }
    }
}




if 'cursos' not in db.list_collection_names():
    cursos = db.create_collection('cursos', validator = cursoSchema)
else:
    cursos = db.get_collection('cursos')
