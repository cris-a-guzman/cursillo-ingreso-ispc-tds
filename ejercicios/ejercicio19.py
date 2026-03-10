# Ejercicio 19
# Crea una lista de números desordenados y ordénala en orden ascendente y descendente.
import random

def ordenar_numeros():
    print(" Este ejercicio tambien es pasivo\n"
          " Voy a crear una lista de numeros y la voy a ordenar de dos formas\n"
          " De forma ascendente y descendente")
    lista = []
    for i in range(11):
        x = random.randint(1,100)
        lista.append(x)
    print(f" La lista que quedo es: {lista}")
    lista.sort()
    print(f" Asi quedo ordenada de forma ascendente: {lista}")
    lista.reverse()
    print(f" Y asi queda ordenada de forma descendente: {lista}")

