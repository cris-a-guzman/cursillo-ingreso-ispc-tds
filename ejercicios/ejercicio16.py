# Ejercicio 16
# Escribe un programa que cuente el número de vocales en una cadena de texto 
# proporcionada por el usuario.

def contar_vocales():
    print(" En este programa vas a ingresar una cadena de texto y voy a contar cuantas\n"
          " Vocales tiene tu cadena de texto.")
    contador = 0
    vocales = ["a", "e", "i", "o", "u"]
    user_input = input(" Ingresa tu texto: ")
    for i in user_input:
        if i in vocales:
            contador += 1
    print(f" Tu texto ('{user_input}') tiene {contador} vocales")