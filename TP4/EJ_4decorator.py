class Numero:
    def __init__(self, valor):
        self.valor = valor

    def obtener(self):
        return self.valor

    def imprimir(self):
        print(f"Valor: {self.obtener()}")


class DecoradorNumero(Numero):
    def __init__(self, numero):
        self.numero = numero

    def obtener(self):
        return self.numero.obtener()


class SumarDos(DecoradorNumero):
    def obtener(self):
        return self.numero.obtener() + 2


class MultiplicarPorDos(DecoradorNumero):
    def obtener(self):
        return self.numero.obtener() * 2


class DividirPorTres(DecoradorNumero):
    def obtener(self):
        return self.numero.obtener() / 3


n = Numero(6)
print("Sin decoradores:")
n.imprimir()

print("\nSolo sumar 2:")
SumarDos(n).imprimir()

print("\nSolo multiplicar por 2:")
MultiplicarPorDos(n).imprimir()

print("\nSolo dividir por 3:")
DividirPorTres(n).imprimir()

print("\nAnidado (sumar 2 → multiplicar por 2 → dividir por 3):")
DividirPorTres(MultiplicarPorDos(SumarDos(n))).imprimir()