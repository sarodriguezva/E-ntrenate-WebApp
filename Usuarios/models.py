from utils import db

userSchema = {
    '$jsonSchema': {
        'bsonType': 'object',
        'additionalProperties': True,
        'required': ['nombre', 'correo', 'contraseña', 'confirmar_contraseña'],
        'properties': {
            'nombre': {
                'bsonType': 'string',
                'maxLength': 20,
                'minLength': 3,
                # unique index
                # trim
            },
            'correo': {
                'bsonType': 'string',
                'pattern': '^\\S+@\\S+\\.\\S+$',
                'minLength': 6,
                'maxLength': 127
                # lowercase 
                # unique index
                # trim
            },
            'contraseña': {
                'bsonType': 'string',
                'minLength': 8,
                # trim
                # hidden index
            },
            'confirmar_contraseña': {
                'bsonType': 'string',
                # trim
                # trigger o changeStream
            },  
            'foto': {
                'bsonType': 'string',
                # default con triggers
            },  
            'rol': {
                'bsonType': 'string',
                'enum': ['estudiante', 'profesor', 'administrador']
            },
            'passwordChangeAt': {
                'bsonType': 'date' 
            },
            'passwordResetToken': {
                'bsonType': 'string'
            },
            'passwordResetExpires': {
                'bsonType': 'date' 
            },
            'activo': {
                'bsonType': 'bool',
                # hidden index
                # default trigger
            }   
        }
    }
}




if 'usuarios' not in db.list_collection_names():
    print('hola')
    usuarios = db.create_collection('usuarios', validator = userSchema)
else:
    usuarios = db.get_collection('usuarios')