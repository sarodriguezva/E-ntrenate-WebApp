from pymongo import MongoClient

connection_string = "mongodb+srv://dapstab:kidAmnesia@e-ntrenate.nnlqu.mongodb.net/E-ntrenate?retryWrites=true&w=majority"

client = MongoClient(connection_string)
entrenate = client["E-ntrenate"]

usuarios = entrenate["usuarios"]
cursos = entrenate["cursos"]

