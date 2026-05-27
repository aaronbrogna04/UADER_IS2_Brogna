# getJason.py
# Descripción: Recupera el valor de una clave desde un archivo JSON.
# Uso: python getJason.py <archivo.json> [clave]
# Argumentos:
#   archivo.json : ruta al archivo JSON de entrada (obligatorio)
#   clave        : clave a recuperar del JSON (opcional, default: "token1")

import json
import sys

jsonfile = sys.argv[1]

jsonkey = sys.argv[2] if len(sys.argv) > 2 else "token1"

with open(jsonfile, "r") as myfile:
    data = myfile.read()
    
obj = json.loads(data)
print(str(obj[jsonkey]))
