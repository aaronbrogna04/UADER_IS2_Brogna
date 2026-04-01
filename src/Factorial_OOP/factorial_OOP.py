import sys

#============= Clase que manja el calculo de factoriales ==============
class Factorial:

    #Constructor
    def __init__(self):
        pass
    
    #Metodo para calcular el factorial
    def calcular (self, num):
        if num < 0:
            print("Factorial de un número negativo no existe")
            return 0
        elif num == 0:
            return 1
        else: 
            fact = 1
            while(num > 1): 
                fact *= num 
                num -= 1
            return fact 
        
    #Metodo para calcular en un rango
    def run(self, min, max):
        for i in range(min, max+1):
            print("Factorial", i, "! es", self.calcular(i))


# ================================ PROGRAMA PRINCIPAL ======================================
#   Creacion de un objeto Factorial
f = Factorial()

# Si no pasa argumento pedir por teclado
if len(sys.argv) < 2:
    entrada = input("Ingrese un número: ")
else:
    entrada = sys.argv[1]
    

# Detectar si es rango
if "-" in entrada:
    partes = entrada.split("-")

    #Caso "-hasta" hacerlo desde 1
    if partes[0] == "":
        desde = 1
        hasta = int(partes[1])

    #Caso "desde-" hacerlo hasta 60
    elif partes[1] == "":
        desde = int(partes[0])
        hasta = 60

    #Caso normal, con ambos valores
    else:
        desde = int(partes[0])
        hasta = int(partes[1])

    f.run(desde, hasta)

else:
    num = int(entrada)
    f.run(num, num)