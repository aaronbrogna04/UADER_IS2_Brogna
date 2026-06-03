#!/usr/bin/env python3
"""
getJason.py - Lector de archivos JSON con patrón Singleton.
copyright UADERFCyT-IS2©2024 todos los derechos reservados.

Uso:
    python3 getJason.py <archivo.json> [clave]
    python3 getJason.py -v
"""
import json
import sys
from abc import ABC, abstractmethod

VERSION = "1.1"


class BaseJasonReader(ABC):

    @abstractmethod
    def leer(self, jsonfile, jsonkey):
        """Lee un archivo JSON y retorna el valor de la clave indicada."""


class JasonReaderLegacy(BaseJasonReader):

    def leer(self, jsonfile, jsonkey):
        try:
            with open(jsonfile, "r", encoding="utf-8") as myfile:
                data = myfile.read()
            obj = json.loads(data)
            if jsonkey not in obj:
                print(f"Error: la clave '{jsonkey}' no existe en el archivo JSON.")
                sys.exit(1)
            return str(obj[jsonkey])
        except FileNotFoundError:
            print(f"Error: el archivo '{jsonfile}' no fue encontrado.")
            sys.exit(1)
        except json.JSONDecodeError:
            print(f"Error: el archivo '{jsonfile}' no tiene formato JSON válido.")
            sys.exit(1)


class JasonReader(BaseJasonReader):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def leer(self, jsonfile, jsonkey):
        try:
            with open(jsonfile, "r", encoding="utf-8") as myfile:
                data = myfile.read()
            obj = json.loads(data)
            if jsonkey not in obj:
                print(f"Error: la clave '{jsonkey}' no existe en el archivo JSON.")
                sys.exit(1)
            return str(obj[jsonkey])
        except FileNotFoundError:
            print(f"Error: el archivo '{jsonfile}' no fue encontrado.")
            sys.exit(1)
        except json.JSONDecodeError:
            print(f"Error: el archivo '{jsonfile}' no tiene formato JSON válido.")
            sys.exit(1)


def get_reader(use_legacy=False):
    if use_legacy:
        return JasonReaderLegacy()
    return JasonReader()


def main():

    if len(sys.argv) == 2 and sys.argv[1] == "-v":
        print(f"getJason.py versión {VERSION}")
        sys.exit(0)

    if len(sys.argv) < 2:
        print("Error: faltan parámetros de ejecución.")
        print("Uso: python3 getJason.py <archivo.json> [clave]")
        print("     python3 getJason.py -v")
        sys.exit(1)

    if sys.argv[1].startswith("-") and sys.argv[1] != "-v":
        print(f"Error: opción desconocida '{sys.argv[1]}'.")
        print("Uso: python3 getJason.py <archivo.json> [clave]")
        print("     python3 getJason.py -v")
        sys.exit(1)

    jsonfile = sys.argv[1]
    jsonkey = sys.argv[2] if len(sys.argv) > 2 else "token1"

    reader = get_reader(use_legacy=False)
    resultado = reader.leer(jsonfile, jsonkey)
    print(resultado)


if __name__ == "__main__":
    main()