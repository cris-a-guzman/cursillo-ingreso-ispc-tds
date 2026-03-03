# Ejercicio 8
# Escribe un programa que a partir de un número entero positivo, muestre por pantalla si es par o impar.
import random as ran
def numero_impar_par():
    print(" En este programa la idea es introducir un numero entero positivo y", '\n'
            " En base a eso te digo si es par o impar.")
    while True:
        user_choice = input(" Preferis introducir un numero (opcion 1) o elijo yo el numero (opcion 2): ")
        if user_choice == "1":
            try:
                user_input = int(input(" Ingresa el numero y te digo si es par o impar: "))
                par = user_input % 2
                if par != 0:
                    print(" Tu numero es impar.")
                elif par == 0:
                    print(" Tu numero es par!.")
            except ValueError:
                print(" El numero ingresado no es valido.", '\n'
                      " Intente de nuevo.")
        elif user_choice == "2":
            num = ran.randint(1,100)
            print(f" El numero que elegi es {num}")
            par = num % 2
            if par != 0:
                print(f" El numero que elegi ({num}) es impar")
            elif par == 0: 
                print(f" El numero que elegi ({num} es par)")
        user_choice = input(" Queres probar otro numero o no? ingresa salir para volver al inicio")
        if user_choice == "salir":
            break