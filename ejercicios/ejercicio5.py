# Ejercicio 5
# Escribe un programa que pida al usuario el radio de un círculo y calcule el área.

def radio_circulo():
    PI = 3.1415926
    while True:
        try:
            user_input = int(input(" Ingrese el radio del circulo a medir: "))
            area = PI * (user_input ** 2)
            print(f" El area del circulo ingresado es de: {area}")

            print(" Queres calcular otro circulo?",'\n'
                  " - SI", '\n'
                  " - NO")
            user_choice = input(" ").lower()
            if user_choice == "no":
                break
        except ValueError:
            print(" Lo que ingresaste no es un numero, volve a intentar")