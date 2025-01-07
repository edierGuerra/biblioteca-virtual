from bcrypt import hashpw,gensalt,checkpw

#Hashea la contraseña 
def hash_password(password:str) -> str:
    try:
        salt = gensalt()
        hashed_password = hashpw(password.encode("utf-8"),salt)
        return hashed_password
    except Exception as e:
        print("Error al hashear la contraseña ", e)

#Comprueba la contraseña hasheada 
def validate_password(password:str,hashed_password:str) -> bool:
    validate = checkpw(password.encode("utf-8"),hashed_password.encode("utf-8"))
    return validate
