from pymongo import MongoClient, cursor, errors

connection_string = "mongodb+srv://dapstab:kidAmnesia@e-ntrenate.nnlqu.mongodb.net/E-ntrenate?retryWrites=true&w=majority"

client = MongoClient(connection_string)
db = client["E-ntrenate"]
