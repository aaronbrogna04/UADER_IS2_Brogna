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


# Gestión de cuentas bancarias: cada cuenta decide si procesa el pago
# o lo delega a la siguiente según su saldo disponible
class CuentaHandler:
    """Gestor abstracto de la cadena de responsabilidad.
    Cada nodo representa una cuenta bancaria. Si tiene saldo suficiente
    procesa el pago; si no, lo delega al siguiente eslabón de la cadena.
    """

    def __init__(self, token: str, saldo_inicial: float,
                 archivo_datos: str, lector_json: JasonReader):
        self._token = token
        self._saldo = saldo_inicial
        self._archivo_datos = archivo_datos
        self._lector_json = lector_json
        self._siguiente = None

    def establecer_siguiente(self, siguiente):
        """Encadena el siguiente gestor y lo retorna para poder seguir encadenando."""
        self._siguiente = siguiente
        return siguiente

    def manejar(self, monto: float) -> bool:
        """Intenta procesar el pago; si no puede, lo delega al siguiente eslabón.
        Returns: True si el pago fue procesado, False si ningún gestor pudo atenderlo.
        """
        if self._saldo >= monto:
            self._procesar(monto)
            return True
        if self._siguiente is not None:
            return self._siguiente.manejar(monto)
        print(f"Pago rechazado: ninguna cuenta tiene saldo suficiente para ${monto}.")
        return False

    def _procesar(self, monto: float) -> None:
        """Descuenta el saldo e imprime el resultado del pago."""
        self._saldo -= monto
        clave_banco = self._lector_json.get_token_key(self._archivo_datos, self._token)
        print(f"Pago de ${monto} procesado exitosamente.")
        print(f" -> Cuenta utilizada: {self._token}")
        print(f" -> Clave del banco : {clave_banco}")
        print(f" -> Saldo restante  : ${self._saldo}\n")

class CuentaToken1(CuentaHandler):
    """Gestor concreto para la cuenta token1 (saldo inicial $1.000)."""
 
 
class CuentaToken2(CuentaHandler):
    """Gestor concreto para la cuenta token2 (saldo inicial $2.000)."""

def main():
    archivo_json = "sitedata.json"
    lector = JasonReader()
 
    print("Sistema de Pagos Automatizado\n")
 
    # Construcción de la cadena: token1 ($1.000) -> token2 ($2.000)
    cuenta1 = CuentaToken1("token1", 1000, archivo_json, lector)
    cuenta2 = CuentaToken2("token2", 2000, archivo_json, lector)
    cuenta1.establecer_siguiente(cuenta2)
 
    # Pruebas: siempre se entra por el primer eslabón de la cadena
    cuenta1.manejar(500)
    cuenta1.manejar(500)
    cuenta1.manejar(500)

if __name__ == "__main__":
    main()