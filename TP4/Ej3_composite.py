# Ejercicio 3 - Patrón Composite
#*------------------------------------------------------------------------
#* Ingeniería de Software II
#* Patrones Estructurales
#* Composite
#* UADER - Ingeniería de Software II
#*------------------------------------------------------------------------

from abc import ABC, abstractmethod


class ComponenteEnsamblado(ABC):
    """Componente abstracto común para piezas y sub-conjuntos."""

    @abstractmethod
    def obtener_cantidad_piezas(self) -> int:
        pass

    @abstractmethod
    def mostrar(self, indentacion: int = 0) -> None:
        pass


class Pieza(ComponenteEnsamblado):
    """Hoja del Composite."""

    def __init__(self, nombre: str) -> None:
        self.nombre = nombre

    def obtener_cantidad_piezas(self) -> int:
        return 1

    def mostrar(self, indentacion: int = 0) -> None:
        espacio = " " * indentacion
        print(f"{espacio}- Pieza: {self.nombre}")


class SubConjunto(ComponenteEnsamblado):
    """Composite que puede contener piezas u otros sub-conjuntos."""

    def __init__(self, nombre: str) -> None:
        self.nombre = nombre
        self.componentes: list[ComponenteEnsamblado] = []

    def agregar(self, componente: ComponenteEnsamblado) -> None:
        self.componentes.append(componente)

    def remover(self, componente: ComponenteEnsamblado) -> None:
        self.componentes.remove(componente)

    def obtener_cantidad_piezas(self) -> int:
        return sum(c.obtener_cantidad_piezas() for c in self.componentes)

    def mostrar(self, indentacion: int = 0) -> None:
        espacio = " " * indentacion
        print(f"{espacio}+ Sub-conjunto: {self.nombre} ({self.obtener_cantidad_piezas()} piezas)")
        for componente in self.componentes:
            componente.mostrar(indentacion + 4)


def main() -> None:
    producto_principal = SubConjunto("Producto Principal")

    subconjunto_a = SubConjunto("Sub-conjunto A")
    subconjunto_a.agregar(Pieza("Pieza A1"))
    subconjunto_a.agregar(Pieza("Pieza A2"))
    subconjunto_a.agregar(Pieza("Pieza A3"))
    subconjunto_a.agregar(Pieza("Pieza A4"))

    subconjunto_b = SubConjunto("Sub-conjunto B")
    subconjunto_b.agregar(Pieza("Pieza B1"))
    subconjunto_b.agregar(Pieza("Pieza B2"))
    subconjunto_b.agregar(Pieza("Pieza B3"))
    subconjunto_b.agregar(Pieza("Pieza B4"))

    subconjunto_c = SubConjunto("Sub-conjunto C")
    subconjunto_c.agregar(Pieza("Pieza C1"))
    subconjunto_c.agregar(Pieza("Pieza C2"))
    subconjunto_c.agregar(Pieza("Pieza C3"))
    subconjunto_c.agregar(Pieza("Pieza C4"))

    producto_principal.agregar(subconjunto_a)
    producto_principal.agregar(subconjunto_b)
    producto_principal.agregar(subconjunto_c)

    print("=== Ensamblado inicial (3 sub-conjuntos) ===")
    producto_principal.mostrar()
    print()
    print(f"Total de piezas: {producto_principal.obtener_cantidad_piezas()}")

    # Sub-conjunto opcional adicional
    subconjunto_d = SubConjunto("Sub-conjunto D (opcional)")
    subconjunto_d.agregar(Pieza("Pieza D1"))
    subconjunto_d.agregar(Pieza("Pieza D2"))
    subconjunto_d.agregar(Pieza("Pieza D3"))
    subconjunto_d.agregar(Pieza("Pieza D4"))

    producto_principal.agregar(subconjunto_d)

    print()
    print("=== Ensamblado con sub-conjunto opcional agregado ===")
    producto_principal.mostrar()
    print()
    print(f"Total de piezas: {producto_principal.obtener_cantidad_piezas()}")


if __name__ == "__main__":
    main()
