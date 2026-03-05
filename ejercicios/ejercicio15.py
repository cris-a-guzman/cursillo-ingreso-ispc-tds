# Ejercicio 15
# Escribe un programa que cuente los caracteres de una cadena de texto proporcionada 
# por el usuario utilizando el for.

def contar_string():
    print(" En este programa vas a ingresar una cadena de texto y te va a devolver la cantidad de\n"
          " Caracteres que tiene esa cadena")
    contador = 0
    user_input = input(" Ingresa la cadena: ")
    for i in user_input:
        contador += 1
    print(f" La cantidad de letras que tiene '{user_input}' es: {contador}")


