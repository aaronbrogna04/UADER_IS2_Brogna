from __future__ import annotations
from abc import ABC, abstractmethod

class Avion:
    def __init__(self) -> None:
        self.partes = []
    
    def agregar_parte(self, parte: str) -> None:
        self.partes.append(parte)
        
    def mostrar(self) -> str:
        return "Avión construido con:\n  - " + "\n  - ".join(self.partes)

class BuilderAvion(ABC):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._avion = Avion()
        
    def obtener_avion(self) -> Avion:
        avion = self._avion
        self.reset()
        return avion
    
    @abstractmethod
    def construir_body(self) -> None:
        pass
    
    @abstractmethod
    def construir_turbinas(self) -> None:
        pass
    
    @abstractmethod
    def construir_alas(self) -> None:
        pass
    
    @abstractmethod
    def construir_tren_aterrizaje(self) -> None:
        pass
    
class BuilderAvionComercial(BuilderAvion):
    def construir_body(self) -> None:
        self._avion.agregar_parte("1 Body")

    def construir_turbinas(self) -> None:
        self._avion.agregar_parte("2 Turbinas")

    def construir_alas(self) -> None:
        self._avion.agregar_parte("2 Alas")

    def construir_tren_aterrizaje(self) -> None:
        self._avion.agregar_parte("1 Tren de aterrizaje")


class Director:
    def __init__(self, builder: BuilderAvion) -> None:
        self._builder = builder

    def construir_avion_completo(self) -> None:
        self.builder.construir_body()
        self.builder.construir_turbinas()
        self.builder.construir_alas()
        self.builder.construir_tren_aterrizaje()


def main():
    builder = BuilderAvionComercial()
    director = Director(builder)
    director.builder = builder

    director.construir_avion_completo()
    avion = builder.obtener_avion()
    print(avion.mostrar())


if __name__ == "__main__":
    main()
