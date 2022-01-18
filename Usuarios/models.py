from mongoConnection import db
import bcrypt

userSchema = {
    '$jsonSchema': {
        'bsonType': 'object',
        'additionalProperties': True,
        'required': ['nombre', 'correo', 'contraseña'],
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
                'bsonType': 'binData',
                'minLength': 8,
                # trim
                # hidden index
            },
            # 'confirmar_contraseña': {
            #     'bsonType': 'string',
            #     # trim
            #     # trigger o changeStream
            # },  
            'foto': {
                'bsonType': 'string',
                # default con triggers
            },  
            'rol': {
                'bsonType': 'string',
                'enum': ['estudiante', 'profesor', 'administrador']
            },
            'passwordChangedAt': {
                'bsonType': 'double' 
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
            },
            'cursos': {
                'bsonType': 'objectId'
            }
        }
    }
}

def get_hashed_password(plain_text_password):
    return bcrypt.hashpw(plain_text_password.encode(), bcrypt.gensalt())


def changedPasswordAfter(JWTTimestamp, user):
    if "passwordChangedAt" in user.keys():
        changedTimestamp = user["passwordChangedAt"]
        print(user["passwordChangedAt"], JWTTimestamp)
        print(user["passwordChangedAt"]-JWTTimestamp)
        return JWTTimestamp < changedTimestamp - 18000 # False means not changed.
    return False

# 16 de enero 2022, iat, 22 de enero cambia contraseña
if 'usuarios' not in db.list_collection_names():
    usuarios = db.create_collection('usuarios', validator = userSchema)
else:
    usuarios = db.get_collection('usuarios')

# Indexes
db.usuarios.create_index(("correo"), unique= True)
# db.usuarios.create_index(("nombre"), unique= True)


# db.usuarios.create_index(("contraseña"), hidden= True)
# db.usuarios.create_index(("confirmar_contraseña"), hidden= True)
