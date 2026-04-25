import copy
from abc import ABC, abstractmethod

class Prototype(ABC):
    """Interfaz que define el método de clonación."""

    @abstractmethod
    def clone(self):
        pass

class Notificacion (Prototype):
    """Clase concreta que implementa el patrón Prototype.
    Simula una notificación de una aplicación """
    def __init__(self, app, icono, sonido, remitente, mensaje):
        self.app = app
        self.icono = icono
        self.sonido = sonido
        self.remitente = remitente
        self.mensaje = mensaje

    def clone(self):
        """
        Devuelve una copia profunda del objeto.
        Se utiliza deepcopy para evitar efectos colaterales.
        """

        return copy.deepcopy(self)
    
    def __str__(self) -> str:
        return (f"({self.app}){self.remitente}: {self.mensaje}")

def main () -> None:
    #Prototipo base de Whatsapp
    notificacion_whatsapp = Notificacion(
        app = "Whatsapp",
        icono = "iconoWhatsapp.png",
        sonido = "tonoDefault.mp3",
        remitente = "",
        mensaje = ""
    )
   
    # clonacion
    notificacion_juan1 = notificacion_whatsapp.clone()
    notificacion_juan1.remitente = "Juan"
    notificacion_juan1.mensaje = "Hola. Como estas?"

    #2da mensaje de Juan
    notificacion_juan2 = notificacion_juan1.clone()
    notificacion_juan2.mensaje = "Me pasas lo que hicieron hoy?"

    #Mensaje Maria
    notificacion_maria = notificacion_whatsapp.clone()
    notificacion_maria.remitente = "Maria"
    notificacion_maria.mensaje = "Te mandé el archivo ayer"

    print("=== Nuevo mensaje de Juan ===")
    print(notificacion_juan1)
    print(notificacion_juan2)

    print("\n=== Nuevo mensaje de Maria ===")
    print(notificacion_maria)

if __name__ == "__main__":
    main()
