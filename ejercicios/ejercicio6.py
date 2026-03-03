# Ejercicio 6
# Escribe un programa que convierta una temperatura dada en grados Celsius a grados Fahrenheit.

def calcular_grados():

    while True:
        user_choice = input(" Queres calcular Fahrenheit a Celsius (1) o Celsius a Fahrenheit (2)? Para salir ingrese (3)")

        if user_choice == "1":
            while True:
                try:
                    user_F = float(input(" Ingrese los grados en Fahrenheit: "))
                    C = (user_F - 32) * (5/9)
                    print(f" {user_F} grados Fahrenheit equivalen a {C} grados Celsius.")
                    break
                except ValueError:
                    print(" Lo que ingresaste no era un numero, para poner decimales usa '.' ")
        elif user_choice == "2":    
            while True:
                try:
                    user_C = float(input(" Ingrese los grados en Celsius: "))
                    F = user_C * (9/5) + 32
                    print(f" {user_C} grados Celsius equivalen a {F} grados Fahrenheit.")
                    break
                except ValueError:
                    print(" Lo que ingresaste no era un numero, para poner decimales usa '.' ")
        elif user_choice == "3":
            break
        else:
            print(" Opcion invalida.")