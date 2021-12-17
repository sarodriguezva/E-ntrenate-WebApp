from utils import db

pipeline = [
    {
        '$match': {'operationType': 'insert'}
    }
]

cursor = db.usuarios.watch(pipeline=pipeline)
print(next(cursor))