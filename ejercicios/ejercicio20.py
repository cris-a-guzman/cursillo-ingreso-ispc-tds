# Ejercicio 20
# Crea una lista de números que cuente el número de veces que aparece 
# el número ingresado por el usuario.

import random

def contar_numeros():
    lista = []
    for i in range(11):
        x = random.randint(1,10)
        lista.append(x)
    try:
        user_input = int(input(" Ingresa el numero y te digo cuantas veces aparece en mi lista: "))
        y = lista.count(user_input)
        print(f" El numero que ingresaste ({user_input}) aparece {y} cantidad de veces en mi lista")
    except ValueError:
        print(" Lo que ingresaste no es un numero")
    print(lista)
contar_numeros()