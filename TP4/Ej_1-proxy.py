from abc import ABC, abstractmethod
import os

# Interfaz común (Sujeto)
class PingInterface(ABC):
    @abstractmethod
    def execute(self, ip_address: str) -> None:
        pass

# Objeto Real
class Ping(PingInterface):
    def execute(self, ip_address: str) -> None:
        if ip_address.startswith("192."):
            print(f"[Ping Real] Realizando 10 intentos a {ip_address}...")
            comando = f"ping -n 10 {ip_address}" if os.name == 'nt' else f"ping -c 10 {ip_address}"
            os.system(comando)
        else:
            print(f"[Ping Real] Error: La dirección {ip_address} no comienza con '192.'")

    def executefree(self, ip_address: str) -> None:
        print(f"[Ping Real - Free] Realizando ping sin restricciones a {ip_address}...")
        comando = f"ping -n 10 {ip_address}" if os.name == 'nt' else f"ping -c 10 {ip_address}"
        os.system(comando)

# Clase Proxy
class PingProxy(PingInterface):
    def __init__(self) -> None:
        self._real_ping = Ping()

    def execute(self, ip_address: str) -> None:
        print(f"\n[Proxy] Evaluando solicitud para IP: {ip_address}")
        
        # Redirección
        if ip_address == "192.168.0.254":
            print("[Proxy] IP especial detectada. Redirigiendo a google.com vía executefree...")
            self._real_ping.executefree("www.google.com")
        else:
            print("[Proxy] Reenviando a método execute estándar...")
            self._real_ping.execute(ip_address)

if __name__ == "__main__":
    proxy = PingProxy()
    # IP válida estándar
    proxy.execute("192.168.0.1")
    
    # IP especial (dispara redirección del proxy)
    proxy.execute("192.168.0.254")
    
    # IP fuera de rango (rechazada por el objeto real)
    proxy.execute("10.0.0.1")