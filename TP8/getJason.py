# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: getJason.py
# Bytecode version: 3.12.0rc2 (3531)
# Source timestamp: 2025-05-06 19:05:36 UTC (1746558336)

import json
import sys
from threading import Lock

class JasonReader:
    _instancia = None
    _lock = Lock()

    def __new__(cls, *args, **kwargs):
        if cls._instancia is None:
            with cls._lock:
                if cls._instancia is None:
                    cls._instancia = super().__new__(cls)
        return cls._instancia

    def __init__(self):
        # Inicializa la configuración solo una vez
        if not hasattr(self, "_inicializado"):
            self._inicializado = True

    def get_token_key(self, filepath: str, token_name: str) -> str:
        # Abre el JSON, extrae la clave y extrae la clave específica del token solicitado
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
            return str(data[token_name])
            
        except FileNotFoundError:
            print(f"Error: El archivo '{filepath}' no fue encontrado.")
            sys.exit(1)
        except json.JSONDecodeError:
            print(f"Error: El archivo '{filepath}' no posee un formato válido.")
            sys.exit(1)
        except KeyError:
            print(f"Error: El token '{token_name}' no se encuentra en el archivo.")
            sys.exit(1)
        except Exception as e:
            print(f"Error inesperado: {e}")
            sys.exit(1)

class ProcesadorDePagos:
    # Componente que automatiza la selección de cuenta
    def __init__(self, archivo_datos: str):
        self.archivo_datos = archivo_datos
        self.lector_json = JasonReader() # Integración del objeto Singleton
        
        # Configuración inicial de cuentas requerida para la automatización
        self.cuentas = {
            "token1": {"saldo": 1000},
            "token2": {"saldo": 2000}
        }
        # Variable para llevar el control del balanceo de pagos
        self.ultimo_token_usado = "token2" 

    def solicitar_pago(self, monto: float) -> None:
        # Selecciona automáticamente la cuenta con saldo e intenta balancear la carga
        # Alternancia básica para pagos balanceados
        token_sugerido = "token1" if self.ultimo_token_usado == "token2" else "token2"
        
        # Verificar si la cuenta sugerida tiene saldo suficiente
        if self.cuentas[token_sugerido]["saldo"] >= monto:
            self._ejecutar_pago(token_sugerido, monto)
            return
            
        # Si no tiene saldo, intentar con la cuenta alternativa
        token_alternativo = "token2" if token_sugerido == "token1" else "token1"
        if self.cuentas[token_alternativo]["saldo"] >= monto:
            self._ejecutar_pago(token_alternativo, monto)
            return
            
        print(f"Solicitud rechazada: No hay saldo suficiente en ninguna cuenta para el monto ${monto}.")

    def _ejecutar_pago(self, token: str, monto: float) -> None:
        # Efectiviza el descuento y obtiene la clave del banco mediante el Singleton
        self.cuentas[token]["saldo"] -= monto
        self.ultimo_token_usado = token
        
        # Utilizar el Singleton para obtener la clave del banco
        clave_banco = self.lector_json.get_token_key(self.archivo_datos, token)
        
        print(f"Pago de ${monto} procesado exitosamente.")
        print(f" -> Cuenta utilizada: {token}")
        print(f" -> Clave del banco: {clave_banco}")
        print(f" -> Saldo restante en {token}: ${self.cuentas[token]['saldo']}\n")

def main():
    # Archivo de datos especificado en los requerimientos
    archivo_json = "sitedata.json" 
    
    print("Sistema de Pagos Automatizado\n")
    procesador = ProcesadorDePagos(archivo_json)
    
    # Pruebas para verificar la automatización y el balanceo
    procesador.solicitar_pago(500)
    procesador.solicitar_pago(500)
    procesador.solicitar_pago(500)


if __name__ == "__main__":
    main()