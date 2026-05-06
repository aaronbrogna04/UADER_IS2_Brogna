from abc import ABC, abstractmethod

class TrenLaminador(ABC):
    @abstractmethod
    def laminar(self, espesor: float, ancho: float) -> str:
        pass

# Implementador 1
class Tren5Mts(TrenLaminador):
    def laminar(self, espesor, ancho):
        return f"Plancha de 5 metros (Dimensiones: {espesor}\" x {ancho}m)"

# Implementador 2
class Tren10Mts(TrenLaminador):
    def laminar(self, espesor, ancho):
        return f"Plancha de 10 metros (Dimensiones: {espesor}\" x {ancho}m)"

# Abstracción: Lámina de Acero
class LaminaAcero:
    def __init__(self, tren: TrenLaminador) -> None:
        self._tren = tren  # Esta es la "puente" (bridge) hacia la implementación
        self._espesor = 0.5
        self._ancho = 1.5

    def producir(self) -> None:
        print(f"Iniciando producción en tren seleccionado...")
        resultado = self._tren.laminar(self._espesor, self._ancho)
        print(f"Resultado: {resultado}")

# Cliente
if __name__ == "__main__":
    print("=== Fábrica de Láminas de Acero ===")
    
    # Producir usando el Tren de 5 metros
    tren_corto = Tren5Mts()
    lamina1 = LaminaAcero(tren_corto)
    lamina1.producir()

    print("-" * 30)

    # Producir usando el Tren de 10 metros
    tren_largo = Tren10Mts()
    lamina2 = LaminaAcero(tren_largo)
    lamina2.producir()