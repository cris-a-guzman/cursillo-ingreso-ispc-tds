# Ejercicio 23
# Escribe una función que reciba como parámetros un nombre y devuelva un saludo personalizado.

def saludo():
    print(" En este programa vas a escribir tu nombre y se devolvera un saludo personalizado.")

    user_input = input(" Ingresa tu nombre: ").strip()
    print(f" Hola {user_input.capitalize} como andas?")