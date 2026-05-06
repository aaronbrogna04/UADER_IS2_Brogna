import math
from threading import Lock


class CalculadoraFactorial:
    _instancia = None
    _lock = Lock()

    def __new__(cls, *args, **kwargs):
        if cls._instancia is None:
            with cls._lock:
                if cls._instancia is None:
                    cls._instancia = super().__new__(cls)
        return cls._instancia

    def __init__(self):
        if not hasattr(self, "_inicializado"):
            self._inicializado = True

    def calcular_factorial(self, n: int) -> int:
        if n < 0:
            return "El número debe ser positivo"
        return math.factorial(n)


# Prueba
def main():
    calc1 = CalculadoraFactorial()
    calc2 = CalculadoraFactorial()

    print(f"¿Son la misma instancia? {calc1 is calc2}")
    print(f"Factorial de 5: {calc1.calcular_factorial(5)}")
    print(f"Factorial de 8: {calc1.calcular_factorial(8)}")
    print(f"Factorial de 3: {calc1.calcular_factorial(3)}")

if __name__ == "__main__":
    main()