import bcrypt
from uuid import uuid4
from Usuarios.models import usuarios
import datetime
import hashlib

def get_hashed_password(plain_text_password):
    return bcrypt.hashpw(plain_text_password.encode(), bcrypt.gensalt())

def correctPassword(candidatePassword, userPassword):
    return bcrypt.checkpw(candidatePassword.encode(), userPassword)

def createPasswordResetToken(email):
    resetToken = uuid4().hex
    print(resetToken, "RESET TOKEN")
    print(type(resetToken), "TYPE RESET TOKEN")
    # hashResetToken = bcrypt.hashpw(resetToken.encode(), bcrypt.gensalt())
    hashResetToken = hashlib.sha256()
    hashResetToken.update(bytes(resetToken, encoding="utf8"))
    # print(hashResetToken.hexdigest(), "RESET-TOKEN MODEL")
    # print(type(hashResetToken.hexdigest()), "TYPE OF RESET-TOKEN MODEL")
    usuarios.find_one_and_update({"correo": email}, {"$set":{"passwordResetToken": hashResetToken.hexdigest(), "passwordResetExpires": datetime.datetime.now() + datetime.timedelta(minutes=10)}})
    return resetToken
