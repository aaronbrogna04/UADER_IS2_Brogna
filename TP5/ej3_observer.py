from abc import ABC, abstractmethod


class Observador(ABC):
    """Interfaz común para todos los observadores."""

    @abstractmethod
    def actualizar(self, id_emitido: str) -> None:
        pass


class EmisorIDs:
    """
    Sujeto observado.

    Mantiene una lista de observadores y notifica cuando se emite un ID.
    """

    def __init__(self) -> None:
        self._observadores: list[Observador] = []

    def agregar_observador(self, observador: Observador) -> None:
        self._observadores.append(observador)

    def remover_observador(self, observador: Observador) -> None:
        self._observadores.remove(observador)

    def emitir_id(self, id_emitido: str) -> None:
        print(f"\n[EMISOR] ID emitido: {id_emitido}")
        self._notificar(id_emitido)

    def _notificar(self, id_emitido: str) -> None:
        for observador in self._observadores:
            observador.actualizar(id_emitido)


# -------------------------------------------------------------------
# Observadores concretos
# -------------------------------------------------------------------

class ObservadorAB12(Observador):

    def __init__(self) -> None:
        self.id_propio = "AB12"

    def actualizar(self, id_emitido: str) -> None:
        if id_emitido == self.id_propio:
            print(f"[AB12] Coincidencia encontrada con el ID {id_emitido}")


class ObservadorCD34(Observador):

    def __init__(self) -> None:
        self.id_propio = "CD34"

    def actualizar(self, id_emitido: str) -> None:
        if id_emitido == self.id_propio:
            print(f"[CD34] Coincidencia encontrada con el ID {id_emitido}")


class ObservadorEF56(Observador):

    def __init__(self) -> None:
        self.id_propio = "EF56"

    def actualizar(self, id_emitido: str) -> None:
        if id_emitido == self.id_propio:
            print(f"[EF56] Coincidencia encontrada con el ID {id_emitido}")


class ObservadorGH78(Observador):

    def __init__(self) -> None:
        self.id_propio = "GH78"

    def actualizar(self, id_emitido: str) -> None:
        if id_emitido == self.id_propio:
            print(f"[GH78] Coincidencia encontrada con el ID {id_emitido}")


# -------------------------------------------------------------------
# Programa principal
# -------------------------------------------------------------------

def main() -> None:

    emisor = EmisorIDs()

    # Crear observadores
    obs1 = ObservadorAB12()
    obs2 = ObservadorCD34()
    obs3 = ObservadorEF56()
    obs4 = ObservadorGH78()

    # Suscribir observadores
    emisor.agregar_observador(obs1)
    emisor.agregar_observador(obs2)
    emisor.agregar_observador(obs3)
    emisor.agregar_observador(obs4)

    # Emitir 8 IDs
    ids = [
        "AB12",
        "XXXX",
        "CD34",
        "ZZZZ",
        "AAAA",
        "EF56",
        "GH78",
        "BBBB"
    ]

    for id_emitido in ids:
        emisor.emitir_id(id_emitido)


if __name__ == "__main__":
    main()