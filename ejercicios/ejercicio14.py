# Ejercicio 14
# Escribe un programa que solicite al usuario 5 números enteros 
# y muestre en consola la sumatoria de los mismos.

def sumatoria():
    print(" En este programa vas a ingresar 5 numeros y te voy a devolver la suma de esos numeros")
    suma = 0
    for i in range(6):
        while True:
            try:
                x = int(input(f" Ingresa el {i+1}° numero"))
            except ValueError:
                print(" Lo ingresado no es un numero")
            else:
                suma += x
                break
    print(f" La suma de los numeros ingresados es: {suma}")