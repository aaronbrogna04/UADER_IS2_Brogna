from abc import ABC, abstractmethod

# =====================
# Productos abstractos
# =====================

class PlatoPrincipal(ABC):
    """Interfaz abstracta para plato principal"""

    @abstractmethod
    def servir(self):
        pass

class Postre(ABC):
    """Interfaz abstracta para postre"""

    @abstractmethod
    def servir (self):
        pass


# ==================================
# Productos concretos - Menú vegano
# ==================================
class MilanesaBerenjena(PlatoPrincipal):
    """Principal concreto para menú vegano"""
    
    def servir(self):
        return "Sirviendo milanesa de berenjena"
    
class MousseVegana(Postre):
    """Postre concreto para menú vegano"""
    
    def servir(self):
        return "Sirviendo mousse vegano"

# =====================================
# Productos concreto - Menú tradicional
# =====================================
class MilanesaCarne(PlatoPrincipal):
    """Principal concreto para menú tradidcional"""

    def servir(self):
        return "Sirviendo milanesa de carne"
    
class MousseClasica(Postre):
    """Postre concreto para menú tradidcional"""

    def servir(self):
        return "Sirviendo mousse tradicional"
    
# ================
# Abstract Factory
# ================
class FabricaMenu(ABC):
    """Interfaz abstracta para crear menús con plato principal y postre."""

    @abstractmethod
    def crear_plato_principal(self) -> PlatoPrincipal:
        pass

    @abstractmethod
    def crear_postre(self) -> Postre:
        pass

# ===================
# Fabricas concretas
# ===================
class MenuVegano(FabricaMenu):
    """Fábrica concreta para para menú vegano."""

    def crear_plato_principal(self) -> PlatoPrincipal:
        return MilanesaBerenjena()

    def crear_postre(self) -> Postre:
        return MousseVegana()


class MenuTradicional(FabricaMenu):
    """Fábrica concreta para para menú tradicional."""

    def crear_plato_principal(self) -> PlatoPrincipal:
        return MilanesaCarne()

    def crear_postre(self) -> Postre:
        return MousseClasica()

# =======
# Cliente
# =======
class Restaurante:
    """
    El cliente trabaja solo con interfaces abstractas.
    No depende de clases concretas.
    """

    def __init__(self, fabrica: FabricaMenu) -> None:
        self.plato_principal = fabrica.crear_plato_principal()
        self.postre = fabrica.crear_postre()
    
    def servir_menu(self):
        print(self.plato_principal.servir())
        print(self.postre.servir())

# ==================
# Programa Principal
# ==================

def main () -> None:

    print("=== Menú vegano ===")
    menu_vegano = Restaurante(MenuVegano())
    menu_vegano.servir_menu()

    print("\n=== Menú tradicional ===")
    menu_tradicional = Restaurante(MenuTradicional())
    menu_tradicional.servir_menu()

if __name__ == "__main__":
    main()
