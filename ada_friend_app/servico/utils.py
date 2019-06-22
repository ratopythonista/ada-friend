from bson import ObjectId

def converter_objectid(resultado):
    for dado in resultado:
        dado['_id'] = str(dado['_id'])
    
    return resultado
