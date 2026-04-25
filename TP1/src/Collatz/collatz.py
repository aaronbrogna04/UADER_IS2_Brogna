import matplotlib.pyplot as plt

# Función que calcula cantidad de iteraciones de Collatz
def collatz_iteraciones(n):
    pasos = 0

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        pasos += 1

    return pasos


# ===================== PROGRAMA PRINCIPAL =====================

numeros = []
iteraciones = []

# Calcula para números del 1 al 10000
for i in range(1, 10001):
    pasos = collatz_iteraciones(i)

    numeros.append(i)
    iteraciones.append(pasos)

# ===================== GRAFICO =====================

plt.figure()
plt.scatter(iteraciones, numeros, s=1)  
plt.xlabel("Iteraciones")
plt.ylabel("Número inicial (n)")
plt.title("Conjetura de Collatz (1 a 10000)")

plt.show()
