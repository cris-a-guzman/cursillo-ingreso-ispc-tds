# Ejercicio 24
# Escribe una función que permita calcular el factorial de un número.

def factorial():
    print(" En este programa vas a escribir un numero y voy a devolver el factorial de ese numero.")
    factor = 1
    try:
        user_input = int(input(" Ingrese el numero: "))
        if user_input > 0:
            for i in range(user_input, 0, -1):
                factor *= i
        elif user_input < 0:
            print(" Los numeros negativos no estan definidos para los numeros negativos.")
            factor = "Undefined"

    except ValueError:
        print(" Lo ingresado no fue un numero.\n",
              " Intentelo de nuevo.")
    print(factor)
