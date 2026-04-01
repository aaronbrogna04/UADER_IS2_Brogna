#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys
def factorial(num): 
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

# Si no pasa argumento pedir por teclado
if len(sys.argv) < 2:
    entrada = input("Ingrese un número: ")
else:
    entrada = sys.argv[1]
    

# Detectar si es rango
if "-" in entrada:
    partes = entrada.split("-")
    desde = int(partes[0])
    hasta = int(partes[1])

    for i in range(desde, hasta + 1 ):
        print("Factorial ", i ,"! es ", factorial(i))

else:
    num = int(entrada)
    print("Factorial ", num, "! es ", factorial(num))